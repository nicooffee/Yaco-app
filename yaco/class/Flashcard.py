from Palabra import Palabra
from RevisionList import RevisionList
import datetime
class Flashcard:
    def __init__(
            self,
            palabra,
            fecha_creacion = datetime.datetime.now(),
            nivel_srs = 1,
            revision_list_reco = RevisionList(),
            revision_list_prod = RevisionList()):
        self.palabra = palabra
        self.revision_list = revision_list
        self.fecha_creacion = fecha_creacion
        self.nivel_srs = nivel_srs