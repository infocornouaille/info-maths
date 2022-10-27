---
title: Bases de données et SQL
description: Bases de données et SQL en spécialité NSI
---

# Bases de données et SQL

## Aspect historique

!!!info "Histoire des bases de donnée"

	- En 1970, **Edgar Codd** invente le _modèle relationnel_ pour les bases de données.
	-  En 1973, première version du langage **SQL** (**S**tructured **Q**uery **L**anguage). C'est un langage de requêtes permettant d'interagir avec une base de données.
	- En 1979, apparition du premier **S**ystème de **G**estion de **B**ase de **D**onnées (**sgbd**) : Oracle qui fera la fortune de ses trois fondateurs (L. Ellison, E. Oats et B. Miner).
	- En 1995 (et 1996), première version d'importants **sgbd** libres}MySQL (et PostGreSQL).
	- En 2020, Le volume mondial de données stockées est estimé à 47 milliards de téra-octets ($47 \times 10^{21}$ octets) et a été multiplié par 20 en 10 ans.



## Outils traditionnels

!!!tip "Apport des bases de données"

	Les bases de données corrigent de nombreux défauts des outils traditionnels de gestion des données. En effet :
	
	- Les accès simultanés par plusieurs programmes aux mêmes données pouvaient générer des conflits.
	- Pour lire (ou modifier) les données il fallait savoir comment elles étaient représentées.
	- Les utilisateurs devaient s'assurer de  l'intégrité des données avant de les stocker. C'est à dire que c'est l'utilisateur qui était chargé du contrôle de la validité de ses données.
		

## Principes

!!!savoir "Principes des bases de données"

		Plusieurs aspects des bases de données viennent corriger les limitations des outils traditionnels :

		- Principe d'**unicité** : un enregistrement doit être unique (une donnée qui apparaît plusieurs fois est dite **redondante**).

		Ici intervient la notion de **clé primaire**, c'est à dire dans une table une identification unique de l'enregistrement.

		- Principe d'**intégrité** : le contrôle de la validité des données est effectué par le **sgbd**.

		Ici intervient la notion de **domaine**, c'est à dire qu'on peut préciser que les valeurs d'un champ doivent être d'un certain types (par exemple entier, flottant, chaine de caractères, ...) et appartenir à un certain ensemble de valeurs  : le domaine.

		- Principe d'**indépendance logique** : les utilisateurs accèdent aux données sans se soucier de la façon dont elles sont représentées ou codées dans la base.
		
!!!example "Exemple"

	Prenons l'exemple suivant :
		
    | Nom      | Prénom | Naissance |
    | -------- | ------ | --------- |
    | Pascal   | Blaise | 1623      |
    | Lovelace | Ada    | 1815      |
    | Boole    | George | 1815      |


		
	-	Il est certes peu probable (mais pas impossible) que deux personnes portant les mêmes noms et prénoms naissent la même année, afin de respecter le **principe d'unicité**, nous devons adjoindre à chaque enregistrement un champ (par exemple `id`) unique qui servira de clé primaire.

	- Les champs  `Nom` et `Prénom` sont au format texte, le champ `Naissance` est un entier.

	- On peut par exemple préciser les contraintes d'intégrité suivantes : `Nom` doit être non vide, `Naissance` doit être supérieur à 0.
		


## Schéma relationnel

!!!savoir "Schéma relationnel"

		Le schéma relationnel d'une base de données présente les tables de cette base sous la forme de liste ou de tableau. 
        
        Dans les deux cas, on précise la clé primaire de la table en **soulignant** l'attribut. 
        
        On indique aussi parfois le type des attributs.

!!!example "Exemple"

	Le schéma relationnel de la table `personne` peut s'écrire sous forme de liste : 
	
    **personnes** (^^`id`^^ : ``int``, ``Nom`` : ``text``, ``Prenom`` : ``text``, ``Naissance`` : ``int``)

	

## Bases de SQL

### SELECT et FROM

