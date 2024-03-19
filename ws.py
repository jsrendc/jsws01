# pronostico_tiempo.py

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/autos', methods=['GET'])
def obtener_pronostico():
    ciudad = request.args.get('ciudad')
    # Simulación de datos de pronóstico del tiempo
    la = [
            {"id":1,"nombre":"Carro 1","marca":"JS","precio":10000},
            {"id":2,"nombre":"Carro 2","marca":"JS","precio":2500},
            {"id":3,"nombre":"Carro 3","marca":"JS","precio":10000},
            {"id":4,"nombre":"Carro 4","marca":"JS","precio":10000},
            {"id":5,"nombre":"Carro 5","marca":"JS","precio":2500},
            {"id":6,"nombre":"Carro 6","marca":"JS","precio":10000}
        ]
    return jsonify(la)

if __name__ == '__main__':
    app.run(debug=True)
