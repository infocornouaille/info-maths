---
title: Listes en Python
description: Cours de spécialité NSI sur les listes en Python
---

# Listes en Python

## Définition des listes en Python

!!! tip "Définition"

     **Tableau**: Un tableau est une collection ordonnée d'éléments de n'importe quel type, organisés séquentiellement les uns à la suite des autres.

!!! info

     En Python, un **tableau** est appelé **liste**. Il est de type `list`

     Le tableau est modifiable par affectation, on dit qu'il est **mutable**

## Bases sur les listes en Python

!!! tip "Création d'une liste"

     Dans une liste, tous les termes doivent être séparés par des virgules et entourés de **crochets**

!!! example "Exemple"

     ```python
     L = [1, 5, 8]
     ```

!!! info

     Une **liste** peut aussi contenir des éléments de types différents

     ```python
     lst = [4, "bonjour", False, [7, 9]]
     ```

!!! tip "liste vide"

     La liste vide est notée `[]`

     ```python
     lst = [] # liste vide
     ```

## Accès aux éléments d'une liste en Python

!!! tip "Accéder aux éléments d'une liste"

     On accède à un élément d'une liste en mettant entre crochets l'indice de l'élémént (qui commence à **zéro**).

!!! example "Exemple"

     ```python
     >>> famille = ["Bart", "Lisa", "Maggie"]
     >>> famille[0]
     'Bart'
     >>> famille[1]
     'Lisa'
     >>> famille[2]
     'Maggie'
     ```

!!! danger

     Un indice qui dépasse la valeur `longueur de la liste -1` provoquera une erreur `list index out of range`.

!!! example "Exemple:"

     ```python
     >>> famille = ["Bart", "Lisa", "Maggie"]
     >>> famille[3] # Erreur de type list index out of range
     IndexError: list index out of range
     ```

!!! tip "Indices négatifs"

     Il est possible d'utiliser des indices **négatifs**.

     $-1$ correspond alors au dernier élément de la liste.

!!! example "Exemple d'utilisation d'indices négatifs"

     ```python
     >>> famille = ["Bart", "Lisa", "Maggie"]
     >>> famille[-1]
     'Maggie'
     >>> famille[-2]
     'Lisa'
     ```

## Modification d'une liste par affectation en Python

!!! tip "Modification d'une liste"

     Les termes d'une listes peuvent être modifiés par affectation au cours d'un programme.

     Cela est possible car les listes sont des objets **mutables**.

!!! example "Exemple de modification par affectation"

     ```python
     >>> animaux = ['renards', 'crocodiles', 'zèbres']
     >>> animaux[1] = 'toucans'
     >>> print(animaux)
     ['renards', 'toucans', 'zèbres']
     ```

## Longueur d'une liste en Python

!!! tip "Longueur d'une liste"

     La longueur d'une liste sera donnée par la fonction `len()`

!!! example "Exemple"

     ```python
     >>> lst = [3, 'bonjour', True, [1, 2, 5]]
     >>> len(lst)
     4
     ```

## Test d'appartenance avec `in` en Python

!!! tip "Tester l'appartenance d'un élément dans une liste"

     On peut tester si un élément appartient à une liste avec `in`

!!! example "Example de test d'appartenance"

     ```python
     >>> lst = ['n', 's', 'i']
     >>> print('n' in lst)
     True
     >>> print('b' in lst)
     False
     ```

## Opération sur les listes en Python

!!! tip "La méthode append()"

     Les listes Python ont la particularité de pouvoir être allongées d'un élément en fin de liste, grâce à la méthode `append()`

!!! example "Example d'utilisation de la méthode append()"

     ```python
     >>> felins = ['chats', 'tigres', 'léopards']
     >>> felins.append('lions')
     >>> print(felins)
     ['chats', 'tigres', 'léopards', 'lions']
     ```

!!! tip "La concaténation"

     Avec l'opérateur `+`, on peut **concaténer** deux listes, c'est-à-dire créer une nouvelle liste formée avec deux listes.

!!! example "Exemple de concaténation"

     ```python
     >>> lst1 = [3, 5, 7]
     >>> lst2 = [12, 15, 9]
     >>> lst3 = lst1 + lst2
     >>> print(lst3)
      [3, 5, 7, 12, 15, 9]
     ```

!!! tip "Multiplication par un entier"

     On peut utiliser la multiplication par un entier `int` pour dupliquer une liste.

!!! example "Exemple de multiplication par un entier"

     ```python
     >>> lst1 = [0]*5
     >>> print(lst1)
      [0, 0, 0, 0, 0]
     >>> lst2 = ['t', 'u']*3
     >>> print(lst2)
     ['t', 'u', 't', 'u', 't', 'u']
     ```

