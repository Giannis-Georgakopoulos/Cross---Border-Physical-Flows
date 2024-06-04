import pandas as pd

def month(month,year):
    data = [
    pd.read_excel(f"DATAENERGY\\GR-ALB\\GR-ALB{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY\\GR-BG\\GR-BG{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY\\GR-IT\\GR-IT{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY\\GR-MK\\GR-MK{year}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY\\GR-TR\\GR-TR{year}.xlsx",skiprows=[0,1,2,3,5])  
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
    
    max = [0,0,0,0,0]
    
    ptrs = [total_list,list_al,list_bg,list_it,list_mk,list_tr,max]

    index_start = 0
    index_end = 0

    mhden="0"
    if (month<=9):
        mhden = "0"+str(month)



    for j in time:
        if j == f"01.{mhden}.{year}":
            break
        else:
            index_start += 1
    mhden="0"
    month=month+1
    if (month<=9):
        mhden = "0"+str(month)

    for j in time:
        if j == f"01.{mhden}.{year}":
            break
        else:
            index_end += 1
            
    save_index_start = index_start
   
    

    for i in range(0,5):
        index_start = save_index_start 
        mult = 1
        while(index_start != index_end):
            day_hours = 24
            
            for j in inc_energy[i]:
                if j>=0:
                    if index_start == -2 and day_hours != 0:
                        total_list[0] += j
                        day_hours -= 1
                    else:
                        index_start -= 1
            index_start = (save_index_start + 27 * mult)
            mult += 1
     
     
 
    for i in range(0,5):
        index_start = save_index_start 
        mult = 1
        while(index_start != index_end):
            day_hours=24
            
            for j in out_energy[i]:
                if j >= 0:
                    if index_start == -2 and day_hours != 0:
                        total_list[1] += j
                        day_hours -= 1
                    else:
                        index_start -= 1
            index_start = (save_index_start + 27 * mult)
            mult+=1
            
    
    total_list[2] = total_list[1] - total_list[0]


    for i in range(0,5):
        index_start = save_index_start 
        mult = 1 
        while(index_start != index_end):
            day_hours = 24
            
            for j in inc_energy[i]:
                if j >= 0:
                    if index_start == -2 and day_hours !=0:
                        ptrs[i+1][0] += j
                        day_hours -= 1
                    else:
                        index_start -= 1
            index_start= (save_index_start + 27 * mult)
            mult += 1
         
    for i in range(0,5):
        index_start = save_index_start 
        mult = 1 
        while(index_start != index_end):
            day_hours = 24
            
            for j in out_energy[i]:
                if j >= 0:
                    if index_start == -2 and day_hours != 0:
                        ptrs[i+1][1] += j
                        day_hours -= 1
                    else:
                        index_start-=1
            index_start= (save_index_start + 27 * mult)
            mult += 1
    
    for i in range(1,6):
        ptrs[i][2] = ptrs[i][1] - ptrs[i][0]

#finding maximum energy
    for i in range(0,5):
        index_start = save_index_start 
        mult = 1 
        while(index_start != index_end):
            day_hours = 24
            
            for j in out_energy[i]:
                if j >= 0:
                    if index_start == -2 and day_hours != 0:
                        if j>ptrs[6][i]:
                            ptrs[6][i] = j
                        day_hours -= 1
                    else:
                        index_start-=1
            index_start= (save_index_start + 27 * mult)
            mult += 1


    for i in range(0,5):
        index_start = save_index_start 
        mult = 1 
        while(index_start != index_end):
            day_hours = 24
            
            for j in inc_energy[i]:
                if j >= 0:
                    if index_start == -2 and day_hours != 0:
                        if j>ptrs[6][i]:
                            ptrs[6][i] = j
                        day_hours -= 1
                    else:
                        index_start-=1
            index_start= (save_index_start + 27 * mult)
            mult += 1

    return ptrs
