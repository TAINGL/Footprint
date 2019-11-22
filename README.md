<!-- Développement d'une application sur l'empreinte carbone en Flask -->
# Développement d'une application sur l'empreinte carbone en Flask
Le but de ce projet est dans un premier temps d’apporter une vision plus clair d’un état des lieu sur l’empreinte carbone de la France et de son positionnement par rapport au monde. Et dans une seconde partie de projeter l’évolution idéale pour répondre à la solution choisie qui est d’atteindre la neutralité carbone d’ici 2050 pour répondre à ce besoin urgent sur le réchauffement climatique.

## Table of Contents

* [Présentation du sujet](#présentation-du-sujet)
  * [L'empreinte carbone](#l-empreinte-carbone)
  * [GES](#GES)
* [Présentation du projet](#présentation-du-projet)
  * [1 - Le contexte](#contexte)
  * [2 - Les objectifs](#objectifs)
  * [3 - Les contraintes](#contraintes)
* [Modèle conceptuel des données](#MCD)
* [Modèle organisationnel des données](#MOD)
* [Import des données](#import)
* [Requêtes](#requetes)
* [Interface](#interface)
* [Conclusion](#conclusion)
* [Aide Mémoire](#memo)


<!-- Présentation du sujet: -->
## Présentation du sujet:

### L'empreinte carbone:
- Définition :
L’empreinte carbone évalue les émissions de gaz à effet de serre (GES) induites par la consommation de la population résidant sur notre sol.
A la différence des émissions produites sur le territoire, elle inclut les émissions de GES associées aux biens et services importés, et exclut celles associées aux biens et services exportés.

- Pourquoi cet indicateur ?
En tenant compte du contenu en GES des importations, l’empreinte carbone permet d’apprécier les pressions sur le climat de la demande intérieure française, quelle que soit l’origine géographique des produits consommés. Élargir le suivi des émissions de GES au contenu des échanges extérieurs est la seule manière d’apprécier l’impact global de la consommation d’un pays sur le climat. 

### GES:
Les principaux GES sont :
•	La vapeur d'eau (H2O)
•	Le dioxyde de carbone (CO2)
•	Le méthane (CH4)
•	Le protoxyde d'azote (N2O)
•	L'ozone (O3)
•	Des gaz fluorés (CFC, HCFC, PFC, HFC, SF6, NF3)

On parlera de GES anthropiques pour les GES dont l'émission est influencée par les activités humaines.


<!-- Présentation du projet: -->
## Présentation du projet:

L'objectif du projet est d'avoir une vision globale sur l’empreinte carbone de la France et de son positionnement par rapport au monde afin de connaitre les axes d'amélioration prioritaire à mettre en place.

Le projet se découpe en deux parties:

- Avoir une fiche bilan pour la France:
    * Consommation de GES dans le temps et par secteur
    * Position de la France vis à vis des autres

- Avoir la projection de l’évolution jusqu’à 2050 : solution apportée


<!-- Cahier des charges -->
## Cahier des charges

### 1 - Le contexte

- Enjeux: Avoir une meilleure compréhension sur l’état actuel et l’évolution sur l’empreinte carbone d’hier à aujourd’hui

- Stratégies : 
    * Centraliser les informations pour faciliter les recherches et l’enregistrement des nouvelles données (Historique de la consommation des différents GES de chaque pays de 1960 à 2019).
    * Différentier les différents secteurs des GES dégagés pour connaître les secteurs les plus consommateurs afin de faciliter la prise de décision.

- Domaine d’application : La France vs Monde


### 2 - Les objectifs

Le but est de pouvoir répondre aux questions suivantes:
* Votre pays est-il débiteur ou créancier écologique? 
* Quels pays ont les plus grands déficits ou réserves écologiques?
* Quand le budget écologique de votre pays est-il passé au rouge? 
* Quels pays se classent au premier rang en termes d'empreintes écologiques et de biocapacités totales? 


### 3 - Les contraintes

1. Le délais Premier projet d'envergure il est difficile d'estimer le temps pour chacune des tâches et d'anticiper les actions.
2. La compréhension des données dû à la complexité du sujet abordée. 
3. L'étendu du projet beaucoup de chose est possible d'entreprendre sur ce projet la difficulté sera de se tenir à des éléments réalisable dans le temps imparti.


<!-- Modèle conceptuel des données -->
## Modèle conceptuel des données

Le MCD est une représentation graphique de haut niveau qui permet facilement de comprendre comment les différents éléments sont liés entre eux à l’aide de diagrammes codifiés dont les éléments suivants font partie :

    Les entités (1 rectangle = 1 objet) ;
    Les propriétés (la liste des données de l’entité) ;
    Les relations qui expliquent et précisent comment les entités sont reliées entre elles ;
    Les cardinalités (les petits chiffres ou icône au niveau des « pattes »).

MCD réaliser avec MySQL Workbench

<!-- Modèle organisationnel des données -->
## Modèle organisationnel des données

```sh
A compléter
```


### Import des données

Les données proviennent de kaggle. Il y a un travail de nettoyage fait au préalable pour l'exploitation des données.
* [Kaggle: 2016 Global Ecological Footprint (GEF)](https://www.kaggle.com/footprintnetwork/ecological-footprint)
* [Kaggle: National Footprint Accounts 2018 (NFA)](https://www.kaggle.com/footprintnetwork/national-footprint-accounts-2018)

### Requêtes

```sh
A compléter
```

### Interface

```sh
"Réalisation d'une maquette à définir"
```
L'idée est de créer une application Flask, nous auront un système de recherche (sur les différents paramètres permettant de calculer l'empreinte carbone). Le but est de pouvoir visualiser à plusieurs degrés ou sur une évolution temporelle à l'aide d'une carte intéractive.


### Conclusion

```sh
A compléter
```

### Aide mémoire

```sh
A compléter
```



