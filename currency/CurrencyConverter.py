from tkinter import ttk
from tkinter import *
import time
import tkinter.messagebox
import pandas
import requests

rates={
    "CAD":1.4627,"HKD":8.5843,"ISK":136.3,"PHP":56.382,"DKK":7.4731,
    "HUF":337.05,"CZK":25.21,"AUD":1.6494,"RON":4.7789,"SEK":10.6768,"IDR":15091.51,
    "INR":78.9055,"BRL":4.7157,"RUB":70.3375,"HRK":7.444,"JPY":120.35,"THB":34.46,"CHF":1.0694,
    "SGD":1.5092,"PLN":4.3009,"BGN":1.9558,"TRY":6.6117,"CNY":7.6664,"NOK":10.1893,"NZD":1.7083,
    "ZAR":16.49,"USD":1.1052,"MXN":20.8044,"ILS":3.809,"GBP":0.84175,"KRW":1321.6,"MYR":4.5297}

# for d in :
#     url = "https://api.exchangeratesapi.io/latest?base=EUR={}".format(d)
#     response = requests.get(url)
#     data = response.json()
#     rates[d] = data


class Converter:
    def __init__(self,root):
        self.root = root
        self.root.title("***Currency Converter***")
        self.root.geometry("1300x800+0+0")
        self.root.configure(background='Black')
        #==========frame==========
        TitleFrame=Frame(self.root, bd=10, width=1350, height=100, padx=10,pady=10, bg="Gray",relief=RIDGE)
        TitleFrame.grid(row=0,column=0)

        self.lblTitle=Label(TitleFrame,text="***Currency Converter***",padx=17,pady=4,bd=1,font=('arial',30,'bold'),bg="sky blue",width=50)
        self.lblTitle.pack()

        MainFrame= Frame(self.root, bd=10, width=1350, height=700, padx=11,pady=10, bg="Gray",relief=RIDGE)
        MainFrame.grid(row=1,column=0)

        FrameOne= Frame(MainFrame, bd=4, width=100, height=600, padx=5,pady=1,relief=RIDGE)
        FrameOne.grid(row=0,column=0)
        
        
        FrameTwo= Frame(MainFrame, bd=4, width=800, height=600, padx=5,pady=2,relief=RIDGE)
        FrameTwo.grid(row=0,column=1)
        
        FrameTwoTop= Frame(FrameTwo, bd=4, width=250, height=300, padx=80,pady=2,relief=RIDGE)
        FrameTwoTop.grid(row=0,column=0)
        
        FrameTwoButtom= Frame(FrameTwo, bd=4, width=350, height=300, padx=5,pady=2,relief=RIDGE)
        FrameTwoButtom.grid(row=1,column=0)

        FrameTwoButtomL= Frame(FrameTwoButtom, bd=4, width=350, height=300, padx=5,pady=2,relief=RIDGE)
        FrameTwoButtomL.grid(row=0,column=0)

        FrameTwoButtomR= Frame(FrameTwoButtom, bd=4, width=350, height=300, padx=10,pady=2,relief=RIDGE)
        FrameTwoButtomR.grid(row=0,column=1)

        FrameThree= Frame(MainFrame, bd=4, width=100, height=600, padx=5,pady=1,relief=RIDGE)
        FrameThree.grid(row=0,column=2)



        DateofConvert = StringVar()
        Value0=StringVar()
        convert=StringVar()
        currency=DoubleVar()
        var1=DoubleVar()
        var2=DoubleVar()

        convert.set(1)
        DateofConvert.set(time.strftime("%d/%m/%Y"))


        def cExit():
            cExit=tkinter.messagebox.askyesno("Exit System","Confirm to Exit")
            if cExit>0:
                root.destroy()
                return

        
        def Reset():
            Value0.set("")
            convert.set(1)
            currency.set["0.0"]
            var1.set(0)
            var2.set(0)
            self.canvas.delete["all"]
            self.root.resizable(True,True)


        def Calculation():
                convert1=float(convert.get()*rates)
                convert2=str('%.2f'%(convert1))
                currency.set(convert2)
                var1.set('%.2f'%(convert1))
                var2.set(convert.get())

            # elif (Value0.get=="Nepal"):
            #     convert1=float(convert.get()*114.34)
            #     convert2=str('%.2f'%(convert1))+"@Nepali Rupe"
            #     currency.set(convert2)
            #     var1.set('%.2f'%(convert1))
            #     var2.set(convert.get())

            


        # def canvasCal():
        #     c1=int(convert.get())
        #     c2=int(convert.get()*1.34)




    #    =========Date======
        self.lblToday=Label(FrameTwoTop,font=('arial',20,'bold'),text="Todays Date",padx=2,pady=10,bd=2,width=18)
        self.lblToday.grid(row=0,column=0)

        self.lblDate=Label(FrameTwoTop,font=('arial',20,'bold'),textvariable=DateofConvert,padx=2,pady=10,bd=2,width=18,justify='center')
        self.lblDate.grid(row=0,column=1)


        # ===============
        self.Converted=Scale(FrameThree,variable=var1,from_=1,to=700,length=500,tickinterval=30,orient=VERTICAL,state=DISABLED,label="Convert",bg="Sky blue",font=('arial',10,'bold'))
        self.Converted.grid(row=0,column=0,rowspan=2)        
        
        self.Convert=Scale(FrameOne,variable=var2,from_=1,to=500,length=508,tickinterval=30,orient=VERTICAL,label="Pound",bg="Sky blue",font=('arial',10,'bold'))
        self.Convert.grid(row=0,column=0,rowspan=2) 

        
        self.lblBritishPound=Label(FrameTwoTop,font=('arial',20,'bold'),text='British Pound',padx=2,pady=10,bd=2,width=19)
        self.lblBritishPound.grid(row=1,column=0)

        self.EntCurrency=Entry(FrameTwoTop,font=('arial',20,'bold'),textvariable=convert, bd=2,width=23,justify='center')
        self.EntCurrency.grid(row=1,column=1,pady=10)

        # self.box=ttk.Combobox(FrameTwoTop,textvariable=Value0,values=list(rates.key()),state='readonly',font=('arial',20,'bold'),width=20)
        # # self.box['values']=list(rates.key())
        # tk.Label(Frame, text='Choose prefered currency', bd=3).grid(row=0, column=0)
        # rates = tk.StringVar()
        # self.lblChoise=Label(FrameTwoTop,font=('arial',20,'bold'),text='Choose prefered currency',padx=2,pady=10,bd=2,width=19)
        # self.lblChoise.grid(row=1,column=0)
        self.box = ttk.Combobox(FrameTwoTop, values=list(rates.keys()),state='readonly',font=('arial',20,'bold'),width=20,textvariable=Value0)
        self.box.bind('<<ComboboxSelected>>', lambda event: label_selected.config(text=rates[Value0.get()]))
        self.box.grid(row=2,column=0,padx=10,pady=6)
        # self.box.current(0)

        # label_selected = tk.Label(root, text="Not Selected")
        # label_selected.grid(row=1, column=1)

        self.lblCurrency=Label(FrameTwoTop,font=('arial',20,'bold'),textvariable=currency,bd=2,width=20,bg='white',pady=2,padx=2,relief='sunken')
        self.lblCurrency.grid(row=2,column=1)



        self.canvas=Canvas(FrameTwoButtomL,width=600,height=300, bg='sky blue')
        self.canvas.pack()
        self.canvas.create_line(100,250,400,250,width=3)
        self.canvas.create_line(100,250,100,50,width=3)


        # ========Button=======
        self.btnTodaysRate=Button(FrameTwoButtomR,text='TodaysRate',padx=2,pady=8,bd=2,fg="black",font=('arial',20,'bold'),width=14,height=2)
        self.btnTodaysRate.grid(row=4,column=0)
        self.btnConvert=Button(FrameTwoButtomR,text='Convert',padx=2,pady=8,bd=2,fg="black",font=('arial',20,'bold'),width=14,height=2,command=Calculation)
        self.btnConvert.grid(row=5,column=0)
        self.btnReset=Button(FrameTwoButtomR,text='Reset',padx=2,pady=8,bd=2,fg="black",font=('arial',20,'bold'),width=14,height=2,command=Reset)
        self.btnReset.grid(row=6,column=0)
        self.btnExit=Button(FrameTwoButtomR,text='Exit',padx=2,pady=8,bd=2,fg="black",font=('arial',20,'bold'),width=14,height=2,command=cExit)
        self.btnExit.grid(row=7,column=0)


if __name__=='__main__':
    root=Tk()
    application=Converter(root)
    root.mainloop()
    

