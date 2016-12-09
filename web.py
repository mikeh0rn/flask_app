from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", greeting="Welcome to Intro to Python")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/stock/<ticker>")
def stock_info(ticker):
  return render_template("stock.html", ticker=ticker)

app.run(debug=True)