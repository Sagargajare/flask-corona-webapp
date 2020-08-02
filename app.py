
import requests
from bs4 import BeautifulSoup
import json
import requests

extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
URL = 'https://www.mohfw.gov.in/'



response = requests.get(URL).content
soup = BeautifulSoup(response, 'html.parser')
header = extract_contents(soup.tr.find_all('th'))



all_rows = soup.find_all('tr')
def func():
    data = requests.get("https://api.covid19india.org/data.json")
    data = data.json()
    return data["statewise"]





from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    stats1 = func()

    return render_template('index.html',a = stats1)



if __name__ == "__main__":
    app.run(debug=True)
