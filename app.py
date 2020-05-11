from flask import Flask, render_template, request, redirect, url_for
import stripe

app = Flask(__name__)

pub_key = 'pk_test_uAmL6T5HDj6mV6y3CvB7sCEe00h4cf8UOg'
secret_key = 'sk_test_ULxF57krPKjNhDcsHt8Axykz00t44Ox2Zc'

stripe.api_key = secret_key

@app.route('/')
def index():
    return render_template('index.html', pub_key=pub_key)

@app.route('/encerramento')
def encerramento():
    return render_template('encerramento.html')

@app.route('/pagamento', methods=['POST'])
def pagamento():
    #quantidade = request.form
    cliente = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    cobranca = stripe.Charge.create(
        customer=cliente.id,
        amount=19900,
        currency='brl',
        description='Cobrança'
    )

    return redirect(url_for('encerramento'))

if __name__ == '__main__':
    app.run(debug=True)