from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

db_restaurants = []


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/v1/restaurants', methods=['GET'])
def get_restaurant():
    return jsonify({"not_implemented": "yet!"})


@app.route('/v1/restaurants/<int:restaurant_id>', methods=['GET'])
def get_food(restaurant_id):
    return jsonify({"not_implemented": "yet!"})


@app.route('/v1/restaurants', methods=['POST'])
def create_food():
    return jsonify({"not_implemented": "yet!"})


@app.route('/v1/restaurants/<int:restaurant_id>', methods=['PUT'])
def update_food(restaurant_id):
    return jsonify({"not_implemented": "yet!"})


@app.route('/v1/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_food(restaurant_id):
    return jsonify({"not_implemented": "yet!"})


if __name__ == '__main__':
    app.run(debug=True)
