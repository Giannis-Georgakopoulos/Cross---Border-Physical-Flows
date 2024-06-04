from PIL import Image
Image.CUBIC = Image.BICUBIC
import ttkbootstrap as ttk
import datetime
from tkinter import *
from tkinter import messagebox

from open_date_code import date
from open_month_code import month
from open_year_code import year

from compare_Date_Denmark import date_denmark
from compare_Date_France import date_france
from compare_Date_Deutchland import date_deutchland

from compare_Month_Denmark import month_denmark
from compare_Month_France import month_france
from compare_Month_Deutchland import month_deutchland

from compare_Year_Denmark import year_denmark
from compare_Year_France import year_france
from compare_Year_Deutchland import year_deutchland

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def appopen():
    #window setup
    window=ttk.Window(title="Cross-Border Physical Flow (GR)",themename="sandstone",position=(500,170))
    window.geometry("900x600")
    window.resizable(False,False)
    icon = PhotoImage(file='logo.png')
    window.iconphoto(True,icon)
    
    #title and choose period labels
    title = ttk.Label(window, text="Cross-Border Physical Flow (Greece)",font=("Helvetica",15), bootstyle="inverse-light")
    title.pack(side="top",pady=40)
    labelperiod = ttk.Label(window, text="Choose time period:",font=("Helvetica",14), bootstyle="dark")
    labelperiod.pack(side="top",pady=(30,40))

    #buttons placement
    b1 = ttk.Button(window, text="Choose Date", bootstyle="outline-dark", width=20, command=lambda: opendate(window))
    b1.pack(side="top")

    b2 = ttk.Button(window, text="Choose Month", bootstyle="outline-dark", width=20, command=lambda: openmonth(window))
    b2.pack(side="top", pady=25)

    b3 = ttk.Button(window, text="Choose Year", bootstyle="outline-dark", width=20, command=lambda: openyear(window))
    b3.pack(side="top")
    
    window.mainloop()

