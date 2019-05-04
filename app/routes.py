from flask import render_template
from app import app
from xorwin.numeric_codes import numeric_codes_question


title = "11+"
domains = {
    'Maths': {
        'Addition': '/addition', 'Subtraction': '/subtraction',
        'Multiplication': '/multiplication', 'Division': '/division',
        'Bodmas': '/bodmas', 'Fractions': '/fractions',
        'Mixed Fractions': '/mixed_fractions'
    },
    'Non-Verbal Reasoning': {
        'Numeric Codes': '/numeric_codes'
    }
}


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title=title, domains=domains)


@app.route('/numeric_codes')
@app.route('/numeric_codes/')
def numeric_codes_route():
    words, codes, query, result = numeric_codes_question()
    return render_template('numeric_codes.html', title=title, domains=domains,
                           words=words, codes=codes, query=query, result=result)
