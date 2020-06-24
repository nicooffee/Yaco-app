import json
from datetime import datetime,timedelta

SRS_TIME_L1 = 14400
SRS_TIME_L2 = 28800
SRS_TIME_L3 = 82800
SRS_TIME_L4 = 252000
SRS_TIME_L5 = 601200
SRS_TIME_L6 = 1206000
SRS_TIME_L7 = 2415600
SRS_TIME_L8 = 9673200

def get_srs_time(srs_lvl):
    if srs_lvl == 1:
        return SRS_TIME_L1
    elif srs_lvl == 2:
        return SRS_TIME_L2
    elif srs_lvl == 3:
        return SRS_TIME_L3
    elif srs_lvl == 4:
        return SRS_TIME_L4
    elif srs_lvl == 5:
        return SRS_TIME_L5
    elif srs_lvl == 6:
        return SRS_TIME_L6
    elif srs_lvl == 7:
        return SRS_TIME_L7
    elif srs_lvl == 8:
        return SRS_TIME_L8
    else:
        raise Exception("El nivel srs es incorrecto")
if __name__ == "__main__":
    fecha_leccion = datetime(2020,6,23,8,00,00)
    srs_l = [SRS_TIME_L1,SRS_TIME_L2,SRS_TIME_L3,SRS_TIME_L4,SRS_TIME_L5,SRS_TIME_L6,SRS_TIME_L7,SRS_TIME_L8]
    for i in range(1,9):
        fecha_leccion = fecha_leccion+timedelta(seconds=srs_l[i-1])
        print("SRS"+str(i)+": "+str(fecha_leccion))