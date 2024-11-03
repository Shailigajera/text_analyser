from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    if not text:
        return render_template('index.html', result="No text provided.")

    # Example analysis: count characters and words
    num_chars = len(text)
    num_words = len(text.split())
    analysis_result = f"Number of characters: {num_chars}<br>Number of words: {num_words}"

    return render_template('index.html', result=analysis_result)

if __name__ == '__main__':
    app.run(debug=True)
