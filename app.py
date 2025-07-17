from flask import Flask, render_template, request, redirect
from sweet_shop import SweetShop

app = Flask(__name__)
shop = SweetShop()

@app.route('/')
def index():
    sweets = shop.view_sweets()
    return render_template('index.html', sweets=sweets)

@app.route('/process', methods=['POST'])
def process():
    try:
        id = int(request.form['id'])
        name = request.form['name']
        category = request.form['category']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])
        action = request.form['action']  # 'add' or 'sell'

        shop.add_or_sell_sweet(id, name, category, price, quantity, action)

    except Exception as e:
        return f"<h2>Error: {str(e)}</h2><a href='/'>Go back</a>"

    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    shop.delete_sweet(id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
