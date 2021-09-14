from flask import Blueprint, request, jsonify, Flask
from decimals import decimals

from function_jwt import validate_token

app_pi = Blueprint("_pi_", __name__)


@app_pi.before_request
def verify_token_middleware():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token, output=False)


@app_pi.route('/pi/<int:n>', methods=["GET"])
def pi(n):
    fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    search_pi = "3."
    i = 0
    n_decimal = n

    if int(n) == 0 or int(n) > 12:
        return jsonify({"Error En consulta ": "numero consultado debe estar entre 1 y 12", "valor enviado": n})

    if int(n) <= 13:
        search_decimals = fibonacci[n - 1]

    while i < search_decimals:
        search_pi += str(decimals[i])
        i = i + 1

    n_decimal = decimals[int(n - 1)]

    if (int(n) == 2) or (int(n) == 3) or (int(n) == 4):
        n_decimal = -1

    return jsonify({"n-decimal": n_decimal, "pi-fibonacci": search_pi})
