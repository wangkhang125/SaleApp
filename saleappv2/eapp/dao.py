from eapp.models import Category, Product

def load_category():
    return Category.query.all()

def load_product():
    query = Product.query


    return query.all()