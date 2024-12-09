from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from chatbot.chat_utils import fetchChatHistory,chatWithChain

app = Flask(__name__)

CORS(app)


@app.route("/chat/<session_id>", methods = ['GET', 'POST'])
def disp(session_id):
    input = request.get_json(force=True)
    user_id = input.get('user_id')
    user_input = input.get('user_input')

    if not input:
        return jsonify({'error': 'No user input provided'}), 400

    chat_history = fetchChatHistory(user_id, session_id)
    return Response(chatWithChain(user_input, chat_history), content_type='text/plain')

if __name__ == '__main__':
    app.run(debug = True)