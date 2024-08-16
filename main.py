from tkinter import*
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=eed5c5c417cd18a0a6908965712c4a4f").json()
    w_label1.config(text=data['weather'][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=data["main"]["temp"]-273.15)
    per_label1.config(text=data["main"]["pressure"])
    wi_label1.config(text=data['wind']["speed"])
    hu_label1.config(text=data["main"]['humidity'])
    
    
win=Tk()
win.title("Weather App")
win.config(bg = "red")
win.geometry("500x500")

name_label = Label(win,text="Weather App",
                   font=("Time New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Weather App",values=list_name,
                   font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

w_label = Label(win,text="Weather climate",
                   font=("Time New Roman",10))
w_label.place(y=260,height=20,width=130,x=25)
w_label1 = Label(win,text="",
                   font=("Time New Roman",10))
w_label1.place(y=260,height=20,width=130,x=200)



wb_label = Label(win,text="Weather description",
                   font=("Time New Roman",10))
wb_label.place(y=290,height=20,width=130,x=25)
wb_label1 = Label(win,text="",
                   font=("Time New Roman",10))
wb_label1.place(y=290,height=20,width=130,x=200)



temp_label = Label(win,text="Temperature",
                   font=("Time New Roman",10))
temp_label.place(y=320,height=20,width=110,x=25)
temp_label1 = Label(win,text="",
                   font=("Time New Roman",10))
temp_label1.place(y=320,height=20,width=140,x=200)



per_label = Label(win,text="Pressere",
                   font=("Time New Roman",10))
per_label.place(y=360,height=20,width=80,x=25)
per_label1 = Label(win,text="",
                   font=("Time New Roman",10))
per_label1.place(y=360,height=20,width=80,x=200)



wi_label = Label(win,text="Wind",
                   font=("Time New Roman",10))
wi_label.place(y=390,height=20,width=130,x=25)
wi_label1 = Label(win,text="",
                   font=("Time New Roman",10))
wi_label1.place(y=390,height=20,width=130,x=200)

hu_label = Label(win,text="Humidity",
                   font=("Time New Roman",10))
hu_label.place(y=420,height=20,width=130,x=25)
hu_label1 = Label(win,text="",
                   font=("Time New Roman",10))
hu_label1.place(y=420,height=20,width=130,x=200)

done_button = Button(win,text="Done",
                   font=("Time New Roman",30,"bold"),command= data_get)
done_button.place(y=190,height=50,width=100,x=200)



win.mainloop()