## Le _slicing_ en Python

!!! tip "Le _slicing_"

     Le découpage de liste (appelé _slicing_) permet d'extraire un séquence d'une liste.

     Soit `lst` une liste

     La syntaxe `lst[i:j]` permet d'extraire de la liste tous les éléments consécutifs compris entre l'élément de rang `i` **inclus** et l'élément de rang `j` **exclus**.

!!! example "Exemples de slicing"

     ```python
     >>> jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']

     ## Les deux premiers jours de la semaine
     >>> jours[0:2]
     ['lundi', 'mardi']

     ## On peut omettre le 0
     >>> jours[:2]
     ['lundi', 'mardi']

     ## Du mardi au vendredi
     >>> jours[1:5]
     ['mardi', 'mercredi', 'jeudi', 'vendredi']

     ## Du jeudi jusqu'à la fin
     >>> jours[3:]
     ['jeudi', 'vendredi', 'samedi', 'dimanche']

     ## Tout sauf le dimanche
     >>> jours[:-1]
     ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi']
     ```

!!! info

     Dans le cas du slicing, il n'y a pas d'erreur d'indexation. Par exemple:

     ```python
     >>> lst = [1, 2, 3]
     >>> lst[2021:]
     []
     ```

## Liste en compréhension en Python

!!! info

     Il est possible et élégant de construire une liste en compréhension avec le langage Python. C'est très pratique pour créer, transformer ou filtrer une liste.

!!! example "Exemples de listes en compréhension"

     ```python
     >>> nombres = [k for k in range(10)]
     >>> nombres
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
     ```

     Il est bien sûr possible d'agir sur le paramètre :

     ```python
     >>> carres_parfaits = [k**2 for k in range(10)]
     >>> carres_parfaits
     [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
     ```

!!! tip "Filtrage"

     Ajouter une **condition de filtrage** permet de ne sélectionner que certains éléments de la liste.

!!! example "Exemples de filtrages"

     ```python
     >>> c = [n for n in carres_parfaits if n % 3 == 0]
     >>> c
     [0, 9, 36, 81]
     ```

## Matrices: les listes de listes en Python

!!! tip "Création d'une liste de listes"

     Un tableau à double entrée, appelé **matrice**, peut être représenté par une liste de listes.

!!! example "Exemples de matrices"

     <style type="text/css">
     .tg  {border-collapse:collapse;border-spacing:0;}
     .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;
     overflow:hidden;padding:10px 5px;word-break:normal;}
     .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;
     font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
     .tg .tg-0lax{text-align:left;vertical-align:top}
     </style>
     <table class="tg">
     <thead>
     <tr>
     <th class="tg-0lax">7</th>
     <th class="tg-0lax">9</th>
     </tr>
     </thead>
     <tbody>
     <tr>
     <td class="tg-0lax">5</td>
     <td class="tg-0lax">2</td>
     </tr>
     </tbody>
     </table>

     ```python
     L = [[7, 9], [5, 2]]
     ```

     On peut aussi écrire sur plusieurs lignes pour plus de confort visuel:

     ```python
     L = [[7, 9],
          [5, 2]]
     ```

!!! example "Exemple du jeu de morpion"

     ![Morpion](../img/tictactoe.PNG)

     On peut représenter ce tableau par une liste de listes:

     ```python
     morpion = [['X', ' ', ' '], ['X', ' ', ' '], ['O', 'O', ' ']]
     ```

     Bien sûr on peut mettre sur plusieurs lignes:

     ```python
     morpion = [['X', ' ', ' '],
               ['X', ' ', ' '],
               ['O', 'O', ' ']]
     ```

!!! tip "Convention sur les lignes et les colonnes"

     Par convention, les **lignes** sont notées avec l'indice $i$ et les **colonnes** sont notées avec $j$.

!!! example "Exemples d'accès aux éléments des matrices"

     ```python
     morpion[i][j] # ligne d'indice i, colonne d'indice j
     morpion[0][0] # ligne 1, colonne 1
     morpion[0][0] # 'X'
     morpion[2][1] # 'O'
     morpion[1][2] # ' '
     ```

     On suppose que le joueur 'X' veuille empêcher le joueur 'O' de gagner:

     ```python
     morpion[2][2] = 'X'
     # morpion = [['X', ' ', ' '],
     #           ['X', ' ', ' '],
     #           ['O', 'O', 'X']]
     ```

!!! tip "Matrices en compréhension"

     On peut générer des matrices en compréhension

!!! example "Exemple de matrice en compréhension"

     ```python
     >>> matrice = [[i+j for j in range(3)] for i in range(3)]
     >>> matrice
     [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
     ```
