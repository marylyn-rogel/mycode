from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    # Implement the logic to process the data from the POST request here
    # Store the data in a text file
    data = request.form['hiking_data']
    with open('data.txt', 'w') as f:
        f.write(data)
    return 'Data received and processed successfully!'


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=800)
