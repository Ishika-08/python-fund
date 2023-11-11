from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Company Name: ABC Corporation <br/> Location: India <br/> Contact Detail: 999-999-9999</h1>"

# pass parameter as follows http://127.0.0.1:5000/input?x=hey
@app.route("/input")
def test():
    data = request.args.get('x')
    return "this is data input from url {}".format(data)

@app.route("/welcome")
def welcome():
    return "<h1>Welcome to ABC Corporation</h1>"

@app.route("/home", methods = ['GET', 'POST'])
def home_page():
    return render_template("index.html")

@app.route("/math", methods = ['POST'])
def math_operation():
    if(request.method == 'POST'):
        ops = request.form['operation']
        n1 = int(request.form['num1'])
        n2 = int(request.form['num2'])
        
        if(ops == "add"):
            r = n1 + n2
            result = 'the sum of ' + str(n1) + ' and ' + str(n2) + ' is ' + str(r)

        if(ops == "subtract"):
            r = n1 - n2
            result = 'the substraction of ' + str(n1) + ' and ' + str(n2) + ' is ' + str(r)

        if(ops == "multiply"):
            r = n1 * n2
            result = 'the multiplication of ' + str(n1) + ' and ' + str(n2) + ' is ' + str(r)

        if(ops == "divide"):
            r = n1 / n2
            result = 'the division of ' + str(n1) + ' and ' + str(n2) + ' is ' + str(r)

    return render_template('result.html', result = result)


@app.route("/post_man", methods = ['POST'])
def math_operation_postman():
    if(request.method == 'POST'):
        ops = request.json['operation']
        n1 = int(request.json['num1'])
        n2 = int(request.json['num2'])
        
        if(ops == "add"):
            r = n1 + n2
            result = 'the sum of ' + str(n1) + ' and ' + str(n2) + ' is ' + str(r)

        if(ops == "subtract"):
            r = n1 - n2
            result = 'the substraction of ' + str(n1) + ' and ' + str(n2) + ' is ' + str(r)

        if(ops == "multiply"):
            r = n1 * n2
            result = 'the multiplication of ' + str(n1) + ' and ' + str(n2) + ' is ' + str(r)

        if(ops == "divide"):
            r = n1 / n2
            result = 'the division of ' + str(n1) + ' and ' + str(n2) + ' is ' + str(r)

    return result

if __name__ == "__main__":
    app.run(host = "0.0.0.0")