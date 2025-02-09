from repositories.products_repository import ProductRepository

class ProductService:
    
    @staticmethod
    def create_product(name, description):
        return ProductRepository.create_product(name, description)
    
    @staticmethod
    def get_product_by_id(product_id):
        return ProductRepository.get_product_by_id(product_id)
    
    @staticmethod
    def update_product(product_id, name, description):
        # Llamar al método del repositorio para actualizar el producto
        updated_product = ProductRepository.update_product(product_id, name, description)
        
        # Verificar si se actualizó correctamente el producto
        if not updated_product:
            return None  # Retornar None si el producto no existe
        
        return updated_product  # Retornar el producto actualizado