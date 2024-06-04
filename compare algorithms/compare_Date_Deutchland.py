import pandas as pd

def date_deutchland(date):
    data = [
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-AT\\DE-AT{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-BE\\DE-BE{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-CH\\DE-CH{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-CZ\\DE-CZ{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-DK\\DE-DK{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-FR\\DE-FR{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-LU\\DE-LU{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-NL\\DE-NL{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-NO\\DE-NO{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-PL\\DE-PL{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_DE\\DE-SE\\DE-SE{date[6:]}.xlsx",skiprows=[0,1,2,3,5])
    ]
        
    timedata = [data[0].Time,data[1].Time,data[2].Time,data[3].Time,data[4].Time,data[5].Time,data[6].Time,data[7].Time,data[8].Time,data[9].Time,data[10].Time]
    timecheck=[timedata[0][2],timedata[1][2],timedata[2][2],timedata[3][2],timedata[4][2],timedata[5][2],timedata[6][2],timedata[7][2],timedata[8][2],timedata[9][2],timedata[10][2]]
    
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
   
    # 0-> lista[a8roisma eiserxomenwn energeiwn apo oles tis xwres,a8roisma e3erxomenwn energeiwn apo oles tis xwres,diafora twn 0 kai 1 se apolyth timh], 
    # 1-> lista[algr,gral,diafora twn 2], listai[..gr,gr..,diafora]

    

    fulldate=date[0:2]+"."+date[3:5]+"."+date[6:]

   
    
    outcoming_incoming=[0,0]
    for i in range(11):
        if timecheck[i]=="00:00 - 00:15":
            index=0
            for j in timedata[i]:
                if j == fulldate:
                    break
                else:
                    index=index+1

            save_index = index
            #-------for files that have 15 mins  counts--------------    
            total_list = [0]*96 #theindex=0 file that contains energy per 15 mins
            count15=0
            day_15 = 98
            index = save_index
            for j in inc_energy[i]:  
                if index == -2 and day_15 != 0 and j>=0:
                    total_list[count15] = j
                    day_15-=1
                    if count15<=94:
                        count15+=1
                else:
                    index-=1

            hour_File_incoming=[0]*24 #thew file that contains energy per hour
            start=0
            end=4
            for k in range(0,24):
                hour_File_incoming[k]=sum(total_list[start:end])
                start+=4
                end+=4
            
            outcoming_incoming[0]+=sum(hour_File_incoming)
            


        else:
            index=0
            for j in timedata[i]:
                if j == fulldate:
                    break
                else:
                    index=index+1

            save_index = index
            
            
            #-------for files that have hour counts--------------
            hour_File_incoming= [0]*24 #the file that contains energy per hour
            count15=0
            day_hour = 27
            index = save_index
            for j in inc_energy[i]:  
                if index == -2 and  day_hour != 0 and j>=0:
                    hour_File_incoming[count15] = j
                    day_hour-=1
                    if count15<=24:
                        count15+=1
                else:
                    index-=1
            
            outcoming_incoming[0]+=sum(hour_File_incoming)
    
            
    for i in range(11):
        
        #--------------FOR OUTCOMING ENERGY--------------------
        if timecheck[i]=="00:00 - 00:15":
            
            index=0
            for j in timedata[i]:
                if j == fulldate:
                    break
                else:
                    index=index+1
            save_index = index
            #-------for files that have 15 mins  counts--------------
            total_list = [0]*96 #the file that contains energy per 15 mins
            count15=0
            day_15 = 98
            index = save_index
           
            for k in out_energy[i]:  
                if index == -2 and day_15 != 0 and k>=0:
                    total_list[count15] = k
                    day_15-=1
                    if count15<=94:
                        count15+=1
                else:
                    index-=1
            
            hour_File_outcoming=[0]*24 #thew file that contains energy per hour
            start=0
            end=4
            for k in range(0,24):
                hour_File_outcoming[k]=sum(total_list[start:end])
                start+=4
                end+=4  
            
            outcoming_incoming[1]+=sum(hour_File_outcoming)
        else:
            
            index=0
            for j in timedata[i]:
                if j == fulldate:
                    break
                else:
                    index=index+1
            save_index=index
            #-------for files that have hour counts--------------
            hour_File_outcoming= [0]*24 #the file that contains energy per hour
            count15=0
            day_hour = 27
            index = save_index
            for j in out_energy[i]:  
                
                if index == -2 and  day_hour != 0 and j>=0:
                    hour_File_outcoming[count15] = j
                    day_hour-=1
                    if count15<=24:
                        count15+=1
                else:
                    index-=1
            
            outcoming_incoming[1]+=sum(hour_File_outcoming)
            
       
    return outcoming_incoming

