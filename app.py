from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello World!"


@app.route("/about")
def about():
  return "Page About!"

# validation for development server
if __name__ == "__main__":
  app.run(debug=True)