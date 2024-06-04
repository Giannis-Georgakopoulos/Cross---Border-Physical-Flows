import pandas as pd

def year_deutchland(year):
    data = [
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-AT\\DE-AT{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-BE\\DE-BE{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-CH\\DE-CH{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-CZ\\DE-CZ{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-DK\\DE-DK{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-FR\\DE-FR{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-LU\\DE-LU{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-NL\\DE-NL{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-NO\\DE-NO{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-PL\\DE-PL{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-SE\\DE-SE{year}.xlsx",skiprows=[0,1,2,3,5])
    ] 

    out_energy = [
        data[0].DEAT,
        data[1].DEBE,
        data[2].DECH,
        data[3].DECZ,
        data[4].DEDK,
        data[5].DEFR,
        data[6].DELU,
        data[7].DENL,
        data[8].DENO,
        data[9].DEPL,
        data[10].DESE
        ]
        
    inc_energy = [
        data[0].ATDE,
        data[1].BEDE,
        data[2].CHDE,
        data[3].CZDE,
        data[4].DKDE,
        data[5].FRDE,
        data[6].LUDE,
        data[7].NLDE,
        data[8].NODE,
        data[9].PLDE,
        data[10].SEDE
        ]
    total_list = [0,0]


    for i in range(0,11):
        for j in inc_energy[i]:
            if j >= 0: 
                total_list[0] += j
    
    for i in range(0,11):
        for j in out_energy[i]:
            if j >= 0: 
                total_list[1] += j



    return total_list