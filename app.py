from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/Home')
def home():
    return render_template('index.html') 

@app.route('/about')
def about():
    return render_template('aboutus.html') 

@app.route('/membership')
def membership(): 
    return render_template('membership.html') 

if __name__ == "__main__":
    app.run(debug=True)
