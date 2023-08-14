from flask import Flask, render_template, request
import http.client
import json  # Import the json module

app = Flask(__name__)

def get_shoprite_product_data(product_id):
    conn = http.client.HTTPSConnection("igrosa-api.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "2d60ff54bcmsh6e16394e740f1a0p18ab6ajsnd1e619f64dc9",
        'X-RapidAPI-Host': "igrosa-api.p.rapidapi.com"
    }

    endpoint = f"/shoprite/{product_id}"
    conn.request("GET", endpoint, headers=headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")

@app.route('/', methods=['GET', 'POST'])
def getproduct():
    product_data = None

    if request.method == 'POST':
        product_id = request.form.get('product_id')
        if product_id:
            product_data = get_shoprite_product_data(product_id)
            product_data = json.loads(product_data)  # Parse JSON
            # print(product_data)

            # Instead of directly returning product_data, create a list of products
            products_list = []

            if product_data:
                for product in product_data:
                    product_info = {
                        'name': product['product_name'],
                        'price': product['price'],
                        'image_url': product.get('img', 'No image available')
                    }
                    products_list.append(product_info)

            return render_template('getproduct.html', products_list=products_list)

    return render_template('getproduct.html', products_list=product_data)

if __name__ == '__main__':
    app.run(debug=True)