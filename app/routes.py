from flask import Blueprint, render_template, request, redirect, url_for
from .models import products

main = Blueprint('main', __name__)

@main.route('/')
def home():
 return render_template('index.html', products=products)

@main.route('/buy/<int:product_id>', methods=['POST'])
def buy(product_id):
 for product in products:
    if product.id == product_id and product.stock > 0:
        product.stock -= 1
        break
 return redirect(url_for('main.home'))

@main.route('/add-product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # Ambil data dari form
        name = request.form.get('name')
        price = request.form.get('price', type=int)
        stock = request.form.get('stock', type=int)
        image = request.form.get('image')
        
        # Validasi sederhana
        if not name or not price or not stock or not image:
            return "Semua data harus diisi!", 400
        
        # Tambahkan produk baru ke daftar
        new_id = max(product.id for product in products) + 1
        products.append(Product(new_id, name, price, stock, image))
        return redirect(url_for('main.home'))
    
    return render_template('add_product.html')
