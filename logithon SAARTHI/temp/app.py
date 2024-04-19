from flask import Flask, render_template

app = Flask(__name__,template_folder="tamplates")

@app.route('/')
def index():
    # Example data
    fruits = 'Apple'
    return render_template('index.html', fruits=fruits)

if __name__ == '__main__':
    app.run(debug=True)
