from tkinter import * #for the pop up window
from tkinter import ttk  #for combo box
import requests

def data_get():
      city =city_name.get()
      data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=a9607efeea6649ae808fb9535a746f3c").json()
      
      w_label1.config(text=data["weather"][0]["main"])

      wb_label.config(text=data["weather"][0]["description"])

      temp1.config(text=str(int(data["main"]["temp"]-273.15)))
  
      pressure1.config(text=data["main"]["pressure"])












win =Tk() #window making calling Tk() class
win.title("Jeet's Weather Window")
win.config(bg ="blue")
win.geometry("500x570")

#LAbel
name_label = Label(win,text="Jeet's Weather App",
                   font=("Times New Roman",40,"bold"))


name_label.place(x=25,y=50,height=50,width=450)

#Combo Box

city_name =StringVar()
list_name =["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]  #List of states
com=ttk.Combobox(win,text="Jeet's Weather App",values=list_name,
                   font=("Times New Roman",20),textvariable=city_name)

com.place(x=25,y=120,height=50,width=450) #y=120 as height = 50 then y=50 + gap =20




w_label = Label(win,text="Weather Climate",
                   font=("Time New Roman",20))


w_label.place(x=25,y=260,height=50,width=210)  #after 190 50 gap then 20 gap
#For data block
w_label1 = Label(win,text="",
                   font=("Time New Roman",20))

w_label1.place(x=250,y=260,height=50,width=210)


wb_label = Label(win,text="Weather Description",
                   font=("Time New Roman",17))


wb_label.place(x=25,y=330,height=50,width=210)  #after 190 50 gap then 20 gap

wb_label = Label(win,text="",
                   font=("Time New Roman",16))


wb_label.place(x=250,y=330,height=50,width=210)


temp = Label(win,text="Temperature",
                   font=("Time New Roman",20))


temp.place(x=25,y=400,height=50,width=210)  

temp1 = Label(win,text="",
                   font=("Time New Roman",20))


temp1.place(x=250,y=400,height=50,width=210) 


pressure = Label(win,text="Pressure",
                   font=("Time New Roman",20))


pressure.place(x=25,y=470,height=50,width=210)


pressure1 = Label(win,text="",
                   font=("Time New Roman",20))


pressure1.place(x=250,y=470,height=50,width=210)


#button 
done_button= Button(win,text="Done",
                   font=("Time New Roman",20,"bold"),command=data_get)

#place button
done_button.place(y=190,height=50,width=100,x=200)  #The position will be 120 + 50(combobox width) + 20 gap.And
#  200gap  |Done button width 100|   200gap 





win.mainloop() #if you run the code at his point a Window will appear..now next step is Decorating the Window




