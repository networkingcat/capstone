from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello from Germany"

@app.route("/udacity")
def hello():
  return "Udacity Capstone Project"



if __name__ == "__main__":
  app.run()
