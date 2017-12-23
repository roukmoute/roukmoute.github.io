---
layout:     post
title:      Le polymorphisme
date:       2017-12-23
summary:    Un peu d'explication
categories: programmation
---

Le polymorphisme est beaucoup utilisé dans le langage informatique.
Ce n'est pas bien compliqué à comprendre, mais souvent je trouve que cela peut 
[partir bien loin](https://fr.wikipedia.org/wiki/Polymorphisme_(informatique)).

Voici donc un petit article qui, je l'espère, vous permettra de comprendre ce 
mot.

Le polymorphisme pourrait avoir comme définition "une interface unique et un 
fonctionnement multiple".  
Par exemple: `x` est une personne et chaque personne travaille différemment 
donc `x` est une interface unique et son fonctionnement est multiple.

La beauté du polymorphisme est que le code qui fonctionne avec les différentes 
classes n'a pas besoin de savoir quelle classe il utilise puisqu'elles sont 
toutes utilisées de la même façon.

<blockquote>
  <p>
    Une analogie du monde réel pour le polymorphisme est un bouton.  
    Tout le monde sait comment utiliser un bouton: il suffit d'appuyer dessus.  
    Ce qu'un bouton "fait", cependant, dépend de ce à quoi il est connecté et 
    du contexte dans lequel il est utilisé — mais le résultat n'affecte pas la 
    façon dont il est utilisé.  
    Si votre patron vous dit d'appuyer sur un bouton, vous disposez déjà de 
    toutes les informations nécessaires pour effectuer la tâche.
  </p>
  <p>    
    Dans le monde de la programmation, le polymorphisme est utilisé pour rendre 
    les applications plus modulaires et extensibles.  
    Au lieu d'écrire plein de conditions décrivant une nouvelle action, vous 
    créez des objets interchangeables que vous sélectionnez en fonction de vos 
    besoins.  
    C'est l'objectif fondamental du polymorphisme.
  </p>
  <footer><cite title="Steve Guidetti">Steve Guidetti</cite></footer>
</blockquote>

Exemple simple avec la méthode `__toString` qui affiche toutes les données 
actuellement stockées dans l'instance `Aircraft` :

{% highlight php %}
class Aircraft
{
    /**
     * @var string
     */
    private $aircraftType;
    /**
     * @var string
     */
    private $departureCity;
    /**
     * @var string
     */
    private $arrivalCity;

    public function __construct(
        string $aircraftType,
        string $departureCity,
        string $arrivalCity
    ) {
        $this->aircraftType = $aircraftType;
        $this->departureCity = $departureCity;
        $this->arrivalCity = $arrivalCity;
    }

    public function __toString(): string
    {
        return sprintf(
            "Bienvenue à bord de notre %s.\n" .
            "Ce vol est en décollage imminent de %s et aura pour arrivée %s.\n" .
            "Merci, à très bientôt !",
            $this->aircraftType(),
            $this->departureCity(),
            $this->arrivalCity()
        );
    }

    public function aircraftType(): string
    {
        return $this->aircraftType;
    }

    public function departureCity(): string
    {
        return $this->departureCity;
    }

    public function arrivalCity(): string
    {
        return $this->arrivalCity;
    }
}
{% endhighlight %}
[L'exemple à tester en ligne](https://3v4l.org/FpTpB)

Pour démontrer les caractéristiques polymorphes dans le langage PHP, on va 
étendre notre classe `Aircraft` avec une classe `PrivateJet` et une classe 
`LowCostAircraft`.  
Pour le `PrivateJet`, on va ajouter un champ supplémentaire appelé 
`airportDestination`, qui est une chaine de caractère qui indique… le nom de 
l'aéroport de notre destination.

Voici donc notre nouvelle classe :

{% highlight php %}
class PrivateJet extends Aircraft
{
    private $arrivalCity;
    /**
     * @var string
     */
    private $airportDestination;

    public function __construct(
        string $aircraftType,
        string $departureCity,
        string $arrivalCity,
        string $airportDestination
    ) {
        parent::__construct($aircraftType, $departureCity, $arrivalCity);

        $this->airportDestination = $airportDestination;
    }

    public function __toString(): string
    {
        return sprintf(
            "%s\n" .
            "Notre arrivé se fera à l'aéroport %s.",
            parent::__toString(),
            $this->airportDestination()
        );
    }

    public function airportDestination(): string
    {
        return $this->airportDestination;
    }
}
{% endhighlight %}
[L'exemple à tester en ligne](https://3v4l.org/eA0Zt)

Notez que nous avons surchargé sur la méthode `__toString`.  
Outre les informations fournies précédemment, la donnée supplémentaire sur le 
nom de l'aéroport d'arrivée est incluse dans la sortie.

Le polymorphisme offre de nombreux avantages.  
Le gain le plus important se produit lorsque le même ensemble de conditions 
apparaît à plusieurs endroits du programme.  
Si vous voulez ajouter un nouveau type, vous devez trouver et mettre à jour 
toutes les conditions.  
Mais avec les sous-classes, il vous suffit de créer une nouvelle sous-classe et 
de fournir les méthodes appropriées.

Nous pouvons aussi modifier une autre méthode disponible :

{% highlight php %}
class LowCostAircraft extends Aircraft
{
    public function __construct(
        string $aircraftType,
        string $departureCity,
        string $arrivalCity
    ) {
        parent::__construct($aircraftType, $departureCity, $arrivalCity);
    }

    public function arrivalCity(): string
    {
        return sprintf("%s.\nLe moteur est le coeur d'un avion, mais le pilote est son âme", parent::arrivalCity());
    }
}
{% endhighlight %}
[L'exemple à tester en ligne](https://3v4l.org/ECneC)

Pour résumer, nous avons trois classes. Chaque sous-classe surcharge une 
méthode pour afficher finalement une information unique.

### Mais en fait, c’est juste une classe abstraite ?

C'est un peu plus que ça.    
Je dirai plus qu’il s’agit d’une implémentation, donc cela peut-être une classe 
abstraite ou une interface.

Les autres méthodes qui vont vouloir utiliser votre interface/abstraction n'ont 
pas besoin de connaître les sous-classes, ce qui réduit les dépendances dans 
votre système et facilite la mise à jour.

La définition du polymorphisme dans le dictionnaire renvoie à un principe de la 
biologie selon lequel un organisme ou une espèce peut avoir plusieurs formes ou 
stades différents.  
Ce principe peut également s’applique aussi à la programmation orientée objet 
et aux langages comme le langage PHP.  
Les sous-classes d’une classe peuvent définir leurs propres comportements 
uniques tout en partageant certaines fonctionnalités de la classe parente.

Le polymorphisme décrit un modèle de programmation orientée objet dans lequel 
les classes ont des fonctionnalités différentes tout en partageant une 
interface commune.

Voilà pour ce court article :)

Bonnes fêtes de Noël !
