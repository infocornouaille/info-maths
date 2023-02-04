[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# info-maths

Site des cours de NSI et de spécialité Mathématiques du lycée de Cornouaille

## install

First thing’s first, we need to get our development environment set up.

```bash
conda create --name info-maths
```

```bash
conda activate info-maths
```

```bash
conda install poetry
```

```bash
poetry install
```

```bash
brew install cairo freetype libffi libjpeg libpng zlib
```

https://info-maths.netlify.app

## A ajouter

- annotations
- notebook

# Update

```
poetry update
```

```
poetry export -f requirements.txt --output requirements.txt
```