def opendate(window):
    def datedata():   
        listofyears=["2023","2022","2021","2020"]
        date_string=dateentry.entry.get()       
        date_ptrs=date(date_string)
        rootdate=ttk.Toplevel(window3)
            
        rootdate.state("zoomed")
        rootdate.resizable(False,False)
        icon = PhotoImage(file='logo.png')
        rootdate.iconphoto(True,icon)
        rootdate.title(date_string + " Data") 
        rootdate.columnconfigure((0,1,2,3,4,5,6,7),weight=1)
        rootdate.rowconfigure((0,1,2,3,4),weight=1)
        totalframe=ttk.Labelframe(rootdate,style="darkly",text="Total Incoming-Outcoming Energy (Greece)",borderwidth=10)
        totalframe.grid(column=0,row=0,columnspan=4,rowspan=2,sticky="nw",padx=60,pady=(30,0))

        meterstats_incoming = ttk.Meter(
            totalframe,
            bootstyle="success",
            arcrange=180,
            arcoffset=180,
            amounttotal=80000,
            amountused=int(date_ptrs[0][0]),
            meterthickness=9,
            metersize=200,
            interactive=False,     
            metertype="semi",
            stepsize=40,
            stripethickness=0,
            textfont="Arial 13",
            subtext="Total Incoming(MWh)",
            subtextfont="Arial 9",
        )
        meterstats_incoming.grid(row=0,column=0,padx=25,pady=(25,0))
        meterstats_outcoming = ttk.Meter(
            totalframe,
            bootstyle="warning",
            arcrange=180,
            arcoffset=180,
            amounttotal=80000,
            amountused=int(date_ptrs[0][1]),
            meterthickness=9,
            metersize=200,
            interactive=False,     
            metertype="semi",
            stepsize=40,
            stripethickness=0,
            textfont="Arial 13",
            subtext="Total Outcoming(MWh)",
            subtextfont="Arial 9",
        )
        x=0
        if date_ptrs[0][2]>=0:
            x = 80000
        else: 
            x=-80000

        meterstats_outcoming.grid(row=0,column=1,padx=25,pady=(25,0))
        meterstats_difference = ttk.Meter(
            totalframe,
            bootstyle="danger",
            arcrange=180,
            arcoffset=180,
            amounttotal=x,
            amountused=(int(date_ptrs[0][2])),
            meterthickness=9,
            metersize=200,
            interactive=False,     
            metertype="semi",
            stepsize=40,
            stripethickness=0,
            textfont="Arial 13",
            subtext="Net Position (MWh)",
            subtextfont="Arial 9",
        )
        meterstats_difference.grid(row=0,column=2,padx=25,pady=(25,0))


        plt.rcParams["axes.prop_cycle"] = plt.cycler(color =["#a3eff0" ,"#dac27c" ,"#a3c8f0", "#a3ddf0", "#a3c8f0"])
        fig1, ax1 = plt.subplots()
        ax1.bar(["ALB","BG","IT","MK","TR"],[date_ptrs[1][0]/1000, date_ptrs[2][0]/1000, date_ptrs[3][0]/1000, date_ptrs[4][0]/1000, date_ptrs[5][0]/1000 ])
        ax1.set_xlabel("Countries")
        ax1.set_ylabel("Incoming Energy (MWh)x1000")
        fig1.set_figheight(4)
        fig1.set_figwidth(5)
        fig2, ax2 = plt.subplots()
        ax2.bar(["ALB","BG","IT","MK","TR"],[ date_ptrs[1][1]/1000, date_ptrs[2][1]/1000, date_ptrs[3][1]/1000, date_ptrs[4][1]/1000, date_ptrs[5][1]/1000 ])
        ax2.set_xlabel("Countries")
        ax2.set_ylabel("Outcoming Energy (MWh)x1000")
        fig2.set_figheight(4)
        fig2.set_figwidth(5)
        
        



        canvas1 = FigureCanvasTkAgg(fig1,rootdate)
        canvas1.draw()
        canvas1.get_tk_widget().grid(rowspan=3,columnspan=3,row=3,column=0,sticky="nwes")
        canvas2 = FigureCanvasTkAgg(fig2,rootdate)
        canvas2.draw()
        canvas2.get_tk_widget().grid(rowspan=3,columnspan=3,row=3,column=3,sticky="nesw")
        def open_profil():
            root_dateprof = ttk.Toplevel(rootdate)
            root_dateprof.geometry("1500x700")
            root_dateprof.resizable(False, False)
            icon = ttk.PhotoImage(file='logo.png')
            root_dateprof.iconphoto(True, icon)
            root_dateprof.title(date_string + " Profils")
            
            frame = ttk.Frame(root_dateprof)
            frame.pack(expand=1, fill="both")

            fig, ax = plt.subplots()  # Creating a single subplot
            
            list_of_x = [
                '01:00', '02:00', '03:00',
                '04:00', '05:00', '06:00', '07:00',
                '08:00', '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00', '15:00',
                '16:00', '17:00', '18:00', '19:00',
                '20:00', '21:00', '22:00', '23:00','24:00'
            ]
            
            y1 = date_ptrs[6][0]  # Extract y1 data
            y2 = date_ptrs[6][1]  # Extract y2 data
            
            ax.plot(list_of_x, y1, label='Total incoming energy (MW)', color='b', marker='o')
            ax.plot(list_of_x, y2, label='Total outgoing energy (MW)', color='r', marker='s')
            
            ax.set_title('Energy Profile')
            ax.set_xlabel('Time (Hours)')
            ax.set_ylabel('Energy (MW)')
            
            ax.legend()
            
            fig.set_figheight(6)  # Adjust figure height
            fig.set_figwidth(8)   # Adjust figure width
            
            canvas = FigureCanvasTkAgg(fig, frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side="top", fill="both", expand=1)

        def open_max_stats():
            root_max = ttk.Toplevel(rootdate)
            root_max.geometry("500x500")
            root_max.resizable(False, False)
            icon = ttk.PhotoImage(file='logo.png')
            root_max.iconphoto(True, icon)
            root_max.title(date_string + " Maximum Energy Exchange")

            plt.rcParams["axes.prop_cycle"] = plt.cycler(color =["#a3eff0" ,"#dac27c" ,"#a3c8f0", "#a3ddf0", "#a3c8f0"])
            fig6, ax6 = plt.subplots()
            ax6.bar(["ALB","BG","IT","MK","TR"],[date_ptrs[7][0], date_ptrs[7][1], date_ptrs[7][2], date_ptrs[7][3], date_ptrs[7][4]])
            ax6.set_xlabel("Countries")
            ax6.set_ylabel("Maximum Energy Exchange (MWh)")
            fig6.set_figheight(4)
            fig6.set_figwidth(5)
            canvas6 = FigureCanvasTkAgg(fig6, root_max)
            canvas6.draw()
            canvas6.get_tk_widget().pack(side="top", fill="both", expand=1)


        profil_button=ttk.Button(rootdate,text="Open Profile window",width=20,padding=20,style="outline-dark",command=open_profil)
        profil_button.grid(row=0,column=5,rowspan=2,padx=(20,270),pady=35)
        
        max_button=ttk.Button(rootdate,text="Open maximum Stats",width=20,padding=20,style="outline-dark",command=open_max_stats)
        max_button.grid(row=1,column=5,rowspan=2,padx=(20,270),pady=35)
        
    

    #window setup
    window.iconify()
    window3=ttk.Toplevel(title="Cross-Border Physical Flow (GR)",position=(500,170))
    window3.geometry("900x650")
    window3.resizable(False,False)
    icon = PhotoImage(file='logo.png')
    window3.iconphoto(True,icon)
    
    #title and choose period labels
    title = ttk.Label(window3, text="Cross-Border Physical Flow (Greece)",font=("Helvetica",15), bootstyle="inverse-light")
    title.pack(side="top",pady=40)
    labelperiod = ttk.Label(window3, text="Choose Date:",font=("Helvetica",14), bootstyle="inverse-light")
    labelperiod.pack(side="top",pady=40)
    startingdate = datetime.datetime(2023, 1, 1)
    #buttons placement
    dateentry=ttk.DateEntry(window3,bootstyle="Dark",startdate=startingdate)
    dateentry.pack()

    
    def confirmdate():
        check = 0 
        datechose = dateentry.entry.get()
        chosenyear = datetime.datetime.strptime(datechose, '%d/%m/%Y').year
        today = datetime.date.today()
        if chosenyear < 2022 or chosenyear > 2023 or datetime.datetime.strptime(datechose, '%d/%m/%Y').date() > today:
            messagebox.showerror("Error", "Please enter a valid date (between 2022-2023)")
            check = 1
        if check == 0:
            datedata() 
        
    labelperiod = ttk.Label(window3, text="*(between 2022-2023)",font=("Helvetica",11), bootstyle="darkly")
    labelperiod.pack(side="top",pady=5)

    bconfirm = ttk.Button(window3,text= "Confirm Date",bootstyle="outline-dark",width=20,command=confirmdate)
    bconfirm.pack(side="top",pady=20)
    #--------------------------------------------Compare------------------------------------------------------------
    line=ttk.Separator(window3,style="darkly")
    line.pack(fill="x",pady=(10,0),padx=70)
    
    titlecompare=ttk.Label(window3,text="Compare Section",font="Arial 15",style="inverse-light")
    titlecompare.pack(pady=(30,15))
    
    list_countries=["Germany","France","Denmark"]
    countries_Combo=ttk.Combobox(window3,bootstyle="Dark",values=list_countries,state="readonly")
    countries_Combo.pack(pady=15)
    countries_Combo.set("Choose Country")

    def open_compare():
        listofyears=["2023","2022"]
        country = countries_Combo.get()
        date_string = dateentry.entry.get()
        chosenyear = datetime.datetime.strptime(date_string, '%d/%m/%Y').year
        today = datetime.date.today()
        country = countries_Combo.get()
        if chosenyear < 2022 or chosenyear > 2023 or datetime.datetime.strptime(date_string, '%d/%m/%Y').date() > today:
            messagebox.showerror("Error", "Please enter a valid date (between 2022-2023)")
        elif country not in list_countries:
            messagebox.showerror("Error","No valid country has been selected.\nPlease enter valid country.")
        else:
            date_string=dateentry.entry.get()       
            root_compare_date=ttk.Toplevel(window3)
                
            root_compare_date.state("zoomed")
            root_compare_date.resizable(False,False)
            icon = PhotoImage(file='logo.png')
            root_compare_date.iconphoto(True,icon)
            root_compare_date.title(date_string + " Data"+f"Compare with {country}")

            #dedomena poy theloume
            date_ptrs_gr=date(date_string) #mono to [0][0] kai [0][1] 
            
            if(country == "Germany"):
                date_ptrs_cmp = date_deutchland(date_string)
            elif(country == "France"):
                date_ptrs_cmp = date_france(date_string)
            elif(country == "Denmark"):
                date_ptrs_cmp = date_denmark(date_string)

            plt.rcParams["axes.prop_cycle"] = plt.cycler(color =["#a3eff0" ,"#a3ddf0" ,"#a3c8f0", "#a3bdf0", "#aca3f0"])
            fig1, ax1 = plt.subplots()
            ax1.bar(["Greece",f"{country}"],[date_ptrs_gr[0][0]/10000,date_ptrs_cmp[0]/10000 ])
            ax1.set_xlabel("Countries")
            ax1.set_ylabel("Total Incoming Energy (MWh)x10000")
            fig1.set_figheight(4)
            fig1.set_figwidth(5)
            fig2, ax2 = plt.subplots()
            ax2.bar(["Greece",f"{country}"],[date_ptrs_gr[0][1]/10000,date_ptrs_cmp[1]/10000 ])
            ax2.set_xlabel("Countries")
            ax2.set_ylabel("Total Outcoming Energy (MWh)x10000")
            fig2.set_figheight(4)
            fig2.set_figwidth(5)
            
            canvas1 = FigureCanvasTkAgg(fig1,root_compare_date)
            canvas1.draw()
            canvas1.get_tk_widget().pack(side="top", fill="both", expand=1)
            canvas2 = FigureCanvasTkAgg(fig2,root_compare_date)
            canvas2.draw()
            canvas2.get_tk_widget().pack(side="top", fill="both", expand=1)
    
    bcompare= ttk.Button(window3,text= "Compare (For selected Date)",bootstyle="outline-dark",width=25,command=open_compare)
    bcompare.pack(pady=15)

    window3.mainloop()

