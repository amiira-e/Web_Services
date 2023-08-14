    if product_data:
                for product in product_data:
                    product_info = {
                        'name': product['product_name'],
                        'price': product['price'],
                        'image_url': product.get('img', 'No image available')
                    }
                    products_list.append(product_info)