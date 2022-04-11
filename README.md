# Polidoro Question
[![Upload Python Package](https://github.com/heitorpolidoro/polidoro-question/actions/workflows/python-publish.yml/badge.svg)](https://github.com/heitorpolidoro/polidoro-question/actions/workflows/python-publish.yml)
[![Lint with comments](https://github.com/heitorpolidoro/polidoro-question/actions/workflows/python-lint.yml/badge.svg)](https://github.com/heitorpolidoro/polidoro-question/actions/workflows/python-lint.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/heitorpolidoro/polidoro-question)
[![Coverage Status](https://coveralls.io/repos/github/heitorpolidoro/polidoro-question/badge.svg?branch=master)](https://coveralls.io/github/heitorpolidoro/polidoro-question?branch=master)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_polidoro-question&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_polidoro-question)

[![Latest](https://img.shields.io/github/release/heitorpolidoro/polidoro-question.svg?label=latest)](https://github.com/heitorpolidoro/polidoro-question/releases/latest)
![GitHub Release Date](https://img.shields.io/github/release-date/heitorpolidoro/polidoro-question)

![PyPI - Downloads](https://img.shields.io/pypi/dm/polidoro-question?label=PyPi%20Downloads)

![GitHub](https://img.shields.io/github/license/heitorpolidoro/polidoro-question)
### To install

```shell
sudo apt install python3-pip -y
pip3 install polidoro_question
```
Retrieve input from terminal user input.

```python
from polidoro_question import Question
resp = Question('Your question here').ask()
```

#### Parameters
`question`: The text to show to the user.
`type`: The type to convert the answer.
`default`: Default value of the question.
`options`: List of options to choose.
`auto_complete`: To use auto-complete mode.
In auto-complete mode will show all the options in a list, the user can either type to filter or choose 
a number to select the option