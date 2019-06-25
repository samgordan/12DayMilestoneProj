from flask import Flask, render_template, request, redirect
import quandl
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/data', methods=['GET','POST'])
def get_data():
  print(request.form['stockName'])
  stockName = request.form['stockName']
  quandl.ApiConfig.api_key = "Fkz_a6YzFZjmydcKx8tX"
  data = quandl.get(stockName)
  print(data)
  return data.to_json()

if __name__ == '__main__':
  app.run(port=33507)


# "EIA/PET_RWTC_D"

# heroku container:push web
# heroku container:release web
# https://tranquil-peak-51666.herokuapp.com/ > https://sgd-12daymilestone.herokuapp.com/
# docker build --tag=milestone .
# docker run -p 5000:5000 -t -e PORT=5000 milestone