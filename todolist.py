from flask import Flask, request
tasks = []
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def homepage():
	html = ''
	html += '<html>\n'
	html += '<body>\n'
	html += '<form align="center" method="POST" action="/addTask">\n'
	html += '<input type="text" placeholder="Enter task" name="form" autofocus>\n'
	html += '<input type="submit" value="Submit">\n'
	html += '</form>\n'
	html += '</body>\n'
	html += '</html>\n'
	return html

@app.route('/addTask', methods=['GET', 'POST'])

def addTask():
	task = request.form['form']
	tasks.append(task)
	html = ''
	html += '<h3>To-Do List</h3>\n'
	html += '<ol>\n'
	for i in tasks:
		html += '<li>' + str(i) + '</li>\n'
	html += '</ol>\n'
	html += '<p><a href="/">Click here to go back</a></p>\n'
	return html

if __name__ == '__main__':
    app.run()