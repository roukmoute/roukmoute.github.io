---
layout:     post
title:      Factory Method — Les Fondements
date:       2017-12-30
summary:    Ce Pattern est utilisé dans toute la littérature sur les Patterns.
categories: design_patterns
---

### Définition du GoF

Définir une interface pour créer un objet, mais laisser les sous-classes 
décider de la classe à instancier.
Factory Method permet à une classe de différer l’instanciation à des 
sous-classes.

Bon pour la définition, c’est fait.

### L’essence de la Factory Method

Comprenons le schéma de la Factory Method (Méthode Usine) en regardant 
quelques classes de vignobles, parce que comprendre avec du bon vin, c’est tout 
aussi bien.  
Nous allons commencer avec notre classe simple ici appelée `GrapeVariety` 
(la traduction du mot cépage) et il a une méthode appelée `produceWine()`, qui 
retourne un vin "standard".  
Ensuite, nous avons un `Riesling` qui a sa propre méthode `produceWine()`.  
Ce cépage produit uniquement… du Riesling.  
Donc cette classe passe outre la méthode `produceWine()` de la classe parent 
pour retourner un vin blanc.  

Il passe outre `produceWine()` et à ce stade, nous pourrions déjà dire que 
`produceWine()` est une Factory Method :  

- Il existe dans la classe parente qui retourne un cépage par défaut.
- Et il existe dans la sous-classe qui l’emporte sur la classe parent.

Voici une autre sous-classe de `GrapeVariety`; `AlsaceGrapeVarieties`.  
`AlsaceGrapeVarieties` produit plusieurs sortes de cépages alsaciens différents.  
Donc il produit la méthode `produceWine()` qui peut retourner soit un 
`Sylvaner`, un `Gewurtztraminer` ou n’importe quel type de vin alsacien.  
Ainsi, selon votre préférence, vous pouvez obtenir l’un ou l’autre.  
Mais ce qu’il faut retenir c’est que la classe `AlsaceGrapeVarieties` peut 
produire différentes sortes de cépages.
Ce sont tous des cépages !  
C’est important parce que le type de retour de `produceWine()` est un vin.  

Et que chaque vin qui est renvoyé via la Factory Method à partir de la méthode 
`produceWine()` doit obéir à ce contrat.  
Et ce doit être une sous-classe du cépage "standard" ou implémenter une 
interface du cépage.  
C’est donc un modèle de la Factory Method.  
C’est une méthode qui fait de la création.  
Elle existe dans une hiérarchie.  
Dans le code une hiérarchie est pyramidale, tout en haut, nous avons le plus 
abstrait, donc une interface ou une classe abstraite par exemple, puis on 
descend jusqu’au plus concret.  
Plus on descend dans les niveaux, plus la classe est plus précise que son 
précédent.  
C’est soit abstrait, soit une interface.  
Ainsi, `produceWine()` n’a pas besoin de renvoyer une valeur par défaut, cela 
pourrait simplement être un commandement pour les sous-classes de déclarer et 
d’implémenter une méthode `produceWine()`.  
Et c’est tout.  
Nous avons donc une création [polymorphe](/programmation/2017/12/23/polymorphisme/) 
de cépages et ceci est une Factory Method.

Le concept de hiérarchie et de polymorphisme est important !  
C’est, en effet, ce qui permettra de faire la distinction avec le Design 
Pattern Template Method.  
Nous verrons ce Pattern plus tard, il est inutile pour la suite de cet article.

### Les variations

Ce pattern peut être fait de plusieurs manières.  
Nous allons voir 3 implémentations de possibles, histoire de bien faire le tour.

#### Les participants

Je vais utiliser le même concept fourni que dans le GoF pour ce qui est des 
"participants".

Les participants ce sont les classes et/ou les objets participant au Design 
Pattern et leurs responsabilités.

- `Consommateur` — L’objet qui veut créer un nouveau `Produit`.
- `Produit` — L’objet qui est créé et livré au `Consommateur`.
- `Producer` — L’objet qui fabrique le `Produit`. Cet objet peut être une 
interface ou une classe abstraite au sein d’une hiérarchie.
- `Factory Method` — La méthode [polymorphe](/programmation/2017/12/23/polymorphisme/) 
dans une hiérarchie de classe qui retourne le `Produit`.

#### Implémentation par défaut

![Implémentation par défaut](/images/factory_method_les_fondements/default_implementation.svg)

Sur ce schéma, l’implémentation par défaut est avec une classe `Creator` qui 
fournit une implémentation par défaut (`ConcreteProduct`) pour la Factory 
Method, tandis que `ConcreteCreator` remplace l’implémentation 
(`AnotherConcreteProduct`) par défaut.

#### Lorsque la Factory Method est abstraite

