from flask import Flask
app = Flask(__name__)

@app.route('/<phrase>')
def hello_world(phrase):
    output = '<H1>Hi Alex, {}</H1>'.format(phrase)
    output += '<img src="uglybunny.jpg">'
    return output
if __name__ == '__main__':
    app.run(debug=True)