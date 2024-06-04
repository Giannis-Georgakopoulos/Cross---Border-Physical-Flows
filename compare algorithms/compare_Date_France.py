import pandas as pd

def date_france(date):
    data = [
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_FR\\FR-BE\\FR-BE{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_FR\\FR-CH\\FR-CH{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_FR\\FR-DE\\FR-DE{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_FR\\FR-ES\\FR-ES{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_FR\\FR-IT\\FR-IT{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    pd.read_excel(f"DATAENERGY_2\\DATAENERGY_FR\\FR-UK\\FR-UK{date[6:]}.xlsx",skiprows=[0,1,2,3,5]),
    ]
        
    timedata = [data[0].Time,data[1].Time,data[2].Time,data[3].Time,data[4].Time,data[5].Time]
    timecheck=[timedata[0][2],timedata[1][2],timedata[2][2],timedata[3][2],timedata[4][2],timedata[5][2]]
    
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

    # 0-> lista[a8roisma eiserxomenwn energeiwn apo oles tis xwres,a8roisma e3erxomenwn energeiwn apo oles tis xwres,diafora twn 0 kai 1 se apolyth timh], 
    # 1-> lista[algr,gral,diafora twn 2], listai[..gr,gr..,diafora]
   
    fulldate=date[0:2]+"."+date[3:5]+"."+date[6:]

   
    
    outcoming_incoming=[0,0]
    for i in range(6):
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
                if index == -2 and  day_hour != 0 and float(j)>=0:
                    hour_File_incoming[count15] = j
                    day_hour-=1
                    if count15<=24:
                        count15+=1
                else:
                    index-=1
            
            outcoming_incoming[0]+=sum(hour_File_incoming)
    
            
    for i in range(6):
        
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


