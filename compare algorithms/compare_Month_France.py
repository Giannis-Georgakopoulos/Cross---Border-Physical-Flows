import pandas as pd

def month_france(month,year):
    data = [
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_FR\\FR-BE\\FR-BE{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_FR\\FR-CH\\FR-CH{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_FR\\FR-DE\\FR-DE{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_FR\\FR-ES\\FR-ES{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_FR\\FR-IT\\FR-IT{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_FR\\FR-UK\\FR-UK{year}.xlsx",skiprows=[0,1,2,3,5]),
    ]

    timedata = [data[0].Time,data[1].Time,data[2].Time,data[3].Time,data[4].Time,data[5].Time]

    inc_energy = [
        data[0].FRBE,
        data[1].FRCH,
        data[2].FRDE,
        data[3].FRES,
        data[4].FRIT,
        data[5].FRUK,
        ]
        
    out_energy = [
        data[0].BEFR,
        data[1].CHFR,
        data[2].DEFR,
        data[3].ESFR,
        data[4].ITFR,
        data[5].UKFR,
        ]
    
    total_list = [0,0]

    index_start = [0,0,0,0,0,0]
    index_end = [0,0,0,0,0,0]

    mhden="0"
    if (month<=9):
        mhden = "0"+str(month)


    for i in range(0,6):

        for j in timedata[i]:
            if j == f"01.{mhden}.{year}":
                break
            else:
                index_start[i] += 1
        #mhden="0"
    month=month+1

    if (month<=9):
        mhden = "0"+str(month)

    for i in range(0,6):
        for j in timedata[i]:
            if j == f"01.{mhden}.{year}":
                break
            else:
                index_end[i] += 1

    save_index_start = [0,0,0,0,0,0]

    for i in range(0,6):
        index_start[i] = save_index_start[i]
        for j in out_energy[i]:
            if(index_start[i]!=index_end[i]):
                if j>0:
                    total_list[1]+=j
                    index_start[i]+=1
                else:
                    index_start[i]+=1

    index_start = save_index_start

    for i in range(0,6):
        for j in inc_energy[i]:
            if(save_index_start[i]!=index_end[i]):
                if j>0:
                    total_list[0]+=j
                    save_index_start[i]+=1
                else:
                    save_index_start[i]+=1
    


    

    return total_list

