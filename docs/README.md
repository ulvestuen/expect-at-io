# ExpectAtIO

## Prerequisities
* Install newman (command line tool for running postman collections)
  * [Postman Learning Center: Command line integration with Newman](https://learning.getpostman.com/docs/postman/collection_runs/command_line_integration_with_newman/)
  * [Newman Github repository](https://github.com/postmanlabs/newman)

## Setup
First create python virtual environment:
```
python3 -m venv env
```
Activate python virtual environment:
```
source env/bin/activate
```
Install dependencies:
```
pip install -r requirements.txt
```
Start application:
```
python3 application.py
```

## Teardown
Deactivate virtual environment:
```
deactivate
```
Remove virtual environment by deleting `env/` folder.
