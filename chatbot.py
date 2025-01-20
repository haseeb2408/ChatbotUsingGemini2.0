
import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyDIly_Uvnhh1i5acecax8gwfRoZUYx1YSY")

# Create the model
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
while True:
    msg=input("Your Message : ")
    response = chat_session.send_message(msg)
    print(f"Gemini's response : {response.text}")
    if msg == 'exit':
        break


if __name__ == '__main__':
    app.run(debug=True)
