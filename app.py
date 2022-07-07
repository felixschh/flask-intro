from flask import Flask, render_template

# create instance
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/about')
def about():
    return "<p>about</p>"





if __name__ == "__main__":
    app.run(debug=True)