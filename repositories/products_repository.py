from models.products import Products, db

class ProductRepository:

    @staticmethod
    def create_product(name, description):
        product = Products(name=name, description=description)
        db.session.add(product)
        db.session.commit()
        return product
    
    @staticmethod
    def get_product_by_id(product_id):
        return Products.query.get(product_id)
    
    @staticmethod
    def update_product(product_id, name, description):
        # Buscar el producto por su ID
        product = db.session.query(Products).filter(Products.id == product_id).first()
        
        if product:
            # Actualizar los campos del producto
            product.name = name
            product.description = description
            db.session.commit()  # Guardar los cambios en la base de datos
            return product  # Retornar el producto actualizado
        return None  # Retornar None si no se encontró el producto