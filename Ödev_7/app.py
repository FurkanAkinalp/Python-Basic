from flask import Flask, render_template, redirect, url_for
from data import create_new_plot

app = Flask(__name__)

@app.route('/')
def index():
    create_new_plot()
    return render_template('index.html')

@app.route('/generate_new')
def generate_new():
    create_new_plot()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
