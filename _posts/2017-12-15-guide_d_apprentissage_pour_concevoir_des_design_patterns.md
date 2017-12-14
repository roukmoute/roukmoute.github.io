---
layout:     post
title:      Guide d'apprentissage pour concevoir des Design Patterns
date:       2017-12-15
summary:    Concepts essentiels et terminologie
categories: design_patterns
---

### Présentation des Patterns

Les Patterns pour le développement sont l'un des thèmes les plus vieux qui 
existent au sein de la communauté orientée objet.  
L'emploi actuel du terme "Pattern" est dérivé des écrits de l'architecte 
Christopher Alexander qui a rédigé plusieurs ouvrages sur le sujet de 
l'urbanisme et de l'architecture du bâtiment.  
Il ne s'agit ni plus ni moins que de la documentation des meilleures pratiques.

### Un vocabulaire commun pour les gouverner tous !

C'est en apprenant et comprenant les Design Pattern que les développeurs 
peuvent correctement s'entendre !  
Ces Patterns ont été créés pour aider les concepteurs de logiciels à résoudre 
les problèmes récurrents rencontrés tout au long du développement.  
Les modèles sont utiles pour créer un langage commun pour communiquer des idées 
et des expériences sur ces problèmes et leurs solutions.  
Si tout le monde les connait, on peut donc raisonner bien plus facilement et
intelligemment aux sujets à résoudre.

### Un guide ?

Quand je parle de Design Pattern autour de moi, on arrive très vite au livre de 
référence "Design Patterns: Elements of Reusable Objet-Oriented Software" du 
Gang of Four.  
On l'a tous déjà entendu au moins une fois, mais :
- L'avons-nous lu en entier ?
- L'avons-nous bien compris ?
- Ne devrions-nous pas dire que nous l'avons "étudié" plutôt que "lu" ?

Ainsi ce guide, qui sera écrit dans le temps, va permettre d'apprendre et 
d'utiliser des Design Patterns, que simplement les avoir "lut".  
Et quand moi il me légitimera d'en apprendre davantage au moment de leurs 
rédactions !  
Je ne compte pas respecter le même ordre que le livre du GoF.  
Les Designs Patterns sont divisés en trois catégories :
- créatifs (création d'objets d'une manière adaptée à la situation)
- structurels (facilitent la conception en identifiant une façon simple de 
réaliser des relations entre les entités)
- comportementaux (identifient les patrons de communication communs entre les 
objets)

Les Patterns sont dangereux, dans le sens où après avoir appris plusieurs
Patterns, nous allons vouloir les utiliser à tout bout de champ, sans avoir
pris le temps de le tester auparavant.  
Il y a bonne phrase de [Gerald Croes](http://www.croes.org) qui [dit](http://www.croes.org/gerald/blog/nutilisez-pas-les-design-patterns-en-php/109/) :  
"N’utilisez jamais les Modèles de Conception, mais connaissez-les, 
maîtrisez-les !"  
Ce qui n'est pas totalement vrai et pas totalement faux.  
Est-ce qu'il faut utiliser les Design Pattern ?  
Oui, mais avant il faut les maîtriser.  
Le problème étant que, jeunes fougueux que nous sommes, nous venons d'apprendre 
un Pattern et du coup on cherche à l'implémenter à tout prix.  
C'est absolument tout ce qu'il ne faut pas faire !
  
![Au bucher !](https://i.imgur.com/dCerM7S.gif)

En les maîtrisant, vous aurez déjà vous-même votre opinion si vous aimez tel ou 
tel Pattern.  
Chacun à ses idées sur chaque Pattern, vous en détesterez comme vous en aimerez.

Les Patterns, en général, sont rarement utilisés isolément.  
Le Pattern Iterator a souvent recours au Pattern Composite, les Patterns 
Observer et Mediator forment un lien classique, et ainsi de suite.  
Lorsque vous commencez à concevoir et programmer des Design Pattern, vous 
découvrez rapidement que le véritable art d'utiliser des Patterns est de savoir 
comment les combiner.

Pour apprendre à les maîtriser et pouvoir voir les relations entre eux, il est 
donc utile d'en assimiler certains avant d'autres.  
Et certains modèles sont un peu plus complexes que d'autres.  
Cela vous permettra de passer intelligemment d'un Pattern à l'autre dans le but 
de les maîtriser.

D'ailleurs le premier article que j'écrirai sera sur la "Factory Method"
(Méthode d'usine).

### Un peu de lecture en plus ?

Vous voulez en apprendre davantage sur l'histoire des Designs Patterns  :
- [http://www.bradapp.com/docs/Patterns-intro.html](http://www.bradapp.com/docs/Patterns-intro.html)
- [http://dirkriehle.com/computer-science/research/1996/tapos-1996-survey.pdf](http://dirkriehle.com/computer-science/research/1996/tapos-1996-survey.pdf)
