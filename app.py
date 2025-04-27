from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_usle(A=None, R=None, K=None, LS=None, C=None, P=None, unknown="A"):
    if unknown == "A":
        return R * K * LS * C * P
    elif unknown == "R":
        return A / (K * LS * C * P)
    elif unknown == "K":
        return A / (R * LS * C * P)
    elif unknown == "LS":
        return A / (R * K * C * P)
    elif unknown == "C":
        return A / (R * K * LS * P)
    elif unknown == "P":
        return A / (R * K * LS * C)
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            unknown = request.form["unknown"]

            # Handle empty fields as None
            def get_value(name):
                value = request.form.get(name)
                return float(value) if value else None

            A = get_value("A")
            R = get_value("R")
            K = get_value("K")
            LS = get_value("LS")
            C = get_value("C")
            P = get_value("P")

            result = calculate_usle(A=A, R=R, K=K, LS=LS, C=C, P=P, unknown=unknown)

        except ValueError:
            result = "Invalid input. Please enter numeric values."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
