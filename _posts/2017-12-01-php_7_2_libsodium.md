---
layout:     post
title:      Rencontre avec Libsodium
date:       2017-12-07
summary:    Venez découvrir la bibliothèque de chiffrement Libsodium — PHP 7.2.0
categories: php
---

Ca y'est !  
A moins d'être resté cloîtré dans une grotte, vous aurez largement lu que PHP 
7.2 est sorti depuis exactement une semaine !  
Cette nouvelle version apporte plusieurs nouveautés 
([typage en `object`](https://wiki.php.net/rfc/object-typehint), 
[etc.](http://php.net/archive/2017.php#id2017-11-30-1)), et introduit plusieurs 
améliorations de sécurité.  
Dont une nouvelle extension [sodium](https://download.libsodium.org/doc/) qui 
fait de PHP le premier langage de programmation à adopter le chiffrement 
moderne dans sa bibliothèque standard !

Sodium est une bibliothèque cryptographique qui prend en charge des abstractions 
de haut niveau pour le chiffrement, le déchiffrement, la signature, 
le hachage des mots de passe et plus encore.  
C'est une copie d'un projet antérieur, [NaCl](http://nacl.cr.yp.to/), 
une bibliothèque de réseaux et de cryptographie.  
L'objectif des deux projets est de fournir aux programmeurs un outil rapide et 
facile à utiliser pour travailler avec le chiffrement en toute sécurité et avec 
lequel ils peuvent construire des outils encore plus performants pour les 
utilisateurs finaux.

Contrairement à de nombreuses autres bibliothèques cryptographiques, Sodium se 
concentre sur les schémas de chiffrage authentifiés.  
Cela signifie que chaque pièce de données chiffrées porte automatiquement un 
code d'authentification de message (MAC, Message Authentication Code) qui peut 
valider l'intégrité des données elles-mêmes.  
Si le MAC s'avère invalide, Sodium produira immédiatement une erreur.  
Utiliser un MAC pour valider un message chiffré n'est pas en soi un trait 
unique.  
Cependant, beaucoup d'autres bibliothèques laisseront au développeur final le 
soin d'implémenter la validation MAC.  
Sodium intègre cette primitive dans la bibliothèque elle-même afin de mieux 
faire respecter les bonnes pratiques en matière d'intégrité des messages.

La force d'une clé privée RSA est liée à la fois à sa longueur et à la 
puissance de calcul d'un attaquant.  
Une clé plus longue nécessite plus de puissance de calcul pour déchiffrer et 
rend donc chaque "devinette" d'un attaquant quelque peu coûteux.  
Au fur et à mesure que les ordinateurs gagnent en vitesse et en performance 
globale, les clés autrefois considérées comme sûres deviennent faibles.

Donc quand vous créez une clé secrète, appelée passphrase, arrêtez de rentrer 
un mot de passe et tapez réellement une phrase ;)

Sodium utilise un autre type de mathématiques pour la cryptographie.  
Plutôt que de miser sur les nombres premiers et la factorisation, Sodium utilise 
des calculs mathématiques défini par une [courbe elliptique](https://www.miximum.fr/blog/cryptographie-courbes-elliptiques-ecdsa/).  
Le calcul lui-même est un peu plus complexe, mais donne une relation de clé 
publique/privée similaire à la clé RSA traditionnelle.  
Cependant, en raison des calculs mathématiques, une clé elliptique de 256 bits 
est aussi puissante qu'une clé RSA de 3072 bits.

Bien que Sodium soit pris en charge nativement à partir de PHP 7.2, certains 
projets pourraient vouloir exploiter les mêmes interfaces cryptographiques sur 
des platesformes utilisant des versions plus anciennes de PHP.  
Heureusement, c'est possible grâce à deux projets.  
Avant que Sodium ne soit en PHP nativement, il était disponible sous forme 
d'extension [PECL](https://pecl.php.net/package/libsodium).  
Toute personne exécutant au moins PHP 7.0 peut installer le module PECL et aura 
le même niveau de fonctionnalité et de support que ceux qui utilisent les 
compilations natives en 7.2.  
Le module PECL et l'extension PHP du noyau sont écrits par les mêmes auteurs, 
de sorte qu'il n' y a aucun compromis sur les environnements plus anciens.

Certains développeurs n'ont pas encore mis à jour vers PHP7, cependant.  
Pour ces équipes, le module [`sodium_compat`](https://github.com/paragonie/sodium_compat) 
de Paragon Initiative9 est la voie à suivre.  
Ce module implémente Sodium en PHP s'il n' y a pas d'extension native disponible 
pour exposer l'API.  
Il est beaucoup plus lent à chiffrer et déchiffrer de cette façon mais signifie 
que les anciens serveurs peuvent toujours utiliser Sodium même sans 
distribution binaire.  
En fait, `sodium_compat` est une approche solide pour tous ceux qui travaillent 
avec Sodium et qui souhaitent maintenir une rétrocompatibilité avec PHP.  
Le module essaiera d'utiliser les fonctionnalités natives de PHP 7.2 si elles 
sont disponibles.  
Il recherchera automatiquement l'extension PECL sur les anciens systèmes et 
l'utilisera si elle est prise en charge.  
Enfin, sur les anciens systèmes sans module PECL pour Sodium, le polyfill 
chargera une implémentation PHP des primitives cryptographiques.  
L'utilisation de `sodium_compat` signifie que vous pouvez écrire votre code une 
fois puis le reporter à la bibliothèque pour choisir la meilleure implémentation  
pour vous.

### Comment chiffrer les données ?

Libsodium rend la cryptographie à clé symétrique (où une seule clé de 
chiffrage/déchiffrage est partagée par les deux parties impliquées) simple avec 
les fonctions `sodium_crypto_secretbox()` et `sodium_crypto_secretbox_open()`.  
La première fonction est utilisée pour chiffrer un message de chaîne de 
caractères avec un nombre arbitraire aléatoire et une clé symétrique spécifique.

{% highlight php %}
<?php

// Création nombre arbitraire
$nonce = random_bytes(SODIUM_CRYPTO_SECRETBOX_NONCEBYTES);

// Création d'une clé secrète
$key = sodium_crypto_secretbox_keygen();

// Notre message à chiffrer
$message = 'Notre message super secret!';

/**
 * Chiffrer le message, et stocker le texte chiffré résultant avec le nonce.
 * Contrairement à la clé, le nonce n'a pas besoin d'être secret tant qu'il 
 * continue d'être généré aléatoirement à chaque fois.
 */
$cipher = sodium_crypto_secretbox($message, $nonce, $key);

// Déchiffrer le texte chiffré en utilisant la même clé et nonce
$decipher = sodium_crypto_secretbox_open($cipher, $nonce, $key);

echo $decipher . PHP_EOL;
{% endhighlight %}

[L'exemple à tester online](https://3v4l.org/CLWVB)

La clé est un secret partagé; notre nonce doit être unique pour chaque 
opération de chiffrage mais ne doit pas être gardé secret.  
Déchiffrer notre message est exactement comme le chiffrage, seulement à l'envers.  
Libsodium utilise un chiffrage authentifié pour chaque transaction.  
Le message est à la fois chiffré et muni d'un code d'authentification de message 
(MAC) pour vérifier que le message n' a pas été falsifié.  
Lors du déchiffrage du message, Sodium vérifiera que personne n'a altéré le 
message et vérifiera automatiquement l'erreur s'il a été modifié.

### Chiffrement authentifié par clé publique

Une des façons dont Sodium brille vraiment est la cryptographie à clé publique.  
Dans ce paradigme, chaque utilisateur a une paire de clés - une clé est gardée 
secrète tandis que l'autre est partagée avec le monde.  
N'importe qui peut chiffrer un message pour un utilisateur particulier avec sa 
clé publique; il ne peut être lu qu'avec sa clé privée.  
De même, un utilisateur peut signer une donnée avec sa clé privée; un tiers 
peut utiliser la clé publique déjà distribuée pour vérifier la signature.
Beaucoup de gens sont familiers avec 
[RSA](https://fr.wikipedia.org/wiki/Chiffrement_RSA), qui est un ancien style 
de cryptographie à clé publique qui utilise de grands nombres premiers, 
l'exponentiation et l'arithmétique modulo pour construire la sécurité.    
Les clés concernées doivent être assez grandes pour garantir la confidentialité; 
l'[Institut National des Normes et de la Technologie](https://www.nist.gov/) 
recommande des clés [RSA d'au moins 3072 bits](https://www.keylength.com/fr/4/).

De même, Sodium introduit des méthodes simples pour alimenter le cryptographe 
avec des clés asymétriques (où une clé publique est distribuée pour le chiffrage, 
et une clé privée est utilisée pour le déchiffrage).  
Ces fonctions sont simplement nommées `sodium_crypto_box()` et 
`sodium_crypto_box_open()`.  
Comme pour le modèle de clé secrète ci-dessus, le chiffrage nécessite un nonce 
unique pour chaque opération (et le déchiffrage nécessite le même nonce).  
En utilisant un chiffrage authentifié par clé publique, Bob peut chiffrer un 
message confidentiel spécifiquement pour Alice, en utilisant la clé publique 
d'Alice.

{% highlight php %}
<?php

/**
 * La fonction sodium_crypto_box_keypair() génère aléatoirement une clé secrète
 * et une clé publique correspondante.
 */
$aliceKeypair = sodium_crypto_box_keypair();
$alicePublicKey = sodium_crypto_box_publickey($aliceKeypair);
$aliceSecretKey = sodium_crypto_box_secretkey($aliceKeypair);

$bobKeypair = sodium_crypto_box_keypair();
$bobPublicKey = sodium_crypto_box_publickey($bobKeypair);
$bobSecretKey = sodium_crypto_box_secretkey($bobKeypair);

$message = 'Bonjour, c\'est Alice.';

/**
 * Le nombre arbitraire n'a pas besoin d'être confidentiel, mais il doit être
 * utilisé avec une seule invocation de crypto_box_open() pour une paire
 * particulière de clés publiques et secrètes.
 */
$nonce = random_bytes(SODIUM_CRYPTO_SECRETBOX_NONCEBYTES);

/**
 * Créer une paire de clés à partir d'une clé secrète (celle d'alice) et d'une
 * clé publique (bob)
 */
$aliceToBobKeyPair = sodium_crypto_box_keypair_from_secretkey_and_publickey($aliceSecretKey, $bobPublicKey);

// Chiffrer le message
$aliceToBobCiphertext = sodium_crypto_box($message, $nonce, $aliceToBobKeyPair);

/**
 * Créer une paire de clés inverse pour déchiffrer le message
 */
$bobToAliceKp = sodium_crypto_box_keypair_from_secretkey_and_publickey($bobSecretKey, $alicePublicKey);

$aliceMessageDecryptedByBob = sodium_crypto_box_open($aliceToBobCiphertext, $nonce, $bobToAliceKp);

echo $aliceMessageDecryptedByBob . PHP_EOL;
{% endhighlight %}

[L'exemple à tester online](https://3v4l.org/UtnS7)

Bon à part la fonction `sodium_crypto_box_keypair_from_secretkey_and_publickey` 
qui a un nom 10 fois trop long, elle s'occupe de tout faire automatiquement.  
L'équivalent sur l'API libsodium serait la fonction `crypto_box_open_easy()`.

En envoyant un message à un tiers, vous envoyez le texte chiffré, le nonce qui 
a servi à le générer, ainsi que votre clé publique.  
Lorsque Sodium commence à déchiffrer le message, il vérifiera un code 
d'authentification du message pour authentifier le message et utilisera votre 
clé privée pour l'authentifier et le déchiffrer.  
Non seulement le destinataire peut vérifier que vous avez bien envoyé le 
message, mais il peut aussi vérifier que quelqu'un d'autre l'a manipulé.  
Comme pour le déchiffrage symétrique ci-dessus, cette opération est authentifiée.  
Si le MAC apposé sur le message n'est pas validé, le message a été manipulé en 
transit et l'opération de déchiffrage est interrompue.

Voilà pour un petit tour du propriétaire !  
Pour plus d'informations vous pouvez aller lire la documentation de 
[sodium](https://download.libsodium.org/doc/).

Et n'oubliez pas ;)  
[On dit chiffrer pas crypter](https://i.imgur.com/SyOejxK.gif)

P.S. : Après avoir discuté avec [@greg0ire](https://twitter.com/greg0ire), voici 
une définition de la différence entre un MAC et une signature :

> Ils sont utilisés dans des contextes complètement différents.  
> Dans le chiffrement à clé publique, il y a la notion de signature qui protège 
l'authenticité de l'expéditeur.  
> La clé secrète est utilisée comme clé de signature et tout le monde peut 
vérifier son exactitude.  
> Et de l'autre côté, dans le cryptage symétrique, il y a la notion de MAC qui 
protège l'intégrité du message avec une clé MAC convenue entre l'expéditeur et 
le destinataire.
