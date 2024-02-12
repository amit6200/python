from tkinter import *
import os

def restart():
    os.system("shutdowm /r /t 1")
def restart_time():
    os.system("shutdowm /r /t 20")
def logout():
    os.system("shutdowm -l")    
def shutdowm():
    os.system("shutdowm /s /t 1")
st=Tk()
st.title("ShutDwon App")
st.geometry("500x500")
st.config(bg="blue")

r_button=Button(st,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="Plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button=Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="Plus",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

lg_button=Button(st,text="Log-Out",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="Plus",command=logout)
lg_button.place(x=150,y=270,height=50,width=200)

st_button=Button(st,text="ShutDowm",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="Plus",command=shutdowm)
st_button.place(x=150,y=370,height=50,width=200)

st.mainloop()