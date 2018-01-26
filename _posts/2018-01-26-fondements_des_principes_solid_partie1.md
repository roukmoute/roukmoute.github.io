---
layout:     post
title:      Fondements des principes SOLID — Partie 1
date:       2018-01-26
summary:    Comment est né le principe SOLID ?
categories: solid
---

On nous parle souvent de faire un code SOLID.  
Mais au fait, de quoi s'agit-il ?

Cet article étant long, j'ai décidé de le couper en deux.  
Cela peut paraitre long, mais je pense que savoir comment est né l'acronyme 
SOLID est important.  
Il n'y a que de la théorie dans cet article.  
Bonne lecture.

### Comment est née l'idée ?

L'acronyme SOLID est né de [Michael Feathers](https://www.r7krecon.com/legacy-code) et [Robert C. Martin](http://blog.cleancoder.com/).  
Leur idée est venue de Jack Reeves qui a publié un article intitulé 
[« What Is Software Design? »](https://www.developerdotstar.com/mag/articles/reeves_design.html)  
La question principale étant : « Que produisent les ingénieurs ? »  
Réponse: Les ingénieurs produisent des documents qui décrivent comment 
concevoir des produits.  

Cela est vrai dans bien des domaines :

- Les architectes en bâtiment produisent des documents, des plans, des schémas 
de construction qui décrivent comment concevoir un bâtiment.
- Les ingénieurs en électronique produisent des schémas de circuit électriques 
qui décrivent comment concevoir une carte de circuit imprimé.  
- Les ingénieurs mécaniciens produisent des documents de dessins mécaniques qui 
décrivent comment concevoir les machines.  

Et pour ce qui est du développement de logiciel, le seul document produit par 
les ingénieurs logiciels qui est suffisamment détaillé pour spécifier un 
produit logiciel est le code source.  
Les autres documents, comme les diagrammes UML, cahier des charges, où tout 
autre document servant à écrire le code source n'en fait pas partie.  
Ils servent à déterminer le code source, pas à produire le document.  
Le document finalisé chez nous sera un binaire ou un site Internet.  
Le code source en est donc la conception.

Et c'est là où il y a une conclusion très intéressante entre les ingénieurs 
logiciels et les autres ingénieurs cités précédemment.  
Dans les exemples précédents, nous passons beaucoup de temps à concevoir le 
document, car le coût de leur conception est beaucoup moins élevé que celui 
de la construction.  
Et le coût de la correction des erreurs une fois la conception terminée et la 
production commencée est énorme.  
Mais dans le logiciel, c'est tout l'inverse, il est bien moins astronomique de 
construire le produit qu'il ne l'est de le concevoir et de corriger les erreurs 
avant la sortie qui est très bon marché.  
En fait, même une fois fini, le coût de réparation des erreurs est beaucoup 
moins cher que de changer les fondations d'une maison.  
Pour les logiciels, le coût de construction c'est le coût de la compilation 
ainsi que des tests.  
Pour compiler un million de lignes d'application en quelques secondes, je peux 
le tester en quelques minutes.  
Enfin la résolution des problèmes à l'intérieur de celui-ci sera une question 
d'heures.  
Donc pour les logiciels, le coût de construction est bon marché.  
Est-ce que si nous pouvions construire une maison pour 100 € de l'heure et en 
même temps pouvoir effectuer des modifications nous prendrions un architecte ?  
Bien sûr que non, eh bien pour le code c'est un peu pareil, voilà pourquoi le 
développeur coûte cher.  
À chaque changement que vous allez vouloir, vous allez payer le développeur 
pour qu'il fasse ce que vous souhaitiez, maintenant que l'on sait que la 
construction du logiciel ne prendra que quelques minutes tout au plus.  
En revanche, pour une nouvelle évolution, il n'y a aucune garantie que nous 
le concevions correctement.  
Il est facile de faire évoluer un design en quelque chose qui fonctionne.  
Malheureusement, il est aussi facile de le rendre difficile à modifier, 
difficile de maintenir.  
Nous savons qu'une bonne série de tests élimine la peur et nous permet de 
garder notre code constamment propre.  
Nous devons pratiquer le développement piloté par les tests (TDD) et faire 
beaucoup d'efforts pour garder notre code toujours propre.  
Le problème, c'est que pour nettoyer nos conceptions, nous devons être en 
mesure de reconnaître quand elles tournent mal.  
Il faut qu'on sache que le design sent mauvais.

###  Quels sont les symptômes d'une mauvaise conception ?

Comment savoir quand la conception de nos systèmes commence à se dégrader ?  
Pour répondre à cette question, nous allons examiner de plus près la rigidité, 
la fragilité, l'immobilité, la viscosité et la complexité inutile.  
Comment pouvons-nous identifier ces mauvaises odeurs et les nettoyer avant 
qu'elles ne deviennent un problème important ?  
Voici donc un top 5 des symptômes d'un code qui sent mauvais, et qui nous 
amèneront donc à faire du code dit SOLID.

#### Rigidité

La rigidité est la tendance d'un système à être difficile à changer, même de 
façon simple.  
Qu'est-ce qui rend un système difficile à changer ?  
Il est difficile de changer un système lorsque le coût du changement est élevé.
Par exemple, si en faisant un petit changement je dois modifier toute une 
partie de mon code, alors ce système est rigide.  
Ce qui a commencé par un simple changement de deux jours en un seul module 
devient un marathon de changement de plusieurs semaines.  
Disons maintenant que vous avez un système qui nécessite trois heures pour le 
construire et le tester.  
Disons aussi que le changement le plus mineur au sous-système le moins 
important de ce système nécessite une compilation et un test de trois heures.  
Ce système est rigide.
Plus cela se produira, plus les gestionnaires et les clients seront mal à 
l'aise et finiront par geler le développement et plus la rigidité 
officielle s'installera.

Cela arrive sur deux choses :

- Quand il faut beaucoup de temps pour faire un test
- Quand un petit changement provoque une cascade de modifications ultérieures 
dans les classes dépendantes.

Si nous pouvions réduire considérablement le temps de construction et d'essai, 
nous pourrions rendre le système beaucoup moins rigide et beaucoup plus facile 
à changer.  
Si nous pouvions trouver un moyen de restructurer le système de telle sorte que 
lorsque vous l'avez modifié, vous n'auriez pas à reconstruire et à refaire tous 
les tests.  
Les changements seraient alors beaucoup plus faciles à apporter et le système 
serait beaucoup moins rigide.

En général, cependant, lorsque les tests prennent beaucoup de temps à 
fonctionner, c'est une bonne indication que nous, développeurs, avons été 
négligents.

Lorsque de petits changements forcent la recompilation, c'est aussi le symptôme 
d'un couplage élevé.  
Et pour finir lorsque des classes sont couplées et que de minuscules 
changements ont entraîné de revoir l'ensemble de toutes ces classes.  
Par conséquent, l'un de nos objectifs de conception est de gérer les 
dépendances entre les classes pour s'assurer que lorsqu'une classe change, 
les autres ne sont pas affectées.

#### Fragilité

La fragilité est étroitement liée à la rigidité.
Un système est fragile lorsqu'une petite modification d'une classe entraîne 
un comportement erroné d'autres classes indépendantes.  
Imaginez un logiciel de domotique, ce logiciel serait fragile si, lorsque vous 
installez un thermostat, celui-ci se met à baisser aussi lorsque vous baissez 
les volets.  
Ce genre de dépendance comportementale n'est pas bonne du tout.  
Surtout du point de vue des managers et des clients qui les considèrent comme 
des indices d'incompétence significative.  
Après tout, si chaque fois que les développeurs corrigent un bug ou ajoutent 
une nouvelle fonctionnalité, quelque chose de complètement indépendant cassé ou 
planté, la seule conclusion à laquelle ils peuvent arriver est que nous avons 
perdu le contrôle de notre logiciel et ne savons pas ce que nous faisons.  
La méfiance règne et la crédibilité est perdue.  
Ce genre de problème est toujours causé par d'étranges couplages et dépendances 
qui serpentent à travers le système.  
La solution est de gérer les dépendances entre les classes et de les isoler les 
uns des autres.

#### Immobilité

Un système est immobile lorsque ses composants internes ne peuvent pas être 
facilement extraits et réutilisés dans de nouveaux environnements.  
Prenons par exemple le cas d'un système dans lequel il existe une classe type 
pour s'identifier avec un nom d'utilisateur et un mot de passe.  
Si vous ne pouvez pas extraire rapidement cette classe de connexion et 
l'utiliser dans un système complètement différent, alors cette classe est 
immobile, elle ne peut pas être déplacée.  
L'immobilisation est causée par les couplages et dépendances dans les classes 
du système.  
Cependant, il arrive aussi souvent que la classe en question ait trop de 
paramètres dont elle dépend.  
Le travail et le risque requis pour séparer les parties souhaitables du 
logiciel des parties indésirables sont trop grands pour être tolérés.  
Par exemple, disons que j'ai une classe de connexion qui utilise un schéma 
de base de données et un schéma d'interface utilisateur particulier.  
Je ne pourrais pas réutiliser cette classe de connexion dans un système 
différent s'il avait un schéma de base de données différent et un schéma 
d'interface utilisateur différent.  
Ce module de connexion serait immobile.  
Cette partie du logiciel est donc simplement réécrite au lieu d'être réutilisée.

#### Viscosité

Le système est visqueux lorsque les opérations nécessaires comme la 
construction et les tests sont difficiles à réaliser et prennent beaucoup de 
temps.  
C'est la résistance au changement.  
La conception de nouvelles fonctionnalités qui doivent être ajoutées à travers 
plusieurs couches du système pour traiter l'information, à travers divers 
mécanismes comme la sérialisation ou l'hydratation.  
Du coup, c’est toujours visqueux parce que, même le changement le plus simple 
coûte cher.  
La cause de la viscosité est toujours la même: la tolérance irresponsable.  
Et cela porte plusieurs petits noms : `hacking`, `quick and dirty` ou encore 
`quick win`.  
C'est facile de faire la mauvaise chose, mais il est plus difficile de faire la 
bonne chose.  
Nous, les développeurs, tolérons des conditions que nous savons mauvaises et ne 
faisons rien pour les corriger.  
Le coût de ces mauvais comportements est le couplage.  
Un couplage rigide rend les systèmes difficiles à construire, à tester et à 
changer.  
C'est ce couplage rigide qui rend le coût de ces opérations essentielles élevé.  
Le traitement pour la viscosité est d'attaquer les symptômes en découplant les 
classes puis en gérant les dépendances qui restent.

#### Complexité inutile

Un véritable problème commun dans les discussions sur la conception de 
logiciels est de savoir comment gérer l'avenir.  
Devrions-nous concevoir notre système que pour répondre aux exigences 
actuelles ?  
Ou bien devrions-nous envisager à long terme et anticiper toutes les exigences 
futures du système ?  
En d'autres termes, devrions-nous verrouiller pour des extensions futures ou 
non ?  
Les systèmes qui portent beaucoup d'anticipation sont inutilement complexes.  
Chaque nouveauté est un autre poids ajouté au système auquel nous devons faire 
attention dans le présent.  
Lorsque vous avez peur de votre code et que vous pensez qu'il est difficile et 
coûteux de le modifier, vous allez alors l'intégrer à votre code avec toutes 
sortes d'éléments de conception anticipatifs.  
Pour que vous n'ayez pas à changer le design plus tard.  
Par contre, suivre une règle simple comme le TDD, vous n'aurez pas peur de 
changer le code.  
Vous n'aurez pas besoin de jongler avec un tas d'éléments anticipatifs, vos 
designs seront plus simples, plus faciles à entretenir et ils ne seront pas 
inutilement complexes.  
La complexité inutile conduit souvent à un couplage fort, car nous anticipons le 
besoin futur de relations entre des classes qui ne sont pas liées actuellement.  
Plus nous anticipons de telles relations futures, plus le logiciel devient 
étroitement couplé.  
La solution, bien sûr, est de garder votre conception axée sur la suite 
actuelle des exigences tout en maintenant une suite complète de tests qui 
réduit votre crainte de changer la conception plus tard.  
Personne ne commence à concevoir un système qui sent mauvais.  
Les mauvaises odeurs s'accumulent au fil du temps.  
Elles sont causées par une série de mauvaises décisions motivées par 
l'insouciance, la peur et de fausses opportunités.  
Plus le désordre est grand, plus il est difficile de progresser, plus tout 
devient difficile.  
Et plus la tentation est grande de prendre le genre de raccourcis qui 
augmentent le désordre.  
Vous aurez peut-être déjà entendu les termes YAGNI (You Ain't Gonna Need It) et 
KISS (Keep It Simple Stupid).    
Attention toutefois à ne pas confondre `Simple` et `Simpliste`.

### Conclusion

Voilà pour la première partie de cet article.  
Ces cinq symptômes sont les signes révélateurs d'une mauvaise architecture.  
Toute application qui les expose souffre d'un design qui pourrit de l'intérieur 
vers l'extérieur.  

##### Mais qu'est-ce qui cause cette pourriture?
  
Ce sera le but du prochain article.  
Pour cela nous regarderons un code qui pourrit.  
Nous commencerons avec un design agréable et propre et regardons changement 
après changement une dégradation de ce design en une sorte de tumeur qui se 
répand.  
Ensuite, nous étudierons une conception alternative qui ne pourrit pas lorsque 
les mêmes changements sont appliqués.  
Nous étudierons la différence entre ces deux conceptions et découvrirons le 
principe qui sous-tend tout le design orienté objet.  
Nous plongerons plus profondément dans l'histoire de l'Orienté Objet (OO), et 
en déduirons une nouvelle définition sans ambiguïté de l'OO basée sur la 
gestion des dépendances.  
Enfin, nous jetterons un bref coup d'œil aux principes S.O.L.I.D. qui seront 
bien plus développés dans de prochains articles.
