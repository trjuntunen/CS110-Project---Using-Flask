from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def homepage():
	html = ''
	html += '<html>\n'
	html += '<body>\n'
	html += '<form align="center" method="POST" action="/calculate" name="form">\n'
	html += '<input placeholder="1st Number" name="firstNumber">\n'
	html += '<input placeholder="2nd Number" name="secondNumber">\n'
	html += '<input placeholder="Operand" name="operand">\n'
	html += '<input type="submit" value="Submit">\n'
	html += '</form>\n'
	html += '</body>\n'
	html += '</html>\n'
	return html

@app.route('/calculate', methods=['GET', 'POST'])

def calculate():
	firstNum = request.form['firstNumber']
	secondNum = request.form['secondNumber']
	operand = request.form['operand']

	if operand != "+" and operand != "-" and operand != "*" and operand != "/":
		answer = '<p>Invalid operand. <a href="/">Click here to go back and try again</p></a>'
	if operand == "+":
		answer = str(int(firstNum) + int(secondNum))
	if operand == "-":
		answer = str(int(firstNum) - int(secondNum))
	if operand == "*":
		answer = str(int(firstNum) * int(secondNum))
	if operand == "/":
		answer = str(int(firstNum) / int(secondNum))
	return answer

if __name__ == '__main__':
	app.run()