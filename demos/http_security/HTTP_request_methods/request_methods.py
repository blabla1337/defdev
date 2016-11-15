from flask import Flask, request, url_for, render_template, redirect


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/post", methods=['POST'])
def post():
    output = "POST successful!"
    return render_template("index.html",output = output)
    
@app.route("/get", methods=['GET'])
def get():
    output = "GET successful!"
    return render_template("index.html",output = output)
    
@app.route("/put", methods=['PUT'])
def put():
    output = "Put successful!"
    return 'Put successful!'

if __name__ == "__main__":
    app.run()
	


