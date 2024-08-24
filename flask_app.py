from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def flask_home():
    return render_template("redirect.html", url="https://pabloriosp.github.io/")

@app.route("/sum", methods=["GET", "POST"])
def sum_access():
    if request.method == 'POST':
        data = request.json
        return sum(data['a'], data['b'])
    else:
        return render_template("redirect.html", url="https://pabloriosp.github.io/docs/projects/project-1.html")
        
def sum(a, b):
    try:
        a = int(a)
        b = int(b)
        return f"<p>{a} + {b} = {a + b}</p>"
    except ValueError:
        return "<p class='error-msg'>Error: Debes ingresar números enteros en ambos campos.</p>"
    except Exception as e:
        return f"<p class='error-msg'>Error: {e}"
