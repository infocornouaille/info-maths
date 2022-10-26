---
title: Le codage des nombres entiers
description: Le codage des nombres entiers
sidebar_position: 2
---

!!! info

    Dans toute la suite, sauf mention contraire, les nombres seront codés sur 1 octet (8 bits).

## Les nombres entiers en binaire non signé

L'expression "non signé" signifie que la contrainte du signe n'existe pas : tous les nombres sont considérés comme étant positifs.

Nous avons déjà vu comment ces nombres se codaient en binaire.

Sur un octet, le nombre minimal qu'on puisse coder est `00000000`. C'est l'entier naturel 0.

Le nombre maximal qu'on puisse coder est `11111111`. C'est l'entier naturel 255.

=== "Exercice"

    1. Quel est le plus grand entier non signé codable sur 16 bits ?
    2. ... sur 32 bits ?
    3. ... $n$ bits ?

=== "Correction"

    1. $N=1+2+2^2+2^3+\dots+2^{15}= 65535$
    2. $N=1+2+2^2+2^3+\dots+2^{31}= 4294967295$
    3. Pour tout $n \in \mathbb{N}$, $1+2+2^2+2^3+\dots+2^{n}=2^{n+1}-1$ (formule de la somme des termes d'une suite géométrique de raison 2).

Addition binaire:

=== "Exercice sur l'addition binaire"

    1. Effectuer la somme des deux nombres binaires `00001101` et `00001011`.
    2. Vérifier que le résultat est cohérent en base 10.

=== "Correction"

    1. ![](data/add1.png)
    2. Cette addition correspond à $13+11=24$

!!! savoir "A retenir"

    - Sur $n$ bits, on peut stocker $2^n$ entiers positifs.

    - Le plus grand entier positif que l'on peut représenter est $2^{n}-1$.

    - Pour évaluer le nombres de bits minimum nécessaires pour l'écriture binaire d'un entier positifn il faut trouver la plus petite puissance de 2 qui soit strictement supérieure à l'entier à écrire.

## 2. Les nombres entiers en binaire signé

!!! tip "Méthode du complément à 2"

    - Les nombres positifs sont représentés comme vu au premier chapitre mais le bit le plus fort vaut forcément zéro.

    - Les nombres négatifs sont obtenus en deux étapes:
        - On inverse les bits de l'écriture binaire de sa valeur absolue. (Complément à 1)
        - On ajoute 1 au nombre obtenu. C'est le complément à 2.

!!!example "Exemple"

    Représenton le nombre $-38$ sur 8 bits.

    Le nombre $38_{10}$ en binaire est $100110$ et donc sur 8 bits: $0010010$

    Son complément à 1 est $11011001$

    On ajoute 1, ce qui nous donne: $11011010$

    On a donc: $-38_{10} = 11011010_2$

=== "Exercice"

    Donner l'écriture binaire sur un octet du nombre $-13$.

=== "Correction"

    Commençons par écrire le nombre 13 en binaire. Il s'écrit  `00001101`.

    - en prenant le complément à 1 de chaque bit, on obtient `11110010`.
    - en ajoutant 1 à ce dernier nombre, on obtient `11110011`.

    Le nombre $-13$ s'écrit donc `11110011`.



## Travail inverse : passage du binaire signé au nombre relatif

Ce sont les même méthodes.

Si le bit fort (le plus à gauche) est un 1, notre nombre est négatif et il faut faire le complément à 2, sinon il est positif et on convertit comme pour tout entier naturel.

!!! savoir "Exemple à connaitre"

    Essayons avec 1111 1101

    Méthode 1: 1111 1101 devient 0000 0010 puis on ajoute 1 donc 0000 0011, ce qui donne 3, et donc $-3$.

    Méthode 2: 1111 1101 = 253 et $2^8-253=3$ , puisqu'il y a un 1 en bit fort, cela fait $-3$

=== "Exercice"

    1. En binaire signé, à quel nombre correspond $11110001$ ?
    2. En binaire signé, quel est le plus grand nombre que l'on puisse écrire sur un octet ?
    3. Quel est le plus petit nombre ?

=== "Correction"

    1. $11110001$ devient $00001110$ puis on ajoute 1 $00001111$ qui donne 15 et donc $-15$
    2. Le plus grand nombre est `01111111`, soit $+127$.
    3. Le nombre minimal est $-128$.


