import pandas as pd

def year_france(year):
    data = [
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_FR\\FR-BE\\FR-BE{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_FR\\FR-CH\\FR-CH{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_FR\\FR-DE\\FR-DE{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_FR\\FR-ES\\FR-ES{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_FR\\FR-IT\\FR-IT{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_FR\\FR-UK\\FR-UK{year}.xlsx",skiprows=[0,1,2,3,5]),
    ]
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


    for i in range(0,6):
        for j in inc_energy[i]:
            if j >= 0: 
                total_list[0] += j
    
    for i in range(0,6):
        for j in out_energy[i]:
            if j >= 0: 
                total_list[1] += j



    return total_list