def openmonth(window):
    def monthdata():    
        listofyears=["2023","2022","2021","2020"]
        month_string=combobox_month.get()
        year_string=combobox_year.get()
        
        if (month_string not in listmonths):
            messagebox.showerror("Error","No valid month has been selected.\nPlease enter valid month.")
        elif year_string not in listyears:
            messagebox.showerror("Error","No valid year has been selected.\nPlease enter valid year.")
        else:
            month_ptrs=month(dict_months[month_string],year_string)
            rootmonth=ttk.Toplevel(window2)
            
            rootmonth.state("zoomed")
            rootmonth.resizable(False,False)
            icon = PhotoImage(file='logo.png')
            rootmonth.iconphoto(True,icon)
            rootmonth.title(month_string + " " + year_string + " Data")
            rootmonth.columnconfigure((0,1,2,3,4,5,6,7),weight=1)
            rootmonth.rowconfigure((0,1,2,3,4,5),weight=1)
            totalframe=ttk.Labelframe(rootmonth,style="darkly",text="Total Incoming-Outcoming Energy (Greece)",borderwidth=3)
            totalframe.grid(column=0,row=0,columnspan=4,rowspan=2,sticky="nw",padx=60,pady=(30,0))

            meterstats_incoming = ttk.Meter(
                totalframe,
                bootstyle="success",
                arcrange=180,
                arcoffset=180,
                amounttotal=1500000,
                amountused=int(month_ptrs[0][0]),
                meterthickness=9,
                metersize=200,
                interactive=False,     
                metertype="semi",
                stepsize=40,
                stripethickness=0,
                textfont="Arial 13",
                subtext="Total Incoming(MWh)",
                subtextfont="Arial 9",
            )
            meterstats_incoming.grid(row=0,column=0,padx=25,pady=(50,0))
            meterstats_outcoming = ttk.Meter(
                totalframe,
                bootstyle="warning",
                arcrange=180,
                arcoffset=180,
                amounttotal=1500000,
                amountused=int(month_ptrs[0][1]),
                meterthickness=9,
                metersize=200,
                interactive=False,     
                metertype="semi",
                stepsize=40,
                stripethickness=0,
                textfont="Arial 13",
                subtext="Total Outcoming(MWh)",
                subtextfont="Arial 9",
            )
            x=0
            if month_ptrs[0][2]>=0:
                x = 1500000
            else: 
                x=-1500000
            
            meterstats_outcoming.grid(row=0,column=1,padx=25,pady=(50,0))
            meterstats_difference = ttk.Meter(
                totalframe,
                bootstyle="danger",
                arcrange=180,
                arcoffset=180,
                amounttotal=x,
                amountused=int(month_ptrs[0][2]),
                meterthickness=9,
                metersize=200,
                interactive=False,     
                metertype="semi",
                stepsize=40,
                stripethickness=0,
                textfont="Arial 13",
                subtext="Net Position(MWh)",
                subtextfont="Arial 9",
            )
            meterstats_difference.grid(row=0,column=2,padx=25,pady=(50,0))

            plt.rcParams["axes.prop_cycle"] = plt.cycler(color =["#a3eff0" ,"#a3ddf0" ,"#a3c8f0", "#a3bdf0", "#aca3f0"])
            fig1, ax1 = plt.subplots()
            ax1.bar(["ALB","BG","IT","MK","TR"],[ month_ptrs[1][0]/100000, month_ptrs[2][0]/100000, month_ptrs[3][0]/100000, month_ptrs[4][0]/100000, month_ptrs[5][0]/100000 ])
            ax1.set_xlabel("Countries")
            ax1.set_ylabel("Incoming Energy (MWh)x100000")
            fig1.set_figheight(4)
            fig1.set_figwidth(5)
            fig2, ax2 = plt.subplots()
            ax2.bar(["ALB","BG","IT","MK","TR"],[ month_ptrs[1][1]/100000, month_ptrs[2][1]/100000, month_ptrs[3][1]/100000, month_ptrs[4][1]/100000, month_ptrs[5][1]/100000 ])
            ax2.set_xlabel("Countries")
            ax2.set_ylabel("Outcoming Energy (MWh)x100000")
            fig2.set_figheight(4)
            fig2.set_figwidth(5)
            
            canvas1 = FigureCanvasTkAgg(fig1,rootmonth)
            canvas1.draw()
            canvas1.get_tk_widget().grid(rowspan=3,columnspan=3,row=3,column=0,sticky="nwes")
            canvas2 = FigureCanvasTkAgg(fig2,rootmonth)
            canvas2.draw()
            canvas2.get_tk_widget().grid(rowspan=3,columnspan=3,row=3,column=3,sticky="nesw")

            def open_max_stats():
                root_max = ttk.Toplevel(rootmonth)
                root_max.geometry("500x500")
                root_max.resizable(False, False)
                icon = ttk.PhotoImage(file='logo.png')
                root_max.iconphoto(True, icon)
                root_max.title(month_string + " " + year_string +" Maximum Energy Exchange")

                plt.rcParams["axes.prop_cycle"] = plt.cycler(color =["#a3eff0" ,"#dac27c" ,"#a3c8f0", "#a3ddf0", "#a3c8f0"])
                fig6, ax6 = plt.subplots()
                ax6.bar(["ALB","BG","IT","MK","TR"],[month_ptrs[6][0], month_ptrs[6][1], month_ptrs[6][2], month_ptrs[6][3], month_ptrs[6][4]])
                ax6.set_xlabel("Countries")
                ax6.set_ylabel("Maximum Energy Exchange (MWh)")
                fig6.set_figheight(4)
                fig6.set_figwidth(5)
                canvas6 = FigureCanvasTkAgg(fig6, root_max)
                canvas6.draw()
                canvas6.get_tk_widget().pack(side="top", fill="both", expand=1)


            max_button=ttk.Button(rootmonth,text="Open maximum Stats",width=20,padding=20,style="outline-dark",command=open_max_stats)
            max_button.grid(row=1,column=5,rowspan=2,padx=(20,270),pady=35)

    #window setup
    window.iconify()
    window2=ttk.Toplevel(title="Cross-Border Physical Flow (GR)",position=(500,170))
    window2.geometry("900x700")
    window2.resizable(False,False)
    icon = PhotoImage(file='logo.png')
    window2.iconphoto(True,icon)

    #title and choose period labels
    title = ttk.Label(window2, text="Cross-Border Physical Flow (Greece)",font=("Helvetica",15), bootstyle="inverse-light")
    title.pack(side="top",pady=40)
    labelperiod = ttk.Label(window2, text="Choose Month:",font=("Helvetica",14), bootstyle="inverse-light")
    labelperiod.pack(side="top",pady=40)

    dict_months ={
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
    }
    #list of months
    listmonths =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    
    #dropdown menu
    combobox_month=ttk.Combobox(window2,bootstyle="Dark",values=listmonths,state="readonly")
    combobox_month.set("Choose month")
    combobox_month.pack()

    #list of years
    listyears = [
        "2022",
        "2023"
    ]

    #dropdown menu
    combobox_year=ttk.Combobox(window2,bootstyle="Dark",values=listyears,state="readonly")
    combobox_year.set("Choose year")
    combobox_year.pack(pady=10)
    
    #button
    bconfirm = ttk.Button(window2,text= "Confirm Month",bootstyle="outline-dark",width=20,command=monthdata)
    bconfirm.pack(side="top",pady=20)
    #--------------------------------------------Compare------------------------------------------------------------
    line=ttk.Separator(window2,style="darkly")
    line.pack(fill="x",pady=(10,0),padx=70)
    
    titlecompare=ttk.Label(window2,text="Compare Section",font="Arial 15",style="inverse-light")
    titlecompare.pack(pady=(30,15))
    
    list_countries=["Germany","France","Denmark"]
    countries_Combo=ttk.Combobox(window2,bootstyle="Dark",values=list_countries,state="readonly")
    countries_Combo.pack(pady=15)
    countries_Combo.set("Choose Country")
    

    def open_compare():
        month_string=combobox_month.get()
        year_string=combobox_year.get()
        country = countries_Combo.get()
        if (month_string not in listmonths):
            messagebox.showerror("Error","No valid month has been selected.\nPlease enter valid month.")
        elif year_string not in listyears:
            messagebox.showerror("Error","No valid year has been selected.\nPlease enter valid year.")
        elif country not in list_countries:
            messagebox.showerror("Error","No valid country has been selected.\nPlease enter valid country.")
            
        
        else:      
            root_compare_month=ttk.Toplevel(window2)
                
            root_compare_month.state("zoomed")
            root_compare_month.resizable(False,False)
            icon = PhotoImage(file='logo.png')
            root_compare_month.iconphoto(True,icon)
            root_compare_month.title(month_string + " " + year_string + " Data"+f"Compare with {country}")

            #dedomena poy theloume
            month_ptrs_gr=month(dict_months[month_string],year_string) #mono to [0][0] kai [0][1] 
            
            if(country == "Germany"):
                month_ptrs_cmp = month_deutchland(dict_months[month_string],year_string)
            elif(country == "France"):
                month_ptrs_cmp = month_france(dict_months[month_string],year_string)
            elif(country == "Denmark"):
                month_ptrs_cmp = month_denmark(dict_months[month_string],year_string)

            plt.rcParams["axes.prop_cycle"] = plt.cycler(color =["#a3eff0" ,"#a3ddf0" ,"#a3c8f0", "#a3bdf0", "#aca3f0"])
            fig1, ax1 = plt.subplots()
            ax1.bar(["Greece",f"{country}"],[month_ptrs_gr[0][0]/100000,month_ptrs_cmp[0]/100000 ])
            ax1.set_xlabel("Countries")
            ax1.set_ylabel("Total Incoming Energy (MWh)x100000")
            fig1.set_figheight(4)
            fig1.set_figwidth(5)
            fig2, ax2 = plt.subplots()
            ax2.bar(["Greece",f"{country}"],[month_ptrs_gr[0][1]/100000,month_ptrs_cmp[1]/100000 ])
            ax2.set_xlabel("Countries")
            ax2.set_ylabel("Total Outcoming Energy (MWh)x100000")
            fig2.set_figheight(4)
            fig2.set_figwidth(5)
            
            canvas1 = FigureCanvasTkAgg(fig1,root_compare_month)
            canvas1.draw()
            canvas1.get_tk_widget().pack(side="top", fill="both", expand=1)
            canvas2 = FigureCanvasTkAgg(fig2,root_compare_month)
            canvas2.draw()
            canvas2.get_tk_widget().pack(side="top", fill="both", expand=1)


    bcompare= ttk.Button(window2,text= "Compare (For selected Month)",bootstyle="outline-dark",width=25,command=open_compare)
    bcompare.pack(pady=15)

    window2.mainloop()


