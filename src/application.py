from flask import Flask
from api.api_controller import ApiController
from service.test_service import TestService

app = Flask(__name__)
test_service = TestService()
api = ApiController(test_service)
app.add_url_rule('/load', 'load', api.load, methods=["POST"])
app.add_url_rule('/run', 'run', api.run, methods=["POST"])
app.add_url_rule('/results', 'results', api.results, methods=["GET"])
app.add_url_rule('/collection', 'collection', api.collection, methods=["GET"])
app.add_url_rule('/inputdata', 'input_data', api.input_data, methods=["GET"])
app.add_url_rule('/outputdata', 'output_data', api.output_data, methods=["GET"])
app.add_url_rule('/ready', 'ready', api.ready, methods=["GET"])
app.add_url_rule('/busy', 'busy', api.busy, methods=["GET"])


if __name__ == '__main__':
    app.run()
