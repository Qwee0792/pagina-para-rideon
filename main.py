from flask import Flask,render_template

app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('Home.html')

@app.route('/Descargar')
def descargar():
    return render_template('Descargar.html')

@app.route('/Trabajo')
def trabajo():
    return render_template('trabajo.html')

@app.route('/contactanos')
def contactanos():
    return render_template('contacto.html')

@app.route('/Politica')
def political_pribacidad():
    return render_template('politicas.html')


# error handling
@app.errorhandler(404)
def error_404():
    return render_template('error_404.html')
@app.errorhandler(500)
def error_500():
    return render_template('error_500.html')

# local development
# if __name__ == '__main__':
#     app.run(host='0.0.0.0',debug=True)