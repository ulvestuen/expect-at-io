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
### On localhost
```
python3 application.py
```
### In docker
From the `/expect-at-io` folder, run the following command to build a docker image:
```
docker build -t expect-at-io:latest .
docker run --name expect-at-io -p 5000:5000 expect-at-io:latest <optional bind-address (default 127.0.0.1)>
```

### Start test object
### On localhost
From within the `example/wiremock-test/` folder, run the following script to start an example instance of wiremock:
```
./start_wiremock.sh
```
### In docker
From within the `example/wiremock-test/` folder, run the following script to start an example instance of wiremock:
```
docker build -t wiremock-test:latest .
docker run --name wiremock-test -p 9998:9998 wiremock-test:latest
```

### Run test
Test is loaded by the following curl command:
```
curl -X POST \
  http://localhost:5000/load \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F collection=@wiremock-test-json.postman_collection.json \
  -F testdata=@input-output_data-json.json
```

```
curl -X POST \
  http://localhost:5000/load \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F collection=@wiremock-test-xml.postman_collection.json \
  -F testdata=@input-output_data-xml.json
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