!!!tip "SELECT et FROM"

	- Pour récupérer la totalité des champs d'une table `table` on utilise la syntaxe :

    ```sql
    SELECT *
    FROM table;
    ```

	- Pour récupérer simplement les champs `champ1`, `champ2`, ... on utilise :

    ```sql
    SELECT champ1, champ2
    FROM table;
    ```
			      
                  
!!!example "Exemple"

    ```sql
    SELECT Nom, Naissance
    FROM personne;
    ```

    | Nom      | Naissance |
    | -------- | --------- |
    | Pascal   | 1623      |
    | Lovelace | 1815      |
    | Boole    | 1815      |
		

### WHERE

!!!tip "Clause WHERE"

		Une instruction `#!sql SELECT` peut être suivie d'une clause `#!sql WHERE` qui permet de rechercher les enregistrements correspondants à certains conditions. Ces conditions s'expriment à l'aide des opérateurs suivant :

		- Comparaison : `=`, `<`, `>`, `<=`, `>=`,  `<>` (différent)  et `#!sql BETWEEN` (entre)
		
        - Logique : `#!sql AND`, `#!sql OR` et `#!sql NOT`
		
        - Modèle de chaines de caractères : `#!sql LIKE` où `#!sql %` désigne n'importe quel suite de caractères et `#!sql _` un unique caractère.
		

!!!example "Exemples"

	Pour chercher dans la table les personnes nées après 1789 :

    ```sql
    SELECT *
    FROM personne
    WHERE naissance > 1789;
	```
		
    Pour chercher dans la table les personnes dont la deuxième lettre du nom est un e :

    ```sql
    SELECT *
    FROM personne
    WHERE nom LIKE "_e%";
    ```



### Classement des résultats

!!!tip "Clause ORDER BY"

	Une instruction `#!sql SELECT` peut être suivie d'une clause `#!sql ORDER BY` qui permet de classer les enregistrements selon un ou plusieurs champs. 
    
    Cette clause est elle même suivie de :
	
    - `#!sql ASC` pour indiquer un classement par ordre croissant
	
    - `#!sql DESC` pour indiquer un classement par ordre décroissant

    La valeur par défaut est `#!sql ASC`


!!!example "Exemple"
	
     Pour classer par ordre alphabétique nom puis prénom notre table exemple :

     ```sql
     SELECT *
     FROM personne
     ORDER BY Nom, Prenom ASC;
     ```
			      

### Clauses DISTINCT et LIMIT

!!!tip "Clauses DISCTINCT et LIMIT"

	- Une instruction `#!sql SELECT` peut être **directement** suivie d'une clause `#!sql DISTINCT champ`  qui indique que `champ` ne doit apparaître qu'une fois dans les résultats
	
    - Une instruction `#!sql SELECT` peut être suivie d'une clause `#!sql LIMIT` qui indique le nombre maximal d'enregistrement à renvoyer. Cette clause est particulièrement utile en relation avec `#!sql ORDER BY`.
		

!!!example "Exemples"

	- Pour afficher les années de naissance sans répétitions :

    ```sql
    SELECT DISTINCT naissance
    FROM personne;
    ```

	- Pour afficher les trois plus jeunes personnes de la table :

    ```sql
    SELECT *
    FROM personne
    ORDER BY naissance DESC
    LIMIT 3;
    ```


### Agrégation

!!!tip "Agrégation"

	Le langage **SQL** offre des opérateurs appelés `fonction d'agrégation` permettant de calculer une valeur à partir d'un ensemble d'enregistrement :

	- `#!sql MIN`pour obtenir le minimum (d'un champ sur un ensemble d'enregistrement)

	- `#!sql MAX`pour obtenir le maximum
  
	- `#!sql SUM`pour obtenir la somme

    - `#!sql AVG` pour obtenir la moyenne

    - `#!sql COUNT` our compter le nombre d'enregistrements
			
            
!!!example "Exemple"

     Pour avoir la personne la plus âgée présente dans la table :

    ```sql
    SELECT MIN(naissance), nom, prenom
    FROM personne;
	```


