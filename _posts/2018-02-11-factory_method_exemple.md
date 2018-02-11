---
layout:     post
title:      Factory Method — Exemple de code
date:       2018-02-11
summary:    Cet exemple reprend celui fourni dans le livre du GoF
categories: design_pattern php
---

Voici la suite de [cet article](/design_patterns/2017/12/30/factory_method_les_fondements/).

[L'exemple suivant](https://github.com/roukmoute/design-patterns/tree/master/Creational/FactoryMethod/Gof) 
enseigne le modèle de la Factory Method telle qu'elle est expliquée dans le Gof.

Cet exemple montre comment une pseudo-suite d'applications de bureautique peut 
partager du code et reporter les décisions de création à des sous-classes.

Parmi les [Applications](https://github.com/roukmoute/design-patterns/blob/master/Creational/FactoryMethod/Gof/Application.php) 
de cette suite il y a :

- [SpreedSheetApplication](https://github.com/roukmoute/design-patterns/blob/master/Creational/FactoryMethod/Gof/SpreadsheetApplication.php)
- [EditorApplication](https://github.com/roukmoute/design-patterns/blob/master/Creational/FactoryMethod/Gof/EditorApplication.php)

Naturellement pour chaque application de la suite, il y a un type de [Document](https://github.com/roukmoute/design-patterns/blob/master/Creational/FactoryMethod/Gof/Document.php) 
correspondant :

- [SpreasheetDocument](https://github.com/roukmoute/design-patterns/blob/master/Creational/FactoryMethod/Gof/SpreadsheetDocument.php)
- [EditorDocument](https://github.com/roukmoute/design-patterns/blob/master/Creational/FactoryMethod/Gof/EditorDocument.php)

la hiérarchie de l'application ressemble à ceci :
![application_hierarchy](https://user-images.githubusercontent.com/2140469/36077136-096a05a4-0f67-11e8-8f1c-26ea90759224.png)

Nous avons notre application générique abstraite ainsi que les sous-classes 
`EditorApplication` et `SpreadsheetApplication`.

En effet il peut arriver d'avoir beaucoup de code en commun.  
Du coup l'utilisation d'une classe parente prend tout son sens.  
Pour rappel, cette classe peut être abstraite ou non si un comportement par 
défaut est mis en place.  
Ainsi on ne laisse que les méthodes qui se distinguent dans les sous-classes.

Mais comment s'assurer que pour chaque sous-classe d'application, le type de 
`Document` est correctement est créé ?

Voici comment faire :  
Dans la classe `Application`, on définit une [méthode abstraite](https://github.com/roukmoute/design-patterns/blob/master/Creational/FactoryMethod/Gof/Application.php#L18), 
`createDocument()`, qui est chargée de s'assurer que les sous-classes créées, 
ont le bon type de `Document` lorsqu'ils implémentent leur copie de 
`createDocument()`.

Par exemple, dans `EditorApplication`, l'implémentation de `createDocument()` 
renvoie un nouveau document `EditorDocument`.  
De même, l'implémentation de `createDocument()` par `SpreadsheetApplication` 
renverra un `SpreadsheetDocument`.

En appliquant la puissance du [polymorphisme](/programmation/2017/12/23/polymorphisme/), 
nous avons veillé à ce que chaque sous-classe d'application renvoie 
correctement la sous-classe `Document` correspondante.
