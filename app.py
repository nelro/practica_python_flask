from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

#para poder dirigirme a la pagina quienes somos 
@app.route("/quienes_somos")
def quienes_somos():
    return render_template("quienes_somos.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/noticias")
def noticias():
    return render_template("noticias.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True)