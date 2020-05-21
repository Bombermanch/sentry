import os
import sentry_sdk

from bottle import Bottle, request
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
	dsn=os.environ.get("https://1554a87737b04a93b9068e2a93a4d9ac@o395806.ingest.sentry.io/5248299"),
	integrations=[BottleIntegration()]
)

app = Bottle()


@app.route('/success') 
def success():
	return "OK"

@app.route('/fail') 
def fail():    
	raise RuntimeError("There is an error!")

app.run(host='localhost', port=8080)