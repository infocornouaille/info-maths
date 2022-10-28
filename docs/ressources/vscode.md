# Visual Studio Code

## Téléchargement

[VSCode](https://code.visualstudio.com/)

## Utiliser le formateur Python Black avec Visual Studio Code

[Black](https://pypi.org/project/black/) est "le formateur de code Python sans compromis".

Il peut être configuré pour formater automatiquement votre code chaque fois que vous enregistrez un fichier
dans VSCode.

Installez Black dans votre environnement:

=== "conda"

    ```bash
    conda install -c conda-forge black
    ```

=== "pip"

    ```bash
    pip install black
    ```

=== "poetry"

    ```bash
    poetry add black
    ```

2. Dans les préférences de VS Code, recherchez "python formatting provider" puis sélectionnez "black".

3. Cherchez ensuite "format on save" et cochez la case "Editor: Format on Save"

!!!example "Exemple"

    === "Avant formattage"

        ```python
        a=2
        a=5+3
        ```

    === "Après formattage"

        ```python
        a = 2
        a = 5 + 3
        ```

## Faire du Latex

Sur Mac, après avoir installé l'extention Latex Workspace

```bash
sudo cpan -i YAML::Tiny File::HomeDir Unicode::GCString
```

https://tex.stackexchange.com/questions/390433/how-can-i-install-latexindent-on-macos
