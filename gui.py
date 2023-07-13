import webbrowser as wb
from tkinter import * 

obj=Tk(className=" WINDOW")

e=Entry(obj,font=('Arial',30))
e.grid()

def navigate():
    query=e.get()
    wb.open("https://in.pinterest.com/search/pins/?q="+query)
    print(f'navigating to {query}')

b=Button(obj,text="Search",
         command=navigate,
         font=("",30))
b.grid() 

b1=Button(obj,text="Close",
         command=obj.destroy,
         font=("",30))
b1.grid()
obj.mainloop()


