from PIL import Image
Image.CUBIC = Image.BICUBIC
import ttkbootstrap as ttk
import datetime
from tkinter import *
from tkinter import messagebox
from open_date_code import date
from open_month_code import month
from open_year_code import year
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def appopen():
    #window setup
    window=ttk.Window(title="Cross-Border Physical Flow (GR)",themename="sandstone",)
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
        rootdate.columnconfigure((0,1,2,3,4),weight=1)
        rootdate.rowconfigure((0,1,2,3,4),weight=1)
        totalframe=ttk.Labelframe(rootdate,style="darkly",text="Total Incoming-Outcoming Energy (Greece)",borderwidth=10)
        totalframe.grid(column=0,row=0,columnspan=4,rowspan=2,sticky="nw",padx=50,pady=(20,0))

        meterstats_incoming = ttk.Meter(
            totalframe,
            bootstyle="darkly",
            arcrange=180,
            arcoffset=180,
            amounttotal=10000000,
            amountused=int(date_ptrs[0][0]),
            meterthickness=9,
            metersize=200,
            interactive=False,     
            metertype="semi",
            stepsize=40,
            stripethickness=0,
            textfont="Arial 13",
            subtext="Total Incoming(MW)",
            subtextfont="Arial 9"
        )
       
        meterstats_incoming.grid(row=0,column=0,padx=25,pady=(25,0))
        meterstats_outcoming = ttk.Meter(
            totalframe,
            bootstyle="darkly",
            arcrange=180,
            arcoffset=180,
            amounttotal=10000000,
            amountused=int(date_ptrs[0][1]),
            meterthickness=9,
            metersize=200,
            interactive=False,     
            metertype="semi",
            stepsize=40,
            stripethickness=0,
            textfont="Arial 13",
            subtext="Total Outcoming(MW)",
            subtextfont="Arial 9"
        )
        
        meterstats_outcoming.grid(row=0,column=1,padx=25,pady=(25,0))
        meterstats_difference = ttk.Meter(
            totalframe,
            bootstyle="darkly",
            arcrange=180,
            arcoffset=180,
            amounttotal=10000000,
            amountused=abs(int(date_ptrs[0][2])),
            meterthickness=9,
            metersize=200,
            interactive=False,     
            metertype="semi",
            stepsize=40,
            stripethickness=0,
            textfont="Arial 13",
            subtext="Total Difference(MW)",
            subtextfont="Arial 9"
        )
        meterstats_difference.grid(row=0,column=2,padx=25,pady=(25,0))
        
        lineseperate=ttk.Separator(rootdate,style="darkly",orient="horizontal")
        lineseperate.grid(row=2,columnspan=4,sticky="wen",padx=55,pady=35)

        plt.rcParams["axes.prop_cycle"] = plt.cycler(color =["#a3eff0" ,"#a3ddf0" ,"#a3c8f0", "#a3bdf0", "#aca3f0"])
        fig1, ax1 = plt.subplots()
        ax1.bar(["ALB","BG","IT","MK","TR"],[ date_ptrs[1][0], date_ptrs[2][0], date_ptrs[3][0], date_ptrs[4][0], date_ptrs[5][0] ])
        ax1.set_xlabel("Countries")
        ax1.set_ylabel("Incoming Energy (MW)")
        fig1.set_figheight(5)
        fig1.set_figwidth(5)

        fig2, ax2 = plt.subplots()
        ax2.bar(["ALB","BG","IT","MK","TR"],[ date_ptrs[1][1], date_ptrs[2][1], date_ptrs[3][1], date_ptrs[4][1], date_ptrs[5][1] ])
        ax2.set_xlabel("Countries")
        ax2.set_ylabel("Outcoming Energy (MW)")
        fig2.set_figheight(5)
        fig2.set_figwidth(5)

        fig3, ax3 = plt.subplots()
        ax3.bar(["ALB","BG","IT","MK","TR"],[ date_ptrs[1][2], date_ptrs[2][2], date_ptrs[3][2], date_ptrs[4][2], date_ptrs[5][2] ])
        ax3.set_xlabel("Countries")
        ax3.set_ylabel("Difference (MW)")
        fig3.set_figheight(5)
        fig3.set_figwidth(5)

        totalframe1=ttk.Labelframe(rootdate,style="darkly",text="Diagrams for incoming-outcoming energy from each country",borderwidth=10)
        totalframe1.grid(column=0,row=3,columnspan=4,rowspan=1,sticky="nws",padx=20,pady=(20,0))

        canvas1 = FigureCanvasTkAgg(fig1,totalframe1)
        canvas1.draw()
        canvas1.get_tk_widget().grid(row=0,column=0,sticky="nw",padx=(25,30))

        canvas2 = FigureCanvasTkAgg(fig2,totalframe1)
        canvas2.draw()
        canvas2.get_tk_widget().grid(row=0,column=1,sticky="nw",padx=(25,25))

        canvas3 = FigureCanvasTkAgg(fig3,totalframe1)
        canvas3.draw()
        canvas3.get_tk_widget().grid(row=0,column=2,sticky="nw",padx=(25,30))

    #window setup
    window.iconify()
    window3=ttk.Toplevel(title="Cross-Border Physical Flow (GR)")
    window3.geometry("900x600")
    window3.resizable(False,False)
    icon = PhotoImage(file='logo.png')
    window3.iconphoto(True,icon)
    
    #title and choose period labels
    title = ttk.Label(window3, text="Cross-Border Physical Flow (Greece)",font=("Helvetica",15), bootstyle="inverse-light")
    title.pack(side="top",pady=40)
    labelperiod = ttk.Label(window3, text="Choose Date:",font=("Helvetica",14), bootstyle="inverse-light")
    labelperiod.pack(side="top",pady=40)

    #buttons placement
    dateentry=ttk.DateEntry(window3,bootstyle="Dark")
    dateentry.pack()
    
    def confirmdate():
        check = 0 
        datechose = dateentry.entry.get()
        chosenyear = datetime.datetime.strptime(datechose, '%d/%m/%Y').year
        today = datetime.date.today()
        if chosenyear < 2022 or chosenyear > 2023 or datetime.datetime.strptime(datechose, '%d/%m/%Y').date() > today:
            messagebox.showerror("Error", "Please enter a valid date (2022-2023 and not after today)")
            check = 1
        if check == 0:
            datedata() 
        
    labelperiod = ttk.Label(window3, text="*(2022-2024)",font=("Helvetica",11), bootstyle="inverse-light")
    labelperiod.pack(side="top",pady=5)

    bconfirm = ttk.Button(window3,text= "Confirm Date",bootstyle="outline-dark",width=20,command=confirmdate)
    bconfirm.pack(side="top",pady=20)

    window3.mainloop()

