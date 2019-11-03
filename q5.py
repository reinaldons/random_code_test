import json

def sort_by_price_ascending(json_string):
    products = json.loads(json_string)

    return json.dumps(sorted(products, key=lambda x: x['price']))

print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))
