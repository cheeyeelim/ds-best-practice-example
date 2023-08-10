# ds-best-practice-example


[![pypi](https://img.shields.io/pypi/v/ds-best-practice-example.svg)](https://pypi.org/project/ds-best-practice-example/)
[![python](https://img.shields.io/pypi/pyversions/ds-best-practice-example.svg)](https://pypi.org/project/ds-best-practice-example/)
[![Build Status](https://github.com/cheeyeelim/ds-best-practice-example/actions/workflows/dev.yml/badge.svg)](https://github.com/cheeyeelim/ds-best-practice-example/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/cheeyeelim/ds-best-practice-example/branch/main/graphs/badge.svg)](https://codecov.io/github/cheeyeelim/ds-best-practice-example)



Showcase best practices for structuring a simple DS-related Python package/application.

If you notice any best practice missing/incorrect, please do let me know and I will update them.

This example package will fit a linear regression on your input data. It comes with the `diabetes` data as a toy data.

Note that this example comes with many tools/components to help your development, but do enable/disable them based on your needs.

The recommend minimum tools I usually go for in most of my projects are :
- Poetry - for Python package management
- Pre-commit - for formating and linting
- hydra - for package configurations
- logging - for logging runtime information
- Pytest - for unit testing

The additional tools are :
- Mkdocs (+ extensions) - for documentation generation
- Tox - for testing under multiple environments
- Codecov - for code coverage report
- GitHub Actions - for CI/CD


* Documentation: <https://cheeyeelim.github.io/ds-best-practice-example>
* GitHub: <https://github.com/cheeyeelim/ds-best-practice-example>
* PyPI: <https://pypi.org/project/ds-best-practice-example/>
* Free software: BSD-3-Clause

## How to install this package?

The easiest way is to install it with pip.

```bash
pip install ds-best-practice-example
```

## How to run this package?

You run this package via both command line and Python.

Note that all configurations are specified via `hydra` in this [config yaml](./input/conf/config.yaml).

Please refer to the [example notebook](./notebook/ds-best-practice-example.ipynb) for more details.

### (1) Run via command line

```bash
poetry run python cli.py
```

### (2) Run via Python

```python
import hydra

from ezml.data import prepare_data
from ezml.model import train_model
from ezml.diagnostic import diagnose_model

# Use Hydra config with Compose API
hydra.initialize(version_base=None, config_path="../input/conf")
cfg = hydra.compose(
    config_name="config",
    overrides=["data.file_path=../input/data/diabetes.csv", "model.file_path=../output/model/linreg_diabetes.joblib"]
)

# Train linear regression with default data
X_train, X_test, y_train, y_test = prepare_data(cfg)
model = train_model(cfg, X_train, y_train)
diagnose_model(X_test, y_test, model)
```

## How to create this project from scratch?

You can create it from scratch by following the steps below.

The steps assumed `cookiecutter`, `pre-commit` and `poetry` has been installed. Otherwise follow their respective installation instructions to install them.

```bash
# Setup project folder interactively
cookiecutter https://github.com/cheeyeelim/cookiecutter-pypackage.git

# Setup pre-commit
pre-commit install

# Update pyproject.toml with required packages
# Install Python packages
poetry install -E test -E dev -E doc
```

## Features

* TODO

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [cheeyeelim/cookiecutter-pypackage](https://github.com/cheeyeelim/cookiecutter-pypackage) project template.
