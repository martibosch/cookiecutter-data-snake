![lint](https://github.com/martibosch/cookiecutter-data-snake/actions/workflows/lint.yaml/badge.svg)
![tests](https://github.com/martibosch/cookiecutter-data-snake/actions/workflows/tests.yaml/badge.svg)

# Cookiecutter Data Snake

A reproducible data science template using a bunch of snakes :snake:, i.e., Python, snakemake, mamba, and more.

This cookiecutter is based on [`cookiecutter-data-science`](http://drivendata.github.io/cookiecutter-data-science/), with the following main differences:

- [snakemake](https://snakemake.github.io) to orchestrate the data analysis workflow instead of [GNU Make](https://www.gnu.org/software/make) ([recommended in `cookiecutter-data-science`](https://drivendata.github.io/cookiecutter-data-science/)). The advantages of snakemake are its more Pythonic syntax as well as the availability of a dedicated code formatter, i.e., [snakefmt](https://github.com/snakemake/snakefmt) (see pre-commit item below).
- [mamba](https://github.com/mamba-org/mamba) as a package manager, which provides a CLI that is almost identical to [conda](https://conda.io) but *(much) faster*.
- [pre-commit](https://pre-commit.com) to manage multi-language pre-commit hooks, including: [black](https://black.readthedocs.io/), [isort](https://pycqa.github.io/isort) and [flake8](https://flake8.pycqa.org) to format and lint Python files (`.py`), [nbstripout](https://github.com/kynan/nbstripout) and [nbQA](https://nbqa.readthedocs.io) to format and lint Jupyter Notebooks (`.ipynb`); [snakefmt](https://github.com/snakemake/snakefmt) to format Snakefiles and more.

## Requirements to use the cookiecutter template:

- Python 3.8+
- [cookiecutter](http://cookiecutter.readthedocs.org), which can be installed with pip, conda or mamba (see [the official installation instructions](https://cookiecutter.readthedocs.org/en/latest/installation.html)).
- [mamba](https://github.com/mamba-org/mamba), which can be installed using conda or [mambaforge](https://github.com/conda-forge/miniforge#mambaforge) (see [the official installation instructions](https://github.com/mamba-org/mamba#installation))

## To start a new project, run:

```bash
$ cookiecutter gh:martibosch/cookiecutter-data-snake
```

fill the required parameters and then follow the instructions in the generated `README.md` file.

## Acknowledgments

- Project based on [Henk Griffioen's version](https://github.com/hgrif/cookiecutter-ds-python) of the [cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science). #cookiecutterdatascience
