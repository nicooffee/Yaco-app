import json
import functools
import pprint
import os.path
import re
try:
    from . import Parser
except ImportError:
    import Parser



#input: Diccionario
#output: JSON
def desglose(J):
    resultado = []
    for word in J:
        definicion_c = 1
        if "def" in word and word["meta"]["lang"] == "en":
            for definicion in word["def"]:
                tipo = definicion["vd"] if "vd" in definicion else word["fl"]
                for sense in definicion["sseq"]:
                    sense = sense[0]
                    if sense[0] == 'sense':
                        sense_descrip = sense[1]
                        palabra = {}
                        palabra["id"] = word["meta"]["id"]+"-d{}".format(definicion_c)+"s{}".format(sense_descrip["sn"] if "sn" in sense_descrip else "")
                        palabra["tipo"] = tipo
                        palabra["definicion_eng"] = [[sense_descrip["vrs"][0]["va"] if "vrs" in sense_descrip else word["meta"]["stems"][0],""]]
                        def_esp = functools.reduce(lambda x,y: x+y,map(lambda x: x[1],filter(lambda x: x[0]=="text",sense_descrip["dt"])),"")
                        if def_esp is not "":
                            palabra["definicion_esp"] = Parser.def_parser(def_esp)
                            palabra["es_ofensiva"] = word["meta"]["offensive"]
                            resultado.append(palabra)
                definicion_c += 1
    return json.dumps(resultado,indent=4)






if __name__ == "__main__":
    import GetWord
    palabra = "aceptar"
    parsed = GetWord.get_word(palabra)
    with open('resp.json','w') as file:
        file.write(desglose(parsed))