def openmonth(window):
    def monthdata():    
        listofyears=["2023","2022","2021","2020"]
        month_string=combobox_month.get()
        year_string=combobox_year.get()
        
        if (month_string not in listmonths):
            messagebox.showerror("Error","No valid month has been selected.\nPlease enter valid month.")
        else:
            month_ptrs=month(dict_months[month_string],year_string)
            rootmonth=ttk.Toplevel(window2)
            
            rootmonth.state("zoomed")
            rootmonth.resizable(False,False)
            icon = PhotoImage(file='logo.png')
            rootmonth.iconphoto(True,icon)
            rootmonth.title(month_string + " " + year_string + " Data")
            rootmonth.columnconfigure((0,1,2,3,4),weight=1)
            rootmonth.rowconfigure((0,1,2,3,4),weight=1)
            totalframe=ttk.Labelframe(rootmonth,style="darkly",text="Total Incoming-Outcoming Energy (Greece)",borderwidth=10)
            totalframe.grid(column=0,row=0,columnspan=4,rowspan=2,sticky="nw",padx=50,pady=(20,0))

            meterstats_incoming = ttk.Meter(
                totalframe,
                bootstyle="darkly",
                arcrange=180,
                arcoffset=180,
                amounttotal=10000000,
                amountused=int(month_ptrs[0][0]),
                meterthickness=9,
                metersize=200,
                interactive=False,     
                metertype="semi",
                stepsize=40,
                stripethickness=0,
                textfont="Arial 13",
                subtext="Total Incoming(MW)",
                subtextfont="Arial 9",
            )
            meterstats_incoming.grid(row=0,column=0,padx=25,pady=(25,0))
            meterstats_outcoming = ttk.Meter(
                totalframe,
                bootstyle="darkly",
                arcrange=180,
                arcoffset=180,
                amounttotal=10000000,
                amountused=int(month_ptrs[0][1]),
                meterthickness=9,
                metersize=200,
                interactive=False,     
                metertype="semi",
                stepsize=40,
                stripethickness=0,
                textfont="Arial 13",
                subtext="Total Outcoming(MW)",
                subtextfont="Arial 9",
            )
            meterstats_outcoming.grid(row=0,column=1,padx=25,pady=(25,0))
            meterstats_difference = ttk.Meter(
                totalframe,
                bootstyle="darkly",
                arcrange=180,
                arcoffset=180,
                amounttotal=10000000,
                amountused=abs(int(month_ptrs[0][2])),
                meterthickness=9,
                metersize=200,
                interactive=False,     
                metertype="semi",
                stepsize=40,
                stripethickness=0,
                textfont="Arial 13",
                subtext="Total Difference(MW)",
                subtextfont="Arial 9",
            )
            meterstats_difference.grid(row=0,column=2,padx=25,pady=(25,0))
            
            lineseperate=ttk.Separator(rootmonth,style="darkly",orient="horizontal")
            lineseperate.grid(row=2,columnspan=4,sticky="wen",padx=55,pady=35)

            plt.rcParams["axes.prop_cycle"] = plt.cycler(color =["#a3eff0" ,"#a3ddf0" ,"#a3c8f0", "#a3bdf0", "#aca3f0"])
            fig1, ax1 = plt.subplots()
            ax1.bar(["ALB","BG","IT","MK","TR"],[ month_ptrs[1][0], month_ptrs[2][0], month_ptrs[3][0], month_ptrs[4][0], month_ptrs[5][0] ])
            ax1.set_xlabel("Countries")
            ax1.set_ylabel("Incoming Energy (MW)")
            fig1.set_figheight(5)
            fig1.set_figwidth(5)

            fig2, ax2 = plt.subplots()
            ax2.bar(["ALB","BG","IT","MK","TR"],[ month_ptrs[1][1], month_ptrs[2][1], month_ptrs[3][1], month_ptrs[4][1], month_ptrs[5][1] ])
            ax2.set_xlabel("Countries")
            ax2.set_ylabel("Outcoming Energy (MW)")
            fig2.set_figheight(5)
            fig2.set_figwidth(5)

            fig3, ax3 = plt.subplots()
            ax3.bar(["ALB","BG","IT","MK","TR"],[ month_ptrs[1][2], month_ptrs[2][2], month_ptrs[3][2], month_ptrs[4][2], month_ptrs[5][2] ])
            ax3.set_xlabel("Countries")
            ax3.set_ylabel("Difference (MW)")
            fig3.set_figheight(5)
            fig3.set_figwidth(5)

            totalframe1=ttk.Labelframe(rootmonth,style="darkly",text="Diagrams for incoming-outcoming energy from each country",borderwidth=10)
            totalframe1.grid(column=0,row=3,columnspan=4,rowspan=1,sticky="nws",padx=20,pady=(20,0))

            canvas1 = FigureCanvasTkAgg(fig1,totalframe1)
            canvas1.draw()
            canvas1.get_tk_widget().grid(row=0,column=0,sticky="nw",padx=(25,30))

            canvas2 = FigureCanvasTkAgg(fig2,totalframe1)
            canvas2.draw()
            canvas2.get_tk_widget().grid(row=0,column=1,sticky="nw",padx=(25,25))

            canvas3 = FigureCanvasTkAgg(fig3,totalframe1)
            canvas3.draw()
            canvas3.get_tk_widget().grid(row=0,column=2,sticky="nw",padx=(25,30))

    #window setup
    window.iconify()
    window2=ttk.Toplevel(title="Cross-Border Physical Flow (GR)")
    window2.geometry("900x600")
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

    window2.mainloop()


