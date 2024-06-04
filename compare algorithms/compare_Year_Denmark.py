import pandas as pd

def year_denmark(year):
    data = [
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DK\\DK-DE\\DK-DE{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DK\\DK-NL\\DK-NL{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DK\\DK-NO\\DK-NO{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DK\\DK-SE\\DK-SE{year}.xlsx",skiprows=[0,1,2,3,5]),
    ]

    inc_energy = [
        data[0].DKDE,
        data[1].DKNL,
        data[2].DKNO,
        data[3].DKSE,
       
        ]
        
    out_energy = [
        data[0].DEDK,
        data[1].NLDK,
        data[2].NODK,
        data[3].SEDK,
        ]
    total_list = [0,0]


    for i in range(0,4):
        for j in inc_energy[i]:
            if j >= 0: 
                total_list[0] += j
    
    for i in range(0,4):
        for j in out_energy[i]:
            if j >= 0: 
                total_list[1] += j



    return total_list