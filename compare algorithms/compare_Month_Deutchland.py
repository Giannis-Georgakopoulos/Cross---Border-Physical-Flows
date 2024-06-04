import pandas as pd

def month_deutchland(month,year):
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
    timedata = [data[0].Time,data[1].Time,data[2].Time,data[3].Time,data[4].Time,data[5].Time,data[6].Time,data[7].Time,data[8].Time,data[9].Time,data[10].Time]
    index_start = [0]*11
    index_end = [0]*11

    total_list = [0,0]

    mhden="0"
    if (month<=9):
        mhden = "0"+str(month)


    for i in range(0,11):

        for j in timedata[i]:
            if j == f"01.{mhden}.{year}":
                break
            else:
                index_start[i] += 1
        #mhden="0"
    month=month+1

    if (month<=9):
        mhden = "0"+str(month)

    for i in range(0,11):
        for j in timedata[i]:
            if j == f"01.{mhden}.{year}":
                break
            else:
                index_end[i] += 1

    save_index_start = [0]*11

    for i in range(0,11):
        index_start[i] = save_index_start[i]
        for j in out_energy[i]:
            if(index_start[i]!=index_end[i]):
                if j>0:
                    total_list[1]+=j
                    index_start[i]+=1
                else:
                    index_start[i]+=1

    index_start = save_index_start

    for i in range(0,11):
        for j in inc_energy[i]:
            if(save_index_start[i]!=index_end[i]):
                if j>0:
                    total_list[0]+=j
                    save_index_start[i]+=1
                else:
                    save_index_start[i]+=1
    



    return total_list

