from flask import Flask , render_template , request , jsonify
import os
import google.generativeai as genai
from  geminiy_api import api_key

genai.configure(api_key = api_key)
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)


app = Flask(__name__)


@app.route("/chat" , methods = ['POST' , 'GET'])
def chat():
    response_text = None
    if request.method == "POST":
        try:
            message = request.form.get('message')
            response = chat_session.send_message(message)
            response_text = response.text
        except:
            return "Error....."
    return render_template('chat.html' , response = response_text)
        



@app.route("/chatwithAI" , methods =['POST'])
def chatwithAI():
    try:
        data = request.get_json()
        try:
            msg = data.get('message')
            response = chat_session.send_message(msg)
            response_msg = response.text
            return jsonify({'response' : response_msg})
        except:
            return jsonify({"Error" : "'message' not found"})
    except:
        return jsonify({"Error" : "Some error in json object"})


if __name__ == '__main__':
    app.run(debug=True)
