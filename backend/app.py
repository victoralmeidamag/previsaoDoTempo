from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
    try:
        data = request.get_json(force=True)
        city = data.get('city','')
        print(f"a cidade é {city}")
        return jsonify({'result' : 'success'})
    except Exception as e:
        print(f"erro {str(e)}")
        return jsonify({'result' : 'error'})


if __name__ == '__main__':
    app.run(debug=True)