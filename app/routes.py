from flask import Blueprint, render_template, request, redirect, url_for
from app.model.GestisDeTareas import GestorDeTareas

main_bp = Blueprint('main',__name__)
gestor = GestorDeTareas()

@main_bp.route('/')
def index():
    
    return render_template('index.html',title='Home',tareas=gestor.obtener_tareas())

@main_bp.route('/agregar', methods=['POST'])
def agregar_tarea():
    
    gestor.agregar_tarea(request.form['texto'])
    return redirect(url_for('main.index'))

@main_bp.route('/completar/<uuid:id>', methods=['POST'])
def completar_tarea(id):
    
    gestor.completar_tarea(id)
    return redirect(url_for('main.index'))
