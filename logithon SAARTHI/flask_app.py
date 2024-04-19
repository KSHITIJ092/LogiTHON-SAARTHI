from flask import Flask, render_template, request
from chatbot import load_responses, chatbot

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    try:
        # Receive the user's message from the request
        user_message = request.json['answer']

        # Process user's message and get bot's response
        bot_responses = load_responses("my.csv")
        bot_response = chatbot(bot_responses, user_message)
        print(bot_response)

        # Concatenate the bot's response with the additional statement
        response_with_statement = f"{bot_response}"

        # Send back the bot's response with the additional statement
        return {'response': response_with_statement}

    except KeyError:
        return {'error': "Invalid request format. 'answer' key not found."}

    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    app.run(debug=False)  # Turn off debug mode for production
