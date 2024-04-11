from database.studente_DAO import StudenteDAO
class Model:
    def __init__(self):
        self._id_map = {}

    def get_student_map(self):
        self._id_map = StudenteDAO.get_studenti_map(self._id_map)

