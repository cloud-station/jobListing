from flask import Flask, render_template, jsonify


app = Flask(__name__)

STATES = [
  {
    'id' : 5,
    'abbr': 'LA',
    'capital': 'Ikeja'
  },
    {
    'id' : 2,
    'abbr': 'FT',
    'capital': 'Abuja',
    'geo': 'Federal Capital',
  },
    {
    'id' : 1,
    'abbr': 'EK',
    'capital': 'Ekiti'
  },
    {
    'id' : 7,
    'abbr': 'OS',
    'capital': 'Osun'
  },
    {
    'id' : 9,
    'abbr': 'AK',
    'capital': 'Akwa Ibom'
  }
]

@app.route('/')
def home():
    return render_template('index.html', states=STATES,title = 'State and Capital')


@app.route('/api/states')
def api():
  return jsonify(STATES)


if __name__ == '__main__':
  app.run(debug=True, port=5000, host='0.0.0.0')
