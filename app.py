
import requests
from bs4 import BeautifulSoup


extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
URL = 'https://www.mohfw.gov.in/'



response = requests.get(URL).content
soup = BeautifulSoup(response, 'html.parser')
header = extract_contents(soup.tr.find_all('th'))



all_rows = soup.find_all('tr')
def func():
    stats = []
    for row in all_rows:
        stat = extract_contents(row.find_all('td'))
        # print(stat)

        if stat:
            if len(stat) == 6:
                # last row
                stat = ['', *stat]
                stats.append(stat)
            elif len(stat) == 5:
                stats.append(stat)
    return stats





from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    stats1 = func()

    return render_template('index.html',a = stats1)



if __name__ == "__main__":
    app.run(debug=True)
