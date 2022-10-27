# Les files

![](data/giffile.webp){: .center}

Comme expliqué précédemment, une file travaille en mode FIFO (First In First Out).
Pour être utilisée, une interface de file doit proposer a minima :

- la création d'une file vide
- l'ajout d'un élément dans la file. On dira qu'on **enfile**.
- le retrait d'un élément de la file et le renvoi de sa valeur. On dira qu'on **défile**.

La représentation la plus courante d'une file se fait horizontalement, en enfilant par la gauche et en défilant par la droite :

![image](data/repfile.png){: .center}

## Utilisation d'une interface de file

!!! example "{{ exercice() }}"

    === "Énoncé"

        On considère l'enchaînement d'opérations ci-dessous. Écrire à chaque étape l'état de la file `f` et la valeur éventuellement renvoyée.

        Par convention, on enfilera **à gauche** et on défilera **à droite**.

        ```python
        1. f = File()
        2. f.enfile(3)
        3. f.enfile(5)
        4. f.est_vide()
        5. f.enfile(1)
        6. f.defile()
        7. f.defile()
        8. f.enfile(9)
        9. f.defile()
        10. f.defile()
        11. f.est_vide()
        ```


    === "Correction"

        {{ correction(True,
            "
            ```python
            1. f est vide
            2. f = 3
            3. f = 5 3
            4. val renvoyée : False
            5. f  = 1 5 3
            6. val renvoyée : 3 , f = 1 5
            7. val renvoyée : 5 , f =  1
            8. f =  9 1
            9. val renvoyée : 1 , f =  9
            10. val renvoyée : 9 , f est vide
            11. val renvoyée : True
            ```
            "
            ) }}

## Implémentation d'une file

L'objectif est de créer une classe `File`, disposant des méthodes suivantes :

- `File()` : crée une file vide.
- `est_vide()` : indique si la file est vide.
- `enfile()` : insère un élément en queue de file.
- `defile()` : renvoie la valeur de l'élément en tête de la file ET le supprime de la file.
- `__str__()` : permet d'afficher la file sous forme agréable (par ex : `|3|6|2|5|`) par `print()`

!!! example "Exercice"

    === "Énoncé"

        Créer la classe ci-dessus. Là encore, le type `list` de Python est peut être utilisé.

        Penser à aller voir [ici](https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists) les méthodes des objets de types ```list```, notamment la méthode ```insert```.

    === "Correction"

        {{ correction(True,
        "
        ```python linenums='1'
        class File:
            def __init__(self):
                self.data = []

            def est_vide(self):
                return len(self.data) == 0

            def enfile(self, x):
                self.data.insert(0, x)

            def defile(self):
                if self.est_vide():
                    print('Vous avez essayé de défiler une file vide !')
                    return None
                else :
                    return self.data.pop()

            def __str__(self):       # Hors-Programme : pour afficher
                s = '|'              # convenablement la file avec print(p)
                for k in self.data:
                    s = s + str(k) + '|'
                return s
        ```

        ```python
        >>> f = File()
        >>> f.enfile(5)
        >>> f.enfile(8)
        >>> print(f)
        |8|5|
        >>> f.defile()
        5
        ```


        "
        ) }}

**Remarque :**  
Notre implémentation répond parfaitement à l'interface qui était demandée. Mais si le «cahier des charges» obligeait à ce que les opérations `enfile()` et `defile()` aient lieu en temps constant (en $O(1)$), notre implémentation ne conviendrait pas.

En cause : notre méthode `enfile()` agit en temps linéaire ($O(n)$) et non pas en temps constant. L'utilisation de la structure de «liste» de Python (les _tableaux dynamiques_) provoque, lors de l'instruction `self.data.insert(0, x)` un redimensionnement de la liste. Le tableau doit être agrandi et chaque élément doit être recopié dans la case suivante. Ceci nous coûte un temps linéaire.

## Implémentation d'une file avec deux piles

Comment créer une file avec 2 piles ?  
L'idée est la suivante : on crée une pile d'entrée et une pile de sortie.

- quand on veut enfiler, on empile sur la pile d'entrée.
- quand on veut défiler, on dépile sur la pile de sortie.
- si celle-ci est vide, on dépile entièrement la pile d'entrée dans la pile de sortie.

<center>
<gif-player src="https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.1_Listes_Piles_Files/data/2piles1file.gif" speed="1" play></gif-player>
</center>

```python linenums='1'
# il est impératif de comprendre qu'on peut choisir l'implémentation
# de la classe Pile qu'on préfère parmi les deux traitées plus haut.
# Comme elles ont la MÊME INTERFACE et qu'on ne va se servir que
# de cette interface, leur mécanisme interne n'a aucune influence
# sur le code de la classe File que nous ferons ensuite.

# Par exemple, on choisit celle avec la liste chaînée :

class Cellule :
    def __init__(self, contenu, suivante):
        self.contenu = contenu
        self.suivante = suivante


class Pile:
    def __init__(self):
        self.data = None

    def est_vide(self):
        return self.data == None

    def empile(self, x):
        self.data = Cellule(x, self.data)

    def depile(self):
        v = self.data.contenu #on récupère la valeur à renvoyer
        self.data = self.data.suivante  # on supprime la 1ère cellule
        return v

    def __str__(self):
        s = "|"
        c = self.data
        while c != None :
            s += str(c.contenu)+"|"
            c = c.suivante
        return s

# -------------------------------------------------------
# Implémentation d'une file à l'aide de deux piles

class File:
    def __init__(self):
        self.entree = Pile()
        self.sortie = Pile()

    def est_vide(self):
        return self.entree.est_vide() and self.sortie.est_vide()

    def enfile(self,x):
        self.entree.empile(x)

    def defile(self):
        if self.est_vide():
            print("File vide !")
            return None

        if self.sortie.est_vide():
            while not self.entree.est_vide():
                self.sortie.empile(self.entree.depile())

        return self.sortie.depile()


```

```python
>>> f = File()
>>> f.enfile(5)
>>> f.enfile(8)
>>> f.defile()
5
```
