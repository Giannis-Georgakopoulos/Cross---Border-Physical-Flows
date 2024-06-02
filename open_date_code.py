import pandas as pd

def date(date):
    data = [
    pd.read_excel(f"DATA ENERGY\\DATAENERGY\\GR-ALB\\GR-ALB{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATA ENERGY\\DATAENERGY\\GR-BG\\GR-BG{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATA ENERGY\\DATAENERGY\\GR-IT\\GR-IT{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATA ENERGY\\DATAENERGY\\GR-MK\\GR-MK{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATA ENERGY\\DATAENERGY\\GR-TR\\GR-TR{date[6:]}.xlsx",skiprows=[0,1,2,3,5])  
    ]
        
    time = data[0].Time
        
    inc_energy = [
        data[0].ALGR,
        data[1].BGGR,
        data[2].ITGR,
        data[3].MKGR,
        data[4].TRGR 
        ]
        
    out_energy = [
        data[0].GRAL,
        data[1].GRBG,
        data[2].GRIT,
        data[3].GRMK,
        data[4].GRTR 
        ]

    # 0-> lista[a8roisma eiserxomenwn energeiwn apo oles tis xwres,a8roisma e3erxomenwn energeiwn apo oles tis xwres,diafora twn 0 kai 1 se apolyth timh], 
    # 1-> lista[algr,gral,diafora twn 2], listai[..gr,gr..,diafora]
        
    total_list = [0,0,0]
    list_al = [0,0,0]
    list_bg = [0,0,0]
    list_it = [0,0,0]
    list_mk = [0,0,0]
    list_tr = [0,0,0]
        
    ptrs = [total_list,list_al,list_bg,list_it,list_mk,list_tr]

    index=0

    fulldate=date[0:2]+"."+date[3:5]+"."+date[6:]

    for i in time:
        if i == fulldate:
            break
        else:
            index=index+1

    save_index = index    
    for i in range(0,5):
        day_hours = 24
        index = save_index
        for j in inc_energy[i]:
            if index == -2 and day_hours != 0 and j>0:
                total_list[0] += j
                day_hours-=1
            else:
                index-=1
                


    for i in range(0,5):
        day_hours = 24
        index = save_index
        for j in out_energy[i]:
            if index == -2 and day_hours != 0:
                total_list[1] += j
                day_hours-=1
            else:
                index-=1

    total_list[2] = total_list[1] - total_list[0]
    for i in range(0,5):
        day_hours = 24
        index = save_index
        for j in inc_energy[i]:
            if index == -2 and day_hours != 0 and j>0:
                ptrs[i+1][0] += j
                day_hours-=1
            else:
                index-=1

    for i in range(0,5):
        day_hours = 24
        index = save_index
        for j in out_energy[i]:
            if index == -2 and day_hours != 0:
                ptrs[i+1][1] += j
                day_hours-=1
            else:
                index-=1

    for i in range(0,5):
        ptrs[i+1][2] = ptrs[i+1][1] - ptrs[i+1][0]

    return ptrs
