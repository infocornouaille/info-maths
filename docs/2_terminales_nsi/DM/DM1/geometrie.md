---
title: Géométrie en POO
description: Géométrie en POO
sidebar_position: 3
---

## Objectifs

En utilisant la programmation objet, nous allons définir des points et des
figures géométriques (rectangles, cercles, etc.) ainsi que les méthodes pour les représenter graphiquement et
les transformer (translation).

!!!danger "Attention"
Le fichier `graphNSI.py` ne devra pas être modifié.

    Le rendu sera uniquement le fichier `geometrieObjet.py`

## graphNSI.py

Commencez par créer un fichier `graphNSI.py`et y coller le code suivant:

```python title="graphNSI.py"
--8<-- "includes/graphNSI.py"
```

## geometrieObjet.py

Dans le même dossier que `graphNSI.py` créez le fichier `geometrieObjet.py` puis y coller le code suivant:

```python title="geometrieObjet.py"
# geometrieObjet.py
import math
import graphNSI as gd


# On initialise l'affichage graphique
gd.init("figures")
# On trace le repère dans la fenêtre graphique
gd.tracerRepere()


# Début de la description des objets
class Point():
    """La classe Point. Un point est défini par ses coordonnées
    x et y"""
    def __init__(self,x,y):
        """Le constructeur de la classe Point"""
        self.x=x    # Initialisation des attributs de l'objet
        self.y=y
    def tracer(self):
        """La méthode de traçage d'un point dans la fenêtre graphique"""
        #Un point est tracé sous la forme d'un cercle (pour être visible)
        #de rayon 1 et avec une épaisseur de trait 1
        gd.tracerCercle(self.x,self.y,1,1)


# On fabrique deux objets de classe Point
p1= Point(20,10)
p2= Point(-100,-20)
print(p1.x)         #on peut accéder aux attributs depuis un objet
p1.tracer()         #on peut appeler une méthode sur un objet
                    #cela trace le premier point
# On trace le second point
p2.tracer()

# On affiche le résultat
gd.show()
```

## Question 1

Lisez le code de `geometrieObjet.py` et repérez la définition de la classe `Point`, son **constructeur**
`__init__`, les **attributs** de l'objet et les **méthodes**.

En vous inspirant du code de `Point` définissez une classe `Cercle` (constructeur, attributs,
méthodes). Un cercle sera défini par son **centre** et un **rayon**. Définissez une méthode `tracer()` et testez-la
en traçant plusieurs cercles construits à l'aide de cette classe.

Dans votre classe `Cercle`, est-ce que le centre est lui même un objet de classe `Point` ? Si ça
n'est pas le cas modifiez votre classe de façon à ce que cela soit le cas. En particulier, votre constructeur
prendra un point en paramètre.

!!!info "Liens avec le paradigme objet"

    Les classes sont des moules pour fabriquer des objets en série.

    L'unique classe `Point` permet de produire des objets points différents (des **instances**). Dans le code du fichier `geometrieObjet.py`, un objet `point` est associé à la variable `p1` et un autre est associé à la variable `p2`. Ces objets ont des **attributs** qui contiennent des valeurs et des **méthodes** qui sont des fonctions spécifiques aux objets de cette classe.

    Par exemple, on ne trace pas de la même façon un point et un cercle. Dans votre code, la méthode `tracer()` d'un point doit être différente de `tracer()` d'un cercle.

## Question 2

Définissez une classe Rectangle défini par deux objets de classe Point : le coin supérieur
gauche et le coin inférieur droit. En vous servant de `gd.tracerRectangle`, définissez une méthode `tracer()`
et testez-la en traçant plusieurs rectangles construits à l'aide de cette classe.

!!!info "gd.tracerRectangle"

    gd.tracerRectangle(x1,y1,x2,y2,e)

    Tracer un rectangle de coordonnées (x1,y1) (x2,y2) et d'épaisseur e (en pixels).

## Question 3

Définissez une classe Combinaison qui comporte une liste (unique) d'autres figures (point,
cercle, rectangles). Définissez une méthode `tracer()` et testez-la en traçant une combinaison construite à
l'aide de cette classe.

!!!info "Liens avec le paradigme objet"

    Tous vos objets ont des types. Dans ce que nous faisons ici, le type
    d'un objet sera toujours le nom de la classe qui l'a construit.

    Pour obtenir cette information, en Python on peut utiliser `type`.

    Par exemple print(type(p1)) doit vous donner : <class '**main**.Point'>.

    Ainsi, si j'appelle `p1.tracer()`, Python saura qu'il faut appeler la méthode `tracer()` de la classe Point
    en consultant le type de p1. En objet, on parle aussi d'**encapsulation**. Avec l'**encapsulation**, un objet
    point/Cercle/Rectangle/Combinaison saura quelle méthode `tracer()` appeler pour être correctement tracée.

## Question 4

Ajoutez une méthode `translation(self,deplacement_x,deplacement_y)` dans vos classes Point, Cercle,
Rectangle, Combinaison, puis testez-la.

!!!info "Liens avec le paradigme objet"

    Une des principales élégances du modèle objet est l'**encapsulation** : on regroupe sous un même couvercle des données et des fonctions relatives à ces données.

    Dans cet exercice,
    on peut appliquer une même opération (ici une translation) à des objets différents (points, rectangles,
    cercles, combinaison) sans avoir besoin de connaître leur type précis dans le code. Ainsi, on peut écrire
    `p.translation(-2, 4)` sans savoir quel sera le type de `p`.

    Ceci est un exemple du principe d'**abstraction**, un autre pilier du paradigme objet. Avant de démarrer un développement, on peut imposer ce **principe d'abstraction** en définissant une **interface**, mais c'est une autre histoire ...
