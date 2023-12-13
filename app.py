from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import Usuario
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Rutas y lógica de la aplicación

@app.route('/')
def landing_page():
    return render_template('landing.html')

@app.route('/facultad/<nombre_facultad>')
def mostrar_facultad(nombre_facultad):
    # Lógica para mostrar la página de la facultad según el nombre
    # Aquí puedes agregar cualquier lógica adicional que necesites
    return render_template(f'{nombre_facultad}.html')

@app.route('/ingenieria')
def ingenieria():
    return render_template('ingenieria.html')

@app.route('/economia')
def economia():
    return render_template('economia.html')

@app.route('/ciencias')
def ciencias():
    return render_template('ciencias.html')

# Agrega más rutas según sea necesario para cada facultad

# Ruta para la nueva facultad
@app.route('/facnueva')
def facnueva():
    return render_template('facnueva.html')

# Rutas para la información detallada del producto y enviar mensaje al vendedor
@app.route('/ingenieria/<int:producto_id>', endpoint='producto_info')
def producto_info(producto_id):
    # Lógica para obtener información detallada del producto según su ID
    # Puedes pasar esta información a la plantilla producto_info.html
    return render_template('ingenieria/producto_1_info.html', producto_id=producto_id)

# Ruta para la información detallada del segundo producto
@app.route('/ingenieria/producto_2_info')
def producto_2_info():
    # Lógica para obtener información detallada del producto 2
    # Puedes pasar esta información a la plantilla producto_2_info.html
    return render_template('ingenieria/producto_2_info.html')


@app.route('/enviar_mensaje/<int:producto_id>')
def enviar_mensaje(producto_id):
    # Lógica para la página de enviar mensaje al vendedor
    # Puedes pasar información del vendedor y del producto a la plantilla enviar_mensaje.html
    return render_template('enviar_mensaje.html', producto_id=producto_id)

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        numero_cuenta = request.form['numero_cuenta']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        confirmar_contrasena = request.form['confirmar_contrasena']
        facultad = request.form['facultad']
        imagen = guardar_imagen(request.files['imagen'])

        if contrasena != confirmar_contrasena:
            return render_template('error.html', mensaje='Las contraseñas no coinciden.')

        nuevo_usuario = Usuario(
            nombres=nombres,
            apellidos=apellidos,
            numero_cuenta=numero_cuenta,
            correo=correo,
            contrasena=contrasena,  # Aquí debes guardar la contraseña de manera segura
            facultad=facultad,
            imagen=imagen
        )

        db.session.add(nuevo_usuario)
        db.session.commit()

        # Redireccionar a la página de inicio de sesión
        return redirect(url_for('inicio_de_sesion'))

    return render_template('error.html', mensaje='Método no permitido.')

def guardar_imagen(imagen):
    if imagen:
        filename = os.path.join('static', 'uploads', imagen.filename)
        imagen.save(filename)
        return filename
    return None

if __name__ == '__main__':
    app.run(debug=True)
