from core.models import Product


def print_product_data():
    product_instance = Product.objects.last()

    # Print the attributes of the retrieved instance
    if product_instance:
        print("Product Name:", product_instance.name)
        print("Quantity:", product_instance.quantity)
        print("Min Quantity:", product_instance.min_quantity)
        print("Expiration Date:", product_instance.expiration_date)
        print("Supplier:", product_instance.supplier)
        print("Product Type:", product_instance.product_type)
        print("Stock Number:", product_instance.stock_number)
        print("Image:", product_instance.image.url if product_instance.image else None)
        print("Note:", product_instance.note)
        print("Created At:", product_instance.created_at)
        print("Updated At:", product_instance.updated_at)
        print("Created By:", product_instance.created_by)


print_product_data()
