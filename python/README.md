Install

install virtual environment

```bash
## install virtual environment
python3 -m venv .venv

## activate virtual environment
source .venv/bin/activate

## install pip
python -m pip install --upgrade pip

## install pytest
pip install -U pytest

## install pylint
pip install -U pylint

```

Running
```bash
## activate virtual environment
source .venv/bin/activate

## run tests
python -m pytest -o markers=task hello_world_test.py

## run specific tests
python -m pytest -o markers=task currency-exchange/exchange_test.py -k 'test_exchange_money'

## run lint
pylint guidos-gorgeous-lasagna/lasagna.py -v

## submit exercises
exercism submit guidos-gorgeous-lasagna/lasagna.py

## down a new task (run from project root)
exercism download --exercise=ghost-gobble-arcade-game --track=python
```
