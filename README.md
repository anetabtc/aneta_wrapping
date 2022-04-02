# aneta-wrapping
Decentralized Wrapping of Bitcoin for Ergo and Cardano

## Repository Description

This codebase implements a framework for *decentralized wrapping of Bitcoin for Ergo and Cardano Networks*, as described in [this lite paper](https://medium.com/@anetaBTC/anetabtc-litepaper-v1-0-171f29b3276a). Several features are concurrently under active development. **Please contact <willie@tca.io> before attempting to use it for your own research.** In particular, this codebase aims to ultimately provide an integrated system for creating wrapped Bitcoin as anetaBTC tokens on Ergo and Cardano. 

### Code Structure

TBD

## Installation
* This repository uses Python versions 3.8+.
* Run `pip install -r requirements.txt` to install dependencies.

## Instructions For Running Code

### Locally
* (recommended) Make a new virtual env or conda env.
* Make sure the parent of the repository is on your PYTHONPATH.
* Run, e.g., `python src/main.py --network testnet` to run the system.

## Instructions For Contributing
* Run `pip install -r requirements-dev.txt` to install all dependencies for development.
* You can't push directly to master. Make a new branch in this repository (don't use a fork, since that will not properly trigger the checks when you make a PR). When your code is ready for review, make a PR and request reviews from the appropriate people.
* To merge a PR, you need at least one approval, and you have to pass the 4 checks defined in `.github/workflows/predicators.yml`, which you can run locally in one line via `./scripts/run_checks.sh`, or individually as follows:
    * `pytest -s tests/ --cov-config=.coveragerc --cov=src/ --cov=tests/ --cov-fail-under=100 --cov-report=term-missing:skip-covered --durations=0`
    * `mypy . --config-file mypy.ini`
    * `pytest . --pylint -m pylint --pylint-rcfile=.predicators_pylintrc`
    * `yapf -i -r --style .style.yapf . && docformatter -i -r . && isort .`
* The first one is the unit testing check, which verifies that unit tests pass and that code is adequately covered. The "100" means that all lines in every file must be covered.
* The second one is the static typing check, which uses Mypy to verify type annotations. If it doesn't work due to import errors, try `mypy -p predicators --config-file predicators/mypy.ini` from one directory up.
* The third one is the linter check, which runs Pylint with the custom config file `.predicators_pylintrc` in the root of this repository. Feel free to edit this file as necessary.
* The fourth one is the autoformatting check, which uses the custom config files `.style.yapf` and `.isort.cfg` in the root of this repository.
