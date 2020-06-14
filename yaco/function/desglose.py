import urllib.request
import json
import functools
import pprint
import os.path
import re
from parser import def_parser




#input: Diccionario
#output: JSON
def desglose(J):
    resultado = []
    for word in J:
        definicion_c = 1
        if "def" in word:
            for definicion in word["def"]:
                tipo = definicion["vd"] if "vd" in definicion else word["fl"]
                for sense in definicion["sseq"]:
                    sense = sense[0]
                    if sense[0] == 'sense':
                        sense_descrip = sense[1]
                        palabra = {}
                        palabra["id"] = word["meta"]["id"]+"-d{}".format(definicion_c)+"s{}".format(sense_descrip["sn"] if "sn" in sense_descrip else "")
                        palabra["tipo"] = tipo
                        palabra["definicion_eng"] = sense_descrip["vrs"][0]["va"] if "vrs" in sense_descrip else word["meta"]["stems"][0]
                        def_esp = functools.reduce(lambda x,y: x+y,map(lambda x: x[1],filter(lambda x: x[0]=="text",sense_descrip["dt"])),"")
                        if def_esp is not "":
                            palabra["definicion_esp"] = def_parser(def_esp)
                            palabra["es_ofensiva"] = word["meta"]["offensive"]
                            resultado.append(palabra)
                definicion_c += 1
    return json.dumps(resultado,indent=4)






if __name__ == "__main__":
    APIKEY = 'f9885f23-b685-4818-af4d-2f213fff9a91'
    palabra = "to%20go%20out"
    resp = urllib.request.urlopen("https://www.dictionaryapi.com/api/v3/references/spanish/json/"+palabra+"?key="+APIKEY).read()
    parsed = json.loads(resp)
    with open('resp.json','w') as file:
        file.write(desglose(parsed))





