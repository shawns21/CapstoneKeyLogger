from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_number():
    number = request.json.get('number')
    if number is not None:
        log_number(number)
        return "Number received and logged successfully."
    else:
        return "No number received."

def log_number(number):
    with open('receivedText.txt', 'a') as file:
        file.write(number + '\n')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)