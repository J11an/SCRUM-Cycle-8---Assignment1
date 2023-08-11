"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app
from flask import render_template, request, redirect, url_for

#Fixed product list to populate the website.
products = [
    {
        'product_id': 0,
        'image': 'tshirt.jpg',
        'title': 'T-Shirt',
        'price': 15.99,
        'product_details': 'A comfortable and stylish black T-shirt made from high-quality cotton.'
    },
    {
        'product_id': 1,
        'image': 'shorts.webp',
        'title': 'Shorts',
        'price': 24.99,
        'product_details': 'Casual navy cotten shorts, perfect for a relaxed summer look.'
    },
    {
        'product_id': 2,
        'image': 'hat.webp',
        'title': 'Hat',
        'price': 9.99,
        'product_details': 'A stylish canvas hat that provides great sun protection.'
    },
    {
        'product_id': 3,
        'image': 'sneakers.webp',
        'title': 'Shoes',
        'price': 49.99,
        'product_details': 'Trendy white sneakers made from high-quality synthetic leather.'
    },
    {
        'product_id': 4,
        'image': 'slippers.jpg',
        'title': 'Slippers',
        'price': 9.99,
        'product_details': 'Comfortable rubber slippers for indoor and outdoor use made from a eco-friendly resource.'
    },
    {
        'product_id': 5,
        'image': 'pant.jpg',
        'title': 'Pants',
        'price': 49.99,
        'product_details': 'Classic cargo pants suitable for various occasions.'
    }
]


# Home page that contains information about owner of site.
@app.route('/')
def home():
    return render_template('home.html')

# Page that displays all the products.
@app.route('/products/')
def get_products():
    return render_template('products.html', products=products)

# Page that displays an individual product.
@app.route('/products/<product_id>')
def product_info(product_id):
    product_id = int(product_id)
    for prod in products:
        if product_id == products.index(prod):
            product = products[product_id]
            return render_template('product.html',product=product)
    else:
        return render_template('404.html')
    

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
