from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", posts=posts)


@app.route('/post/<int:num>')
def see_post(num):
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("post.html", num=num, posts=posts)




if __name__ == "__main__":
    app.run(debug=True)