def openyear(window):
    def yeardata():
        listofyears=["2023","2022","2021","2020"]
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
            rootyear.columnconfigure((0,1,2,3,4),weight=1)
            rootyear.rowconfigure((0,1,2,3,4),weight=1)
            totalframe=ttk.Labelframe(rootyear,style="darkly",text="Total Incoming-Outcoming Energy (Greece)",borderwidth=10)
            totalframe.grid(column=0,row=0,columnspan=4,rowspan=2,sticky="nw",padx=50,pady=(20,0))

            meterstats_incoming = ttk.Meter(
                totalframe,
                bootstyle="darkly",
                arcrange=180,
                arcoffset=180,
                amounttotal=10000000,
                amountused=int(year_ptrs[0][0]),
                meterthickness=9,
                metersize=200,
                interactive=False,     
                metertype="semi",
                stepsize=40,
                stripethickness=0,
                textfont="Arial 13",
                subtext="Total Incoming(MW)",
                subtextfont="Arial 9",
            )
            meterstats_incoming.grid(row=0,column=0,padx=25,pady=(25,0))
            meterstats_outcoming = ttk.Meter(
                totalframe,
                bootstyle="darkly",
                arcrange=180,
                arcoffset=180,
                amounttotal=10000000,
                amountused=int(year_ptrs[0][1]),
                meterthickness=9,
                metersize=200,
                interactive=False,     
                metertype="semi",
                stepsize=40,
                stripethickness=0,
                textfont="Arial 13",
                subtext="Total Outcoming(MW)",
                subtextfont="Arial 9",
            )
            meterstats_outcoming.grid(row=0,column=1,padx=25,pady=(25,0))
            meterstats_difference = ttk.Meter(
                totalframe,
                bootstyle="darkly",
                arcrange=180,
                arcoffset=180,
                amounttotal=10000000,
                amountused=abs(int(year_ptrs[0][2])),
                meterthickness=9,
                metersize=200,
                interactive=False,     
                metertype="semi",
                stepsize=40,
                stripethickness=0,
                textfont="Arial 13",
                subtext="Total Difference(MW)",
                subtextfont="Arial 9",
            )
            meterstats_difference.grid(row=0,column=2,padx=25,pady=(25,0))
            
            lineseperate=ttk.Separator(rootyear,style="darkly",orient="horizontal")
            lineseperate.grid(row=2,columnspan=4,sticky="wen",padx=55,pady=35)

            plt.rcParams["axes.prop_cycle"] = plt.cycler(color =["#a3eff0" ,"#a3ddf0" ,"#a3c8f0", "#a3bdf0", "#aca3f0"])
            fig1, ax1 = plt.subplots()
            ax1.bar(["ALB","BG","IT","MK","TR"],[ year_ptrs[1][0], year_ptrs[2][0], year_ptrs[3][0], year_ptrs[4][0], year_ptrs[5][0] ])
            ax1.set_xlabel("Countries")
            ax1.set_ylabel("Incoming Energy (MW)")
            fig1.set_figheight(5)
            fig1.set_figwidth(5)

            fig2, ax2 = plt.subplots()
            ax2.bar(["ALB","BG","IT","MK","TR"],[ year_ptrs[1][1], year_ptrs[2][1], year_ptrs[3][1], year_ptrs[4][1], year_ptrs[5][1] ])
            ax2.set_xlabel("Countries")
            ax2.set_ylabel("Outcoming Energy (MW)")
            fig2.set_figheight(5)
            fig2.set_figwidth(5)

            fig3, ax3 = plt.subplots()
            ax3.bar(["ALB","BG","IT","MK","TR"],[ year_ptrs[1][2], year_ptrs[2][2], year_ptrs[3][2], year_ptrs[4][2], year_ptrs[5][2] ])
            ax3.set_xlabel("Countries")
            ax3.set_ylabel("Difference (MW)")
            fig3.set_figheight(5)
            fig3.set_figwidth(5)


            totalframe1=ttk.Labelframe(rootyear,style="darkly",text="Diagrams for incoming-outcoming energy from each country",borderwidth=10)
            totalframe1.grid(column=0,row=3,columnspan=4,rowspan=1,sticky="nws",padx=20,pady=(20,0))

            canvas1 = FigureCanvasTkAgg(fig1,totalframe1)
            canvas1.draw()
            canvas1.get_tk_widget().grid(row=0,column=0,sticky="nw",padx=(25,30))

            canvas2 = FigureCanvasTkAgg(fig2,totalframe1)
            canvas2.draw()
            canvas2.get_tk_widget().grid(row=0,column=1,sticky="nw",padx=(25,25))

            canvas3 = FigureCanvasTkAgg(fig3,totalframe1)
            canvas3.draw()
            canvas3.get_tk_widget().grid(row=0,column=2,sticky="nw",padx=(25,30))
        
    #window setup
    window.iconify()
    window1=ttk.Toplevel(title="Cross-Border Physical Flow (GR)")
    window1.geometry("900x600")
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

    window1.mainloop()

appopen()