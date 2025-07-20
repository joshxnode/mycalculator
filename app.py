from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    expression = ""
    result = ""
    
    if request.method == "POST":
        expression = request.form.get("expression", "")
        if "clear" in request.form:
            expression = ""
        elif "equals" in request.form:
            try:
                result = str(eval(expression))
            except:
                result = "Error"
        else:
            button = request.form.get("button")
            expression += button

    return render_template("index.html", expression=expression, result=result)

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')

