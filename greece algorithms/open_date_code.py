import pandas as pd

def date(date):
    data = [
    pd.read_excel(f"DATAENERGY\\GR-ALB\\GR-ALB{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY\\GR-BG\\GR-BG{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY\\GR-IT\\GR-IT{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY\\GR-MK\\GR-MK{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY\\GR-TR\\GR-TR{date[6:]}.xlsx",skiprows=[0,1,2,3,5])  
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
    sum_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    

    max=[0,0,0,0,0]

    ptrs = [total_list,list_al,list_bg,list_it,list_mk,list_tr,sum_list,max]

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

#--------------list_per_h----------

    algr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    gral = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    bggr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    grbg = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    itgr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    grit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    mkgr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    grmk = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    trgr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    grtr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    list_inc = [algr,bggr,itgr,mkgr,trgr]
    list_out = [gral,grbg,grit,grmk,grtr]

    
    
    for i in range (0,5):
        day_hours = 24
        index = save_index
        for j in inc_energy[i]:
            if index == -2 and day_hours >= 0 and j>=0:
                list_inc[i][24-day_hours] = j
                day_hours-=1
            else:
                index-=1

    for i in range (0,5):
        day_hours = 24
        index = save_index
        for j in out_energy[i]:
            if index == -2 and day_hours >= 0 and j>=0:
                list_out[i][24-day_hours] = j
                day_hours-=1
            else:
                index-=1
    
    
    for i in range (0,24):
        sum_list[0][i] = list_inc[0][i] + list_inc[1][i] + list_inc[2][i] + list_inc[3][i] + list_inc[4][i]
    
    for i in range (0,24):
        sum_list[1][i] = list_out[0][i] + list_out[1][i] + list_out[2][i] + list_out[3][i] + list_out[4][i]


    #find maximum energy

    for i in range(0,5):
        for j in list_inc[i]:
            if j>ptrs[7][i]:
                ptrs[7][i] = j
        for k in list_inc[i]:
            if k>ptrs[7][i]:
                ptrs[7][i] = k

    return ptrs

