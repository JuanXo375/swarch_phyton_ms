from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.products_service import ProductService

product_blueprint = Blueprint('products', __name__)
@product_blueprint.route('/products', methods=['POST'])
def create_product():
    data = request.form
    name = data.get('name')
    description = data.get('description')
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    ProductService.create_product(name, description)
    return redirect(url_for('products.index'))

@product_blueprint.route('/products/<int:product_id>', methods=['POST'])
def update_product(product_id):
    if request.form.get('_method') == 'PUT':
        data = request.form
        name = data.get('name')
        description = data.get('description')

        # Verificar que el nombre o la descripción no están vacíos
        if not name or not description:
            return jsonify({'error': 'Name and description are required'}), 400

        # Actualizar el producto con el id especificado
        updated_product = ProductService.update_product(product_id, name, description)

        if not updated_product:
            return jsonify({'error': 'Product not found'}), 404

        return redirect(url_for('products.index'))  # Redirigir a la vista de productos después de la actualización

    return jsonify({'error': 'Invalid method'}), 405

@product_blueprint.route('/')
def index():
    return render_template('index.html')

@product_blueprint.route('/products/<int:product_id>/edit', methods=['GET'])
def edit_product(product_id):
    product = ProductService.get_product_by_id(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return render_template('index_put.html', product=product)