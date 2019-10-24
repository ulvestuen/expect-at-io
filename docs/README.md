# ExpectAtIO

## Prerequisities
* Install newman (command line tool for running postman collections)
  * [Postman Learning Center: Command line integration with Newman](https://learning.getpostman.com/docs/postman/collection_runs/command_line_integration_with_newman/)
  * [Newman Github repository](https://github.com/postmanlabs/newman)

## Setup
From within the `src/` folder, first create a python virtual environment:
```
python3 -m venv env
```
Activate the python virtual environment:
```
source env/bin/activate
```
Install dependencies:
```
pip install -r requirements.txt
```

## How to run a test (example)

### Start test framework
```
python3 application.py
```

### Start test object
From within the `example/` folder, run the following script to start an example instance of wiremock:
```
./start_wiremock.sh
```

### Run test
Test is loaded by the following curl command:
```
curl -X POST \
  http://localhost:5000/load \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F collection=@wiremock-test.postman_collection.json \
  -F testdata=@input-output_data.json
```

Then run the test:
```
curl -X POST http://localhost:5000/run
```

Obtain test results:
```
curl -X GET http://localhost:5000/results
```


## Teardown
Deactivate the virtual environment:
```
deactivate
```
Remove the virtual environment by deleting `env/` folder.
