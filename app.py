from flask import Flask, render_template, request, url_for, redirect

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

@app.route("/datosPostRecividos", methods=['POST'])
def datosPostRecividos():
   nombre = request.form.get('nombre')
   email = request.form.get('email')
   mensaje = request.form.get('mensaje')

   # Devolver la plantilla renderizada
   return render_template("datosPostRecividos.html", nombre=nombre, email=email, mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)