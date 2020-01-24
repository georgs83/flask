from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return '<a href=''/about''>Hi!</a>'

@app.route('/about')
def about():
  return '<h1>Georgs Ņefedovs</h1>'

@app.route('/about')
def contact():
  return render_template('contact.html')


if __name__ == '__main__':
  app.run(host = '0.0.0.0', prot = 5211, threaded = True, debug = True)
