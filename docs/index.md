# Welcome to Info-Maths

!!! savoir "À savoir"

    :fontawesome-regular-hand-spock: l'informatique c'est sympa :fontawesome-regular-face-laugh-wink:

    :octicons-heart-fill-24:{ .heart }
    :octicons-heart-fill-24:{ .heart }
    :octicons-heart-fill-24:{ .heart }

!!! done "Les maths c'est sympa aussi :material-ufo-outline:{ .ufo }"

    En 1735, Leonhard Euler résout le **problème de Bâle** en établissant la formule suivante :

    $$\sum\limits_{k\in\mathbb N^*} \frac 1 {k^2} = \frac {\pi^2}6$$

    Cependant, il ne démontrera rigoureusement son résultat qu’en 1741.


```python
print("Cliquez sur la croix !") # (1)
```

1.  :man_raising_hand: Je suis un commentaire ! Je peux contenir du  `code`, du texte, des images, ... en gros tout ce qu'on veut :octicons-heart-fill-24:{ .heart }



``` py
import tensorflow as tf
```

``` py title="bubble_sort.py"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```




=== "C"

    ``` c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "C++"

    ``` c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```
:octicons-heart-fill-24:{ .heart }








`Lorem ipsum dolor sit amet`

:   Sed sagittis eleifend rutrum. Donec vitae suscipit est. Nullam tempus
    tellus non sem sollicitudin, quis rutrum leo facilisis.

`Cras arcu libero`

:   Aliquam metus eros, pretium sed nulla venenatis, faucibus auctor ex. Proin
    ut eros sed sapien ullamcorper consequat. Nunc ligula ante.

    Duis mollis est eget nibh volutpat, fermentum aliquet dui mollis.
    Nam vulputate tincidunt fringilla.
    Nullam dignissim ultrices urna non auctor.

