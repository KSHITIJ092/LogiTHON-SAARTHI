from flask import Flask, render_template, request, jsonify
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
        bot_responses = load_responses(r"C:\WEB DEVELOPMENT\LogiTHON-SAARTHI\logithon SAARTHI\my.csv")
        print("Bot Responses:", bot_responses)
        bot_response = chatbot(bot_responses, user_message)
        print("Bot Response:", bot_response)

        # Send back the bot's response
        return jsonify({'response': bot_response})

    except KeyError:
        error_message = "Invalid request format. 'answer' key not found."
        print("Error:", error_message)
        return jsonify({'error': error_message}), 400

    except Exception as e:
        error_message = "An error occurred: " + str(e)
        print("Error:", error_message)
        return jsonify({'error': error_message}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Turn off debug mode for production
