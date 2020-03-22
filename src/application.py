import connexion
from flask_cors import CORS
import sys

app = connexion.App(__name__, specification_dir='openapi/')
app.add_api('openapi.yml')
CORS(app.app)

if __name__ == '__main__':
    host_ip = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
    app.run(host=host_ip)
