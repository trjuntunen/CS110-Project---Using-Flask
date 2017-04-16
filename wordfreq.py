from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def homepage():
    html = ''
    html += '<html>\n'
    html += '<body>\n'
    html += '<form method="POST" action="/calculate">'
    html += '<input type="text" placeholder="Enter text here" name="text">'
    html += '<input type="submit" value="Submit">'
    html += '</form>'
    html += '</body>\n'
    html += '</html>\n'
    return html

@app.route('/calculate', methods=['GET', 'POST'])

def calculate():
    wordDictionary = {}
    text = request.form['text']
    processedText = text.lower().split()
    for word in processedText:
        if word not in wordDictionary:
            wordDictionary[word] = 0
        if word in wordDictionary:
            wordDictionary[word] += 1
    html = ''
    html += '<table border="1">'
    html += '<th>Word</th>'
    html += '<th>Count</th>'
    for i in sorted(wordDictionary.keys()):
        html += '<tr>'
        html += '<td>' + str(i) + '</td>'
        html += '<td>' + str(wordDictionary[i]) + '</td>'
        html += '</tr>'
    html += '</table>'
    return html

if __name__ == '__main__':
    app.run()