def openyear(window):
    def yeardata():
        listofyears=["2023","2022"]
        year_string=combobox.get()
        
        if (year_string not in listofyears):
            messagebox.showerror("Error","No valid year has been selected.\nPlease enter valid year.")
        else:
            year_ptrs=year(year_string)
            rootyear=ttk.Toplevel(window1)
            
            rootyear.state("zoomed")
            rootyear.resizable(False,False)
            icon = PhotoImage(file='logo.png')
            rootyear.iconphoto(True,icon)
            rootyear.title( "Year "+ year_string + " Data")
            rootyear.columnconfigure((0,1,2,3,4,5,6,7),weight=1)
            rootyear.rowconfigure((0,1,2,3,4,5),weight=1)
            totalframe=ttk.Labelframe(rootyear,style="darkly",text="Total Incoming-Outcoming Energy (Greece)",borderwidth=10)
            totalframe.grid(column=0,row=0,columnspan=4,rowspan=2,sticky="nw",padx=60,pady=(30,0))

            meterstats_incoming = ttk.Meter(
                totalframe,
                bootstyle="success",
                arcrange=180,
                arcoffset=180,
                amounttotal=15000000,
                amountused=int(year_ptrs[0][0]),
                meterthickness=9,
                metersize=200,
                interactive=False,     
                metertype="semi",
                stepsize=40,
                stripethickness=0,
                textfont="Arial 13",
                subtext="Total Incoming(MWh)",
                subtextfont="Arial 9",
            )
            meterstats_incoming.grid(row=0,column=0,padx=25,pady=(50,0))
            meterstats_outcoming = ttk.Meter(
                totalframe,
                bootstyle="warning",
                arcrange=180,
                arcoffset=180,
                amounttotal=15000000,
                amountused=int(year_ptrs[0][1]),
                meterthickness=9,
                metersize=200,
                interactive=False,     
                metertype="semi",
                stepsize=40,
                stripethickness=0,
                textfont="Arial 13",
                subtext="Total Outcoming(MWh)",
                subtextfont="Arial 9",
            )

            x=0
            if year_ptrs[0][2]>=0:
                x = 15000000
            else: 
                x=-15000000
            meterstats_outcoming.grid(row=0,column=1,padx=25,pady=(50,0))
            meterstats_difference = ttk.Meter(
                totalframe,
                bootstyle="danger",
                arcrange=180,
                arcoffset=180,
                amounttotal=x,
                amountused=int(year_ptrs[0][2]),
                meterthickness=9,
                metersize=200,
                interactive=False,     
                metertype="semi",
                stepsize=40,
                stripethickness=0,
                textfont="Arial 13",
                subtext="Net Position(MWh)",
                subtextfont="Arial 9",
            )
            meterstats_difference.grid(row=0,column=2,padx=25,pady=(50,0))

            plt.rcParams["axes.prop_cycle"] = plt.cycler(color =["#a3eff0" ,"#a3ddf0" ,"#a3c8f0", "#a3bdf0", "#aca3f0"])
            fig1, ax1 = plt.subplots()
            ax1.bar(["ALB","BG","IT","MK","TR"],[ year_ptrs[1][0],year_ptrs[2][0],year_ptrs[3][0], year_ptrs[4][0], year_ptrs[5][0] ])
            ax1.set_xlabel("Countries")
            ax1.set_ylabel("Incoming Energy (MWh)")
            fig1.set_figheight(4)
            fig1.set_figwidth(5)
            fig2, ax2 = plt.subplots()
            ax2.bar(["ALB","BG","IT","MK","TR"],[ year_ptrs[1][1], year_ptrs[2][1], year_ptrs[3][1], year_ptrs[4][1],year_ptrs[5][1] ])
            ax2.set_xlabel("Countries")
            ax2.set_ylabel("Outcoming Energy (MWh)")
            fig2.set_figheight(4)
            fig2.set_figwidth(5)
            
            canvas1 = FigureCanvasTkAgg(fig1,rootyear)
            canvas1.draw()
            canvas1.get_tk_widget().grid(rowspan=3,columnspan=3,row=3,column=0,sticky="nwes")
            canvas2 = FigureCanvasTkAgg(fig2,rootyear)
            canvas2.draw()
            canvas2.get_tk_widget().grid(rowspan=3,columnspan=3,row=3,column=3,sticky="nesw")

            def open_max_stats():
                root_max = ttk.Toplevel(rootyear)
                root_max.geometry("500x500")
                root_max.resizable(False, False)
                icon = ttk.PhotoImage(file='logo.png')
                root_max.iconphoto(True, icon)
                root_max.title("Year "+ year_string + " Maximum Energy Exchange")

                plt.rcParams["axes.prop_cycle"] = plt.cycler(color =["#a3eff0" ,"#dac27c" ,"#a3c8f0", "#a3ddf0", "#a3c8f0"])
                fig6, ax6 = plt.subplots()
                ax6.bar(["ALB","BG","IT","MK","TR"],[year_ptrs[6][0], year_ptrs[6][1], year_ptrs[6][2], year_ptrs[6][3], year_ptrs[6][4]])
                ax6.set_xlabel("Countries")
                ax6.set_ylabel("Maximum Energy Exchange (MWh)")
                fig6.set_figheight(4)
                fig6.set_figwidth(5)
                canvas6 = FigureCanvasTkAgg(fig6, root_max)
                canvas6.draw()
                canvas6.get_tk_widget().pack(side="top", fill="both", expand=1)


            max_button=ttk.Button(rootyear,text="Open maximum Stats",width=20,padding=20,style="outline-dark",command=open_max_stats)
            max_button.grid(row=1,column=5,rowspan=2,padx=(20,270),pady=35)

    #window setup
    window.iconify()
    window1=ttk.Toplevel(title="Cross-Border Physical Flow (GR)",position=(500,170))
    window1.geometry("900x650")
    window1.resizable(False,False)
    icon = PhotoImage(file='logo.png')
    window1.iconphoto(True,icon)
    
    #title and choose period labels
    title = ttk.Label(window1, text="Cross-Border Physical Flow (Greece)",font=("Helvetica",15), bootstyle="inverse-light")
    title.pack(side="top",pady=40)
    labelperiod = ttk.Label(window1, text="Choose Year:",font=("Helvetica",14), bootstyle="inverse-light")
    labelperiod.pack(side="top",pady=30)

    #list of years
    listyears = [
        "2022",
        "2023"
    ]

    #dropdown menu
    combobox=ttk.Combobox(window1,bootstyle="Dark",values=listyears,state="readonly")
    combobox.set("Choose year")
    combobox.pack()

    #button
    bconfirm = ttk.Button(window1,text= "Confirm year",bootstyle="outline-dark",width=20,command=yeardata)
    bconfirm.pack(side="top",pady=20)

    line=ttk.Separator(window1,style="darkly")
    line.pack(fill="x",pady=(10,0),padx=70)
    
    titlecompare=ttk.Label(window1,text="Compare Section",font="Arial 15",style="inverse-light")
    titlecompare.pack(pady=(30,15))
    
    list_countries=["Germany","France","Denmark"]
    countries_Combo=ttk.Combobox(window1,bootstyle="Dark",values=list_countries,state="readonly")
    countries_Combo.pack(pady=15)
    countries_Combo.set("Choose Country")

    def open_compare():
        listofyears=["2023","2022"]
        year_string=combobox.get()
        country = countries_Combo.get()
        if (year_string not in listofyears ):
            messagebox.showerror("Error","No valid year has been selected.\nPlease enter valid year.")
        elif country not in list_countries:
            messagebox.showerror("Error","No valid country has been selected.\nPlease enter valid country.")
        else:
            root_compare_year=ttk.Toplevel(window1)
            root_compare_year.state("zoomed")
            root_compare_year.resizable(False,False)
            icon = PhotoImage(file='logo.png')
            root_compare_year.iconphoto(True,icon)
            root_compare_year.title( "Year "+ year_string + f" Compare with {country}")

            #dedomena poy theloume
            year_ptrs_gr=year(year_string) #mono to [0][0] kai [0][1] 
            
            if(country == "Germany"):
                year_ptrs_cmp = year_deutchland(year_string)
            elif(country == "France"):
                year_ptrs_cmp = year_france(year_string)
            elif(country == "Denmark"):
                year_ptrs_cmp = year_denmark(year_string)

            plt.rcParams["axes.prop_cycle"] = plt.cycler(color =["#a3eff0" ,"#a3ddf0" ,"#a3c8f0", "#a3bdf0", "#aca3f0"])
            fig1, ax1 = plt.subplots()
            ax1.bar(["Greece",f"{country}"],[year_ptrs_gr[0][0],year_ptrs_cmp[0] ])
            ax1.set_xlabel("Countries")
            ax1.set_ylabel("Total Incoming Energy (MWh)")
            fig1.set_figheight(4)
            fig1.set_figwidth(5)
            fig2, ax2 = plt.subplots()
            ax2.bar(["Greece",f"{country}"],[year_ptrs_gr[0][1],year_ptrs_cmp[1] ])
            ax2.set_xlabel("Countries")
            ax2.set_ylabel("Total Outcoming Energy (MWh)")
            fig2.set_figheight(4)
            fig2.set_figwidth(5)
            
            canvas1 = FigureCanvasTkAgg(fig1,root_compare_year)
            canvas1.draw()
            canvas1.get_tk_widget().pack(side="top", fill="both", expand=1)
            canvas2 = FigureCanvasTkAgg(fig2,root_compare_year)
            canvas2.draw()
            canvas2.get_tk_widget().pack(side="top", fill="both", expand=1)
            
            


            
    
    bcompare= ttk.Button(window1,text= "Compare (For selected Year)",bootstyle="outline-dark",width=25,command=open_compare)
    bcompare.pack(pady=15)

    window1.mainloop()

appopen()