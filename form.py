from tkinter import *
import webbrowser

def submit_form():
    name = entry_name.get()
    contact = entry_contact.get()
    
    selected_source = ""
    if var_source.get() == 1:
        selected_source = "Instagram Ads"
    elif var_source.get() == 2:
        selected_source = "YouTube Ads"
    elif var_source.get() == 3:
        selected_source = "Google Ads"
    
    with open("user_data.txt", "a") as file:
        file.write(f"Name: {name}, Contact: {contact}, Source: {selected_source}\n")
    
    if selected_source == "Instagram Ads":
        webbrowser.open("https://support.discord.com/hc/en-us/sections/200613688-FAQ")
    elif selected_source == "YouTube Ads":
        webbrowser.open("https://support.discord.com/hc/en-us/sections/200613688-FAQ")
    elif selected_source == "Google Ads":
        webbrowser.open("https://support.discord.com/hc/en-us/sections/200613688-FAQ")

window =Tk()
window.title("Enquiry Form")

main_label = Label(window,text='Enquiry Page By Discord',font='Fixedsys')
main_label.pack()

label_name =Label(window, text="Name:")
label_name.pack()
entry_name =Entry(window)
entry_name.pack()

label_contact = Label(window, text="Contact:")
label_contact.pack()
entry_contact = Entry(window)
entry_contact.pack()

label_source = Label(window, text="Where did you heard about our App/Website?",font=('Arial',10))
label_source.pack()

var_source = IntVar()

radiobutton_instagram = Radiobutton(window, text="Instagram Ads", variable=var_source, value=1)
radiobutton_instagram.pack()

radiobutton_youtube = Radiobutton(window, text="YouTube Ads", variable=var_source, value=2)
radiobutton_youtube.pack()

radiobutton_google = Radiobutton(window, text="Google Ads", variable=var_source, value=3)
radiobutton_google.pack()

button_submit = Button(window, text="Submit", command=submit_form)
button_submit.pack()

window.mainloop()
