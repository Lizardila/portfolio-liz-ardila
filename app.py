from flask import Flask, render_template, abort

app = Flask(__name__)


# ==========================================
# DATOS DEL PORTAFOLIO
# ==========================================

proyectos = [

    {
        "id": "diario-animo",
        "nombre": "Diario de Ánimo",
        "categoria": "Python",
        "tipo": "Aplicación de consola",
        "descripcion": "Aplicación de consola para registrar estados de ánimo y reflexiones diarias.",
        "objetivo": "Crear una aplicación sencilla que permita registrar y consultar información personal mediante una interfaz de consola.",
        "tecnologias": [
            "Python",
            "Bucles",
            "Condicionales",
            "Listas"
        ],
        "destacado": True
    },

    {
        "id": "calculadora-iva",
        "nombre": "Calculadora del IVA",
        "categoria": "Python",
        "tipo": "Utilidad financiera",
        "descripcion": "Aplicación para calcular automáticamente el IVA de un producto y obtener su precio final.",
        "objetivo": "Automatizar cálculos financieros sencillos mediante una aplicación desarrollada en Python.",
        "tecnologias": [
            "Python",
            "Funciones",
            "Cálculos"
        ],
        "destacado": True
    },

    {
        "id": "simulador-inversiones",
        "nombre": "Simulador de Inversiones",
        "categoria": "Python",
        "tipo": "Finanzas y simulación",
        "descripcion": "Simulador que permite analizar el crecimiento de una inversión mediante interés compuesto.",
        "objetivo": "Comprender y representar mediante programación cómo evoluciona una inversión a lo largo del tiempo.",
        "tecnologias": [
            "Python",
            "Funciones",
            "Matemáticas",
            "Bucles"
        ],
        "destacado": True
    },

    {
        "id": "organizador-archivos",
        "nombre": "Organizador Automático de Archivos",
        "categoria": "Python",
        "tipo": "Automatización",
        "descripcion": "Script que clasifica automáticamente archivos según su extensión para mantener organizada una carpeta.",
        "objetivo": "Automatizar tareas repetitivas y mejorar la organización de archivos mediante Python.",
        "tecnologias": [
            "Python",
            "OS",
            "Automatización",
            "Archivos"
        ],
        "destacado": True
    },

    {
        "id": "mi-portafolio",
        "nombre": "Mi Portafolio",
        "categoria": "Web",
        "tipo": "Desarrollo web",
        "descripcion": "Página web personal desarrollada con Flask, HTML y CSS para presentar proyectos y habilidades.",
        "objetivo": "Crear un espacio profesional para mostrar mis proyectos y documentar mi evolución como desarrolladora.",
        "tecnologias": [
            "Python",
            "Flask",
            "HTML5",
            "CSS3",
            "Jinja2"
        ],
        "destacado": True
    }

]


# ==========================================
# HABILIDADES
# ==========================================

habilidades = [

    {
        "nombre": "Python",
        "nivel": "Intermedio"
    },

    {
        "nombre": "HTML5",
        "nivel": "Intermedio"
    },

    {
        "nombre": "CSS3",
        "nivel": "Intermedio"
    },

    {
        "nombre": "Flask",
        "nivel": "En aprendizaje"
    },

    {
        "nombre": "Jinja2",
        "nivel": "En aprendizaje"
    },

    {
        "nombre": "Git",
        "nivel": "En aprendizaje"
    },

    {
        "nombre": "Automatización",
        "nivel": "En aprendizaje"
    },

    {
        "nombre": "Desarrollo Web",
        "nivel": "En aprendizaje"
    }

]


# ==========================================
# PÁGINA PRINCIPAL
# ==========================================

@app.route("/")
def portafolio():

    proyectos_python = [
        proyecto
        for proyecto in proyectos
        if proyecto["categoria"] == "Python"
    ]

    proyectos_web = [
        proyecto
        for proyecto in proyectos
        if proyecto["categoria"] == "Web"
    ]

    return render_template(
        "index.html",
        proyectos_python=proyectos_python,
        proyectos_web=proyectos_web,
        habilidades=habilidades
    )


# ==========================================
# PÁGINA INDIVIDUAL DEL PROYECTO
# ==========================================

@app.route("/proyecto/<proyecto_id>")
def proyecto(proyecto_id):

    proyecto_actual = next(
        (
            proyecto
            for proyecto in proyectos
            if proyecto["id"] == proyecto_id
        ),
        None
    )

    if proyecto_actual is None:
        abort(404)

    return render_template(
        "proyecto.html",
        proyecto=proyecto_actual
    )


# ==========================================
# EJECUTAR APLICACIÓN
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)