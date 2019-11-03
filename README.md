# Cron Expression Parser

Program to create a tabular representation of cron expressions

## Prerequisites

```
    - activate Python virtual environment

    - pip3 install -r requirements.txt
```

## Usage

<pre>
    parameter 0: main.py
    parameter 1: munute [0-59]
    parameter 2: hour [0-23]
    parameter 3: day of month [1-31]
    parameter 4: month [1-12]
    parameter 5: day of week [0-6]
    parameter 6: command

    example: main.py */15 0 1,15 * 1-5 /usr/bin/find
</pre>

## Unit Tests

Run pre-configured unit tests for the program

```
    - ./tests.py
```
