from flask import Flask;
app = Flask(__name__)

@app.route("/home")
def getHome():
    return 'Hello World'

import requests
page = requests.get("")
pag
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')