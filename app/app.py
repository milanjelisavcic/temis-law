import os

from flask import Flask
from flask import request
from flask_cors import CORS

from PyPDF2 import PdfReader

app = Flask(__name__)
CORS = CORS(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    return "Hello, I am Temis graph scrapper!"

@app.route('/upload', methods=['POST'])
def upload():
    pdf_file = request.files['file']

    pdf_reader = PdfReader(pdf_file)

    response = ""
    for page in pdf_reader.pages:
        page_content = page.extract_text()
        
        response += page_content

    pdf_file.close()
    return response

if __name__ == '__main__':
    app.run(debug=True)
