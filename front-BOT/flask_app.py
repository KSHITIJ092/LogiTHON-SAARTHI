
from flask import Flask, render_template, request
from chatbot import load_responses,chatbot

# app = Flask(__name__, template_folder='standalone-frontend')
app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/', methods=['POST'])
def handle_form():
    question = request.form['answer']
    print("Received message:", question)
    answer = chatbot(responses,question)
    print(answer)
    return '', 204

if __name__ == '__main__':
    responses = load_responses("my.csv")
    app.run(debug=True)