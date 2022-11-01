from flask import Flask, render_template, request
from profanity_check import predict, predict_prob

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template("homepage.html", result="")
    else:
        text_content = request.form['content']
        has_swear_content = predict([text_content])
        has_swear_content_prob = predict_prob([text_content])
        return render_template("homepage.html",
                               input=text_content,
                               result=has_swear_content[0] == 1 if "true" else "false",
                               probability=has_swear_content_prob)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
