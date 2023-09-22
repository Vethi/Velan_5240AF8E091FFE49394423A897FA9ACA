def linear_search_product(product_list, target_product):
    indices = []
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    return indices

# Example usage
products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]
target_product = "Apple"

result = linear_search_product(products, target_product)
if result:
    print(f"{target_product} found at indices: {result}")
else:
    print(f"{target_product} not found in the list.")
  