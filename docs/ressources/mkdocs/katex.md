---
title: Ajouter katex à mkdocs
description: Comment ajouter katex à mkdocs
---


# Ajouter Katex à MkDocs

=== "javascripts/katex.js"

    ```js
    --8<-- "docs/javascripts/katex.js"
    ```

=== "mkdocs.yml"

    ```yaml
    extra_javascript:
        - javascripts/katex.js 
        - https://cdn.jsdelivr.net/npm/katex@0.16.3/dist/katex.min.js 

    extra_css:
        - stylesheets/extra.css
        - https://cdn.jsdelivr.net/npm/katex@0.16.3/dist/katex.min.css
    ```
