from flask import Flask, request, jsonify
import json


class ShoppingStatisticsAPI:

    def __init__(self):
        self.file_path = "../api_implementation/products.json"

    def load_products(self):
        with open(self.file_path) as file:
            data = json.load(file)
        return data

    @staticmethod
    def categories(data):
        cat = list(set(product['category'] for product in data))
        return cat

    @staticmethod
    def money_spent_by_category(category, products):
        matching_products = [product for product in products if product["category"] == category]
        grand_total = 0
        for match in matching_products:
            gross_total = float(match["price"]) * float(match["quantity"])
            single_total = gross_total - (gross_total * float(match["percentage_discount"])) / 100
            grand_total += single_total
        return grand_total

    def get_statistics(self):
        category = request.args.get('category')
        data = self.load_products()
        if category in self.categories(data):
            total = self.money_spent_by_category(category, data)
            return jsonify({"data": {category: total}})
        elif category is None:
            all_categories = self.categories(data)
            totals = []
            for cat in all_categories:
                totals.append(self.money_spent_by_category(cat, data))
            data = dict(zip(all_categories, totals))
            return jsonify({"data": data})
        else:
            return "404 Not a valid category", 404


app = Flask(__name__)


@app.route('/api/v1/shopping/statistics', methods=['GET'])
def get_statistics():
    api = ShoppingStatisticsAPI()
    return api.get_statistics()


if __name__ == '__main__':
    app.run(debug=True)
