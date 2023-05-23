import openai
import os
from flask import Flask,request,jsonify
from dotenv import load_dotenv

# Set up OpenAI API credentials
load_dotenv("D:\Skripsi\Code\model\.env")
openai.api_key = os.getenv("OPENAI_API_KEY")
# # fine-tune = "ft-m9nqicBkFK8Cc25fpe8vUl9T"
model = os.getenv("MODEL_1")
model2 = os.getenv("MODEL_2")
model3 = os.getenv("MODEL_3")


# Define a function to send a prompt to GPT-3 and get a response


# def askGPT(text):
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=text,
#         temperature=0.6,
#         max_tokens=150,
#         stop=["\n"],
#     )
#     return print("A: "+response.choices[0].text)


# def main():
#     while True:
#         print('Bot: Ask me a question\n')
#         myQuestion = input()
#         # askGPT(myQuestion)
#         # print('\n')

#         completion = openai.Completion.create(
#             model=model3, prompt=myQuestion, max_tokens=150)

#         answer = completion.choices[0]["text"]

#         print(answer)
# main()

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    return "helloworld"
@app.route('/chatbot', methods=['GET','POST'])
def chatbot():
    if request.method == 'POST':
        data = request.form.get('data')
        completion = openai.Completion.create(model=model3, prompt=data, max_tokens=150, temperature=0.6)

        return jsonify({'answer':completion.choices[0]["text"]})
    
if __name__ == '__main__':
    app.run(debug=True)