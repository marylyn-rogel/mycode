from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    # Implement the logic to process the data from the POST request here
    # For simplicity, let's just store the data in a text file
    data = request.form['hiking_data']
    with open('data.txt', 'w') as f:
        f.write(data)
    return 'Data received and processed successfully!'

