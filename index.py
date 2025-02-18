from flask import Flask

app = Flask(__name__)

@app.route("/")
def intro():
    return "I am Fatima Qurban. I am a student of Software Engineering at FAST NUCES."

if __name__ == "__main__":
    app.run(debug=True)

