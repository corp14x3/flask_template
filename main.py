from flask import Flask , render_template , request , url_for , redirect

app = Flask(__name__)
app.secret_key = "ruhi123"

@app.route("/", methods=["GET","POST"])
def main():
    hello = ""
    if request.method == "POST":
        if "hi" in request.form:
            hello = "selam"
        if "deneme" in request.form:
            hello = "happy"
    return render_template("index.html",ss=hello)


if __name__ == "__main__":
    app.run()