from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/book_consultation')
def consultation():
    return render_template('consultation.html')

if __name__ == '__main__':
    app.run(debug=True)