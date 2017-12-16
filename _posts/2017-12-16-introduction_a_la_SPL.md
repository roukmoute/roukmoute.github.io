---
layout:     post
title:      Introduction à la SPL
date:       2017-12-16
summary:    Les structures de données de la bibliothèque PHP standard
categories: php spl
---

### Introduction

La plupart du temps, le développement en PHP consiste à récupérer et traiter 
des données d’une source ou d’une autre, comme une base de données, des 
fichiers locaux, une API distante, etc. En tant que tels, les développeurs 
passent beaucoup de temps à obtenir, organiser, déplacer et manipuler ces 
données.  
Dans certains cas, un tableau ne suffira pas à réduire l’utilisation et les 
performances de la mémoire et donc de meilleures structures de données sont 
nécessaires.  
Aussi, avec tant de discussion et de concentration sur les frameworks 
(cette page pourrait être remplie avec des noms de frameworks PHP !), vous ne 
pouvez pas connaitre parfaitement tous les frameworks.  
Ils se développent et changent à une vitesse folle.  
Il existe beaucoup de frameworks, même si actuellement seuls quelques un ont 
réussi à se démarquer comme Symfony, Laravel ou encore Zend.  
Aussi, si vous n’en aviez jamais utilisé, vous n’allez pas pouvoir sortir du 
lot rapidement dans ce domaine.

Un secteur sur lequel il faut se concentrer, et où vous êtes raisonnablement 
sûr qu’un expert PHP aura la familiarité, est dans la manipulation et la 
composition générale de la bibliothèque standard PHP (SPL).  
Si vous avez une solide formation dans cette discipline, vos chances de succès 
pour avoir un travail seront bien plus grandes.  
Et vous pourrez vous adapter et comprendre bien plus vite les frameworks 
actuels, qui utilisent énormément la SPL dans leur cœur.  
Plus précisément, vous devriez être familier avec une partie ou l’ensemble 
des neuf structures de données SPL énumérées dans le Manuel PHP.  
Beaucoup offrent des possibilités très similaires les unes aux autres, mais les 
légères variations rendent chacune d’entre elles plus parfaitement adaptée à un 
usage particulier.  
Nous étudierons toute la SPL de long en large, les neuf structurent des 
données, les itérateurs, etc.  
Cependant, l’un des gros problèmes de la SPL est sa documentation qui n’incite 
pas à l’utiliser tellement elle est austère et en manque d’exemples.  
Après avoir lu cette partie, vous serez prêt pour manipuler les interfaces SPL, 
les neuf structures de données et bien sûr les itérateurs.

### Que propose la SPL ?

Nous allons maintenant voir ce que propose la SPL pour les structures de 
données.  
Il en existe neuf, que nous analyserons tout au long des prochains articles.

Mais qu’apportent-elles de nouveau par rapport à nos tableaux ?

Et bien dans l’absolu… rien.
Oui oui, vous avez bien lu, vous pouvez faire exactement la même chose avec de 
simples tableaux.  
En revanche si elles sont là, ce n’est pas non plus pour faire de la 
décoration, leur utilité va se trouver au niveau des ressources dans votre 
application.

### Mais au fait, qu’est-ce qu’une structure de données ?

Avant tout, une structure de données est un moyen de stocker et d’organiser les 
données, qu’on appelle élément, dans la mémoire afin qu’elles puissent être 
utilisées avantageusement.  
L’efficacité signifie qu’ils peuvent être rapides à récupérer ou encore à 
mettre à jour ou qu’ils peuvent être puissants en ce qui concerne l’utilisation 
de la mémoire.

Un tableau par exemple est quelque chose de très manipulable, mais pas 
forcément l’élément le plus léger pour accéder où écrire des données.

C’est là où ces structures rentrent en jeu.

Certaines vont être capables d’aller vite en lecture, d’autres bien plus 
rapides en écriture, d’autres seront aptes de se maintenir à un certain seuil en 
mémoire et d’autre encore seront rapide en écriture et lecture, mais au prix 
d’un plus gros tampon nécessaire.

Apprenez à les manipuler et les performances de votre application iront bien 
mieux qu’avec de simples tableaux.

Toutes les structures implémentent au minimum `Iterator` et `Countable`.
Ce qui veut dire que l’on peut donc toutes les compter (via un modeste 
`count()`) ou bien les parcourir (en utilisant `foreach()`), exactement comme 
array.

Alors à très vite pour voir ensemble `SplDoublyLinkedList` !
