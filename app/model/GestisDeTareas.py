import uuid

class GestorDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, texto):
        tarea = {
            'id': uuid.uuid4(),
            'texto': texto,
            'completada': False
        }
        self.tareas.append(tarea)
        return tarea

    def completar_tarea(self, tarea_id):
        for tarea in self.tareas:
            if tarea['id'] == tarea_id:
                tarea['completada'] = True
                return True
        return False

    def obtener_tareas(self):
        return self.tareas
