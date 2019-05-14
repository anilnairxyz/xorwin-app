from flask import render_template
from app import app
from xorwin.numeric_codes import numeric_codes_question
from xorwin.arithmetic import Question1


title = "11+"
domains = {
    'Mathematical Operations': {
        'Integer Operations': {
            'Addition': '/integer_addition', 'Subtraction': '/integer_subtraction',
            'Multiplication': '/integer_multiplication', 'Division': '/integer_division',
            'Bodmas': '/integer_bodmas'
        },
        'Decimal Operations': {
            'Addition': '/decimal_addition', 'Subtraction': '/decimal_subtraction',
            'Multiplication': '/decimal_multiplication', 'Division': '/decimal_division'
#        },
#        'Fraction Operations': {
#            'Addition': '/fraction_addition', 'Subtraction': '/fraction_subtraction',
#            'Multiplication': '/fraction_multiplication', 'Division': '/fraction_division',
#            'Bodmas': '/fraction_bodmas'
#        },
#        'Mixed Fraction Operations': {
#            'Addition': '/mixed_addition', 'Subtraction': '/mixed_subtraction',
#            'Multiplication': '/mixed_multiplication', 'Division': '/mixed_division',
#            'Bodmas': '/mixed_bodmas'
        }
    },
    'Non-Verbal Reasoning': {
        'Encoding': {
            'Numeric Codes': '/numeric_codes'
        }
    }
}


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title=title, domains=domains)


@app.route('/numeric_codes')
def numeric_codes_route():
    breadcrumb = {'h1': 'Non-Verbal Reasoning', 'h2': 'Numeric Codes'}
    words, codes, query, result = numeric_codes_question()
    return render_template('numeric_codes.html', title=title, domains=domains, breadcrumb=breadcrumb,
                           words=words, codes=codes, query=query, result=result)


@app.route('/integer_addition')
def integer_addition():
    breadcrumb = {'h1': 'Maths', 'h2': 'Addition'}
    arithmetic = Question1()
    arithmetic.negative = True
    arithmetic.decimal_pt = 0
    arithmetic.value_range = (0, 10000)
    arithmetic.operand_count = 2
    arithmetic.operations = ['+']
    q = arithmetic.frame_decimal_question()
    query = q.sequence_str
    result = q.result
    return render_template('operations.html', title=title, domains=domains, breadcrumb=breadcrumb,
                           query=query, result=result)


@app.route('/integer_subtraction')
def integer_subtraction():
    breadcrumb = {'h1': 'Maths', 'h2': 'Subtraction'}
    arithmetic = Question1()
    arithmetic.negative = True
    arithmetic.decimal_pt = 0
    arithmetic.value_range = (0, 10000)
    arithmetic.operand_count = 2
    arithmetic.operations = ['-']
    q = arithmetic.frame_decimal_question()
    query = q.sequence_str
    result = q.result
    return render_template('operations.html', title=title, domains=domains, breadcrumb=breadcrumb,
                           query=query, result=result)


@app.route('/integer_multiplication')
def integer_multiplication():
    breadcrumb = {'h1': 'Maths', 'h2': 'Multiplication'}
    arithmetic = Question1()
    arithmetic.negative = True
    arithmetic.decimal_pt = 0
    arithmetic.value_range = (0, 10000)
    arithmetic.operand_count = 2
    arithmetic.operations = ['*']
    q = arithmetic.frame_decimal_question()
    query = q.sequence_str
    result = q.result
    return render_template('operations.html', title=title, domains=domains, breadcrumb=breadcrumb,
                           query=query, result=result)


@app.route('/integer_division')
def integer_division():
    breadcrumb = {'h1': 'Maths', 'h2': 'Division'}
    arithmetic = Question1()
    arithmetic.negative = True
    arithmetic.decimal_pt = 0
    arithmetic.value_range = (0, 10000)
    arithmetic.operand_count = 2
    arithmetic.operations = ['/']
    q = arithmetic.frame_decimal_question()
    query = q.sequence_str
    result = q.result
    return render_template('operations.html', title=title, domains=domains, breadcrumb=breadcrumb,
                           query=query, result=result)


@app.route('/integer_bodmas')
def integer_bodmas():
    breadcrumb = {'h1': 'Maths', 'h2': 'Bodmas'}
    arithmetic = Question1()
    arithmetic.negative = True
    arithmetic.decimal_pt = 0
    arithmetic.value_range = (0, 10)
    arithmetic.operand_count = 4
    q = arithmetic.frame_decimal_question()
    query = q.sequence_str
    result = q.result
    return render_template('operations.html', title=title, domains=domains, breadcrumb=breadcrumb,
                           query=query, result=result)


