from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Teknik Pemrograman', version='0.0.1')

@app.route('/')
def index():
    return 'Hello world from teknik pemrograman 2019-07-11'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