![la Factory Method est abstraite](/images/factory_method_les_fondements/factory_method_is_abstract.svg)

Ici très peu de changement par rapport au schéma précédent.  
La Factory Method est déclarée comme abstraite dans `Creator` et `Produit` est 
abstrait.  
Ceci permet à la méthode `AnOperation()` de fournir une instanciation 
[polymorphe](/programmation/2017/12/23/polymorphisme/) du produit.  
__Il ne faut pas confondre cela avec l'Abstract Factory.__

#### Factory Method paramétrée

{% highlight php %}
class Database
{
    public function create(string $database): \PDO
    {
        if ($database === 'mysql') {
            return new DatabaseMySql();
        }

        if ($database === 'pgsql') {
            return new DatabasePostgreSQL();
        }
    }
}

class CommercialDatabase extends Database
{
    public function create(string $database): \PDO
    {
        if ($database === 'microsoft') {
            return new SQLServer();
        }

        if ($database === 'oracle') {
            return new Database12c();
        }

        return parent::create($database);
    }
}
{% endhighlight %}

Dans ce cas, la Factory Method prend un paramètre qui l’aide à sélectionner 
la `Base de données` obtenue.  
Ce dernier cas est un des plus connu et utilisé.  
Si le paramètre passé à la Factory Method n’aide pas à la sélection de la 
`Base de données`, elle ne serait techniquement pas appelée 
"Factory Method paramétrée".

### Résumé

Voici donc un petit résumé pour remettre tout dans le bon ordre histoire 
d’avoir bien compris ce Pattern.

Une Factory Method est, par définition, [polymorphe](/programmation/2017/12/23/polymorphisme/).  
Si elle n’était pas [polymorphe](/programmation/2017/12/23/polymorphisme/), nous l’appellerions probablement 
`Creation Method` (encore une fois c’est un Pattern que nous verrons plus tard).

Comme nous avons pu le voir avec l’implémentation par défaut, il n’est pas 
nécessaire d’utiliser une méthode abstraite pour implémenter une Factory Method.  
Bien que la hiérarchie soit une caractéristique de la Factory Method, il est 
possible de fournir un `Produit` par défaut, épargnant ainsi aux sous-classes 
qui n’ont pas besoin de passer outre à la nécessité de spécifier l’une des leurs.

Une Factory Method peut créer un seul objet et même un agrégat d’objets.  
Tandis qu’une Factory Method renvoie un seul objet, cet objet peut contenir des 
objets supplémentaires accessibles à travers les champs de la nouvelle 
instance.  
En effet, le `Produit` peut être un agrégat élaboré, comme un arbre ou une 
collection.

Si une Factory Method prend un paramètre, c’est n’est PAS par définition une 
"Factory Method paramétrée".  
N’importe quelle Factory Method peut prendre des paramètres qui remplissent le 
même rôle que ceux d’un constructeur, c’est-à-dire aider à décider comment 
remplir les champs de la nouvelle instance.  
Ce n’est que dans les cas où le paramètre est utilisé pour déterminer le type 
réel du `Produit` retourné que nous nous référons à la Factory Method comme 
étant une "Factory Method paramétrée".

Une fois qu'une méthode devient statique, elle ne peut pas être une Factory 
Method puisque les Factory Methods sont implémentées en utilisant l'héritage 
et que vous n'obtenez pas d'héritage avec les méthodes statiques.

### Comment la Factory Method favorise-t-elle un code à couplage faible ?

Une Factory Method peut reporter la création de l'objet à une sous-classe, ce 
qui permet un couplage faible, aucune statique ne doit rentrer en jeu, sinon 
cela s'appelle une Creation Method.  
Une Factory Method ne permet pas au consommateur de créer une "famille de 
produits".  
Il s'agit de l'`Abstract Factory Pattern`.  
La plupart des implémentations de la méthode Factory Method ont tendance à 
fonctionner avec un seul produit (pas avec une famille de produits), et 
que ce seul produit a souvent plusieurs implémentations concrètes.  
Le code client qui appelle la Factory Method est faiblement couplé au code qui 
crée et retourne un objet, parce que le client n'a pas besoin de se soucier de 
quelle sous-classe est appelée.

### Conclusion

Bon… Pour la théorie, c’est maintenant fini :)  
Je suis bien plus pour la pratique, mais je pense qu’un petit peu de théorie 
est tout de même important pour mieux comprendre ce que l’on va faire par la 
suite.  
Pour ce qui est de la pratique, cela se fera en plusieurs articles, chaque 
article étant un cas concret.  
Non pas qu’il soit difficile, comme vous venez de le voir, mais je pense que 
plus il y a d’exemples disponibles, mieux c’est.

À l’année prochaine !
