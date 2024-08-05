from flask import_Flask, request, jsonify
import util
app = Falask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Accers-Control-Allow-Origin', '^')

    return response


if __name__== "__main__":
    print("String python Flask Server For Home Price Prediction...")
    app.run()