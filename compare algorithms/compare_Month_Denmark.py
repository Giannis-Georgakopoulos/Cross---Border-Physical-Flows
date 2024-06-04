import pandas as pd

def month_denmark(month,year):
    data = [
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DK\\DK-DE\\DK-DE{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DK\\DK-NL\\DK-NL{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DK\\DK-NO\\DK-NO{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DK\\DK-SE\\DK-SE{year}.xlsx",skiprows=[0,1,2,3,5]),
    ]

    timedata = [data[0].Time,data[1].Time,data[2].Time,data[3].Time,]

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

    index_start = [0,0,0,0]
    index_end = [0,0,0,0]

    mhden="0"
    if (month<=9):
        mhden = "0"+str(month)


    for i in range(0,4):

        for j in timedata[i]:
            if j == f"01.{mhden}.{year}":
                break
            else:
                index_start[i] += 1
        #mhden="0"
    month=month+1

    if (month<=9):
        mhden = "0"+str(month)

    for i in range(0,4):
        for j in timedata[i]:
            if j == f"01.{mhden}.{year}":
                break
            else:
                index_end[i] += 1

    save_index_start = [0,0,0,0]

    for i in range(0,4):
        index_start[i] = save_index_start[i]
        for j in out_energy[i]:
            if(index_start[i]!=index_end[i]):
                if j>0:
                    total_list[1]+=j
                    index_start[i]+=1
                else:
                    index_start[i]+=1

    index_start = save_index_start

    for i in range(0,4):
        for j in inc_energy[i]:
            if(save_index_start[i]!=index_end[i]):
                if j>0:
                    total_list[0]+=j
                    save_index_start[i]+=1
                else:
                    save_index_start[i]+=1
    


    return total_list
    

