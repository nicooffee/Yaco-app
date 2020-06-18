from Usuario import Usuario

class Estudiante(Usuario):
    def __init__(
            self,
            nombre_usuario,
            flashcard_list = FlashcardList(),
            palabra_dict = PalabraDict(),
            fecha_registro = datetime.datetime.now(),
            ultimo_logeo = datetime.datetime.now(),
            tipo_estudiante,
            exp_total = 0):
        super().__init__(nombre_usuario,flashcard_list,palabra_dict,fecha_registro,ultimo_logeo)
        self.tipo_estudiante = tipo_estudiante
        self.exp_total = exp_total

    #GETTER###################################
    def get_tipo_estudiante(self):
        return self.tipo_estudiante
    def get_exp_total(self):
        return self.exp_total
    #SETTER###################################

    def set_tipo_estudiante(self,tipo_estudiante):
        self.tipo_estudiante = tipo_estudiante
    def set_exp_total(self,exp_total):
        self.exp_total = exp_total