@app.route('/decimal_addition')
def decimal_addition():
    breadcrumb = {'h1': 'Maths', 'h2': 'Addition'}
    arithmetic = Question1()
    arithmetic.negative = True
    arithmetic.decimal_pt = 1
    arithmetic.value_range = (0, 10)
    arithmetic.operand_count = 2
    arithmetic.operations = ['+']
    q = arithmetic.frame_decimal_question()
    query = q.sequence_str
    result = q.result
    return render_template('operations.html', title=title, domains=domains, breadcrumb=breadcrumb,
                           query=query, result=result)


@app.route('/decimal_subtraction')
def decimal_subtraction():
    breadcrumb = {'h1': 'Maths', 'h2': 'Subtraction'}
    arithmetic = Question1()
    arithmetic.negative = True
    arithmetic.decimal_pt = 1
    arithmetic.value_range = (0, 10)
    arithmetic.operand_count = 2
    arithmetic.operations = ['-']
    q = arithmetic.frame_decimal_question()
    query = q.sequence_str
    result = q.result
    return render_template('operations.html', title=title, domains=domains, breadcrumb=breadcrumb,
                           query=query, result=result)


@app.route('/decimal_multiplication')
def decimal_multiplication():
    breadcrumb = {'h1': 'Maths', 'h2': 'Multiplication'}
    arithmetic = Question1()
    arithmetic.negative = True
    arithmetic.decimal_pt = 1
    arithmetic.value_range = (0, 10)
    arithmetic.operand_count = 2
    arithmetic.operations = ['*']
    q = arithmetic.frame_decimal_question()
    query = q.sequence_str
    result = q.result
    return render_template('operations.html', title=title, domains=domains, breadcrumb=breadcrumb,
                           query=query, result=result)


@app.route('/decimal_division')
def decimal_division():
    breadcrumb = {'h1': 'Maths', 'h2': 'Division'}
    arithmetic = Question1()
    arithmetic.negative = True
    arithmetic.decimal_pt = 1
    arithmetic.value_range = (0, 10)
    arithmetic.operand_count = 2
    arithmetic.operations = ['/']
    q = arithmetic.frame_decimal_question()
    query = q.sequence_str
    result = q.result
    return render_template('operations.html', title=title, domains=domains, breadcrumb=breadcrumb,
                           query=query, result=result)


@app.route('/fraction_addition')
def fraction_addition():
    breadcrumb = {'h1': 'Maths', 'h2': 'Addition'}
    arithmetic = Question1()
    arithmetic.negative = True
    arithmetic.decimal_pt = 0
    arithmetic.value_range = (0, 100)
    arithmetic.operand_count = 2
    arithmetic.operations = ['+']
    q = arithmetic.frame_fraction_question()
    query = q.sequence_str
    result = q.result
    return render_template('operations.html', title=title, domains=domains, breadcrumb=breadcrumb,
                           query=query, result=result)


@app.route('/fraction_subtraction')
def fraction_subtraction():
    breadcrumb = {'h1': 'Maths', 'h2': 'Subtraction'}
    arithmetic = Question1()
    arithmetic.negative = True
    arithmetic.decimal_pt = 0
    arithmetic.value_range = (0, 100)
    arithmetic.operand_count = 2
    arithmetic.operations = ['-']
    q = arithmetic.frame_fraction_question()
    query = q.sequence_str
    result = q.result
    return render_template('operations.html', title=title, domains=domains, breadcrumb=breadcrumb,
                           query=query, result=result)


@app.route('/fraction_multiplication')
def fraction_multiplication():
    breadcrumb = {'h1': 'Maths', 'h2': 'Multiplication'}
    arithmetic = Question1()
    arithmetic.negative = True
    arithmetic.decimal_pt = 0
    arithmetic.value_range = (0, 100)
    arithmetic.operand_count = 2
    arithmetic.operations = ['*']
    q = arithmetic.frame_fraction_question()
    query = q.sequence_str
    result = q.result
    return render_template('operations.html', title=title, domains=domains, breadcrumb=breadcrumb,
                           query=query, result=result)


@app.route('/fraction_division')
def fraction_division():
    breadcrumb = {'h1': 'Maths', 'h2': 'Division'}
    arithmetic = Question1()
    arithmetic.negative = True
    arithmetic.decimal_pt = 0
    arithmetic.value_range = (0, 100)
    arithmetic.operand_count = 2
    arithmetic.operations = ['/']
    q = arithmetic.frame_fraction_question()
    query = q.sequence_str
    result = q.result
    return render_template('operations.html', title=title, domains=domains, breadcrumb=breadcrumb,
                           query=query, result=result)


@app.route('/fraction_bodmas')
def fraction_bodmas():
    breadcrumb = {'h1': 'Maths', 'h2': 'Bodmas'}
    arithmetic = Question1()
    arithmetic.negative = True
    arithmetic.decimal_pt = 0
    arithmetic.value_range = (0, 100)
    arithmetic.operand_count = 4
    q = arithmetic.frame_fraction_question()
    query = q.sequence_str
    result = q.result
    return render_template('operations.html', title=title, domains=domains, breadcrumb=breadcrumb,
                           query=query, result=result)
