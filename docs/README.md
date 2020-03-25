# ExpectAtIO

## Prerequisities
* Install newman (command line tool for running postman collections)
  * [Postman Learning Center: Command line integration with Newman](https://learning.getpostman.com/docs/postman/collection_runs/command_line_integration_with_newman/)
  * [Newman Github repository](https://github.com/postmanlabs/newman)




## How to run a test (example)
### Setup
#### On localhost
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
#### In docker
From the `/expect-at-io` folder, run the following command to build a docker image:
```
docker build -t expect-at-io:latest .
```
### Start test framework
#### On localhost
```
python3 application.py
```
#### In docker
In this example, the test framework is started together with the test object.

### Start test object
#### On localhost
From within the `example/wiremock-test/` folder, run the following script to start an example instance of wiremock:
```
./start_wiremock.sh
```
#### In docker
Enter the `example/wiremock-test/` folder and run the following command to build a new docker image of the 
wiremock-test instance:
```
docker build -t wiremock-test:latest .
```
From the `example/` folder, start the test environment:
```
docker-compose up -d
```
### Run test
#### On localhost
Test is loaded by the following curl command:
```
curl -X POST \
  http://localhost:5000/load \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F collection=@wiremock-test.postman_collection.json \
  -F testdata=@input-output_data.json
```

#### In docker
Test is loaded by the following curl command:
```
curl -X POST \
  http://localhost:5000/load \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F collection=@wiremock-test.postman_collection.json \
  -F testdata=@input-output_data-docker.json
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
### On localhost
Deactivate the virtual environment:
```
deactivate
```
Remove the virtual environment by deleting `env/` folder.

### In docker
```
docker stop expect-at-io
docker rm expect-at-io
docker rmi expect-at-io
```
