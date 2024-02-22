from flask import Flask
from flask import jsonify


app = Flask(__name__)

@app.route('/prime/<int:n>')
def prime(n):
    is_prime = True
    if n <= 1:
        is_prime = False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
    
    return jsonify({
        "result": is_prime,
        "number": n
    })

if __name__ == '__main__':
    app.run()
