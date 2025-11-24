import uuid
import json

class GestorDeTareas:
    def __init__(self):
        self.cargar_tareas()

    def cargar_tareas(self):
        try:
            with open('database/tareas.json', 'r') as archivo:
                self.tareas = json.load(archivo)
        except FileNotFoundError:
            self.tareas = []

    def guardar_tareas(self):
        with open('database/tareas.json', 'w') as archivo:
            json.dump(self.tareas, archivo)

    def agregar_tarea(self, texto):
        tarea = {
            'id': str(uuid.uuid4()),
            'texto': texto,
            'completada': False
        }
        self.tareas.append(tarea)
        self.guardar_tareas()
        return tarea

    def completar_tarea(self, tarea_id):
        for tarea in self.tareas:
            if tarea['id'] == tarea_id:
                tarea['completada'] = not tarea['completada']

                self.guardar_tareas()
                return True
        return False

    def obtener_tareas(self):
        
        return self.tareas
