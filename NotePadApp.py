from tkinter import *
from tkinter import filedialog
import os
note = Tk()

note.title("Notepad")
note.geometry("350x410")
note.iconbitmap("C:\\Users\\jamie\\.vscode\\py\\Python Tkinter Practice\\icons\\Icons8-Windows-8-Programming-Edit-Property.ico")

#File status bool variable
File_Status_Name = False
selected = False
#Function for opening file
def Open_File():
    try:
        global text_file
        global File_Status_Name

        File_Status_Name = True

        #Opens file
        text_file = filedialog.askopenfilename(initialdir="C:\\Users\\jamie\\OneDrive\\Documents\\TextFiles", title="Open Text File", filetypes=(("Text file","*.txt"),))
        txt_file = open(text_file,"r")

        #Updates the status bar
        Name = text_file
        StatusBar.config(text=Name)
        
        #updates the title
        Name = Name.replace("C:/Users/jamie/OneDrive/Documents/TextFiles/", "")
        note.title(f"{Name} - Notepad")

        #Inserting text from file to text box and closing the file
        text = txt_file.read()
        MainText.delete(1.0, END)
        MainText.insert(END, text)

        #closing the file
        txt_file.close()

    except:
        pass

#Function fort saving file as
def Save_As_File():
    global File_Status_Name, text_file
    try:
        text_file = filedialog.asksaveasfilename(initialdir="C:\\Users\\jamie\\OneDrive\\Documents\\TextFiles", title="Open Text File", filetypes=(("Text File","*.txt"),), defaultextension="*.")
        txt_file = open(text_file, "w")
        txt_file.write(MainText.get(1.0, END))
        txt_file.close()    

        #Updates the status bar
        Name = text_file
        StatusBar.config(text=Name)
        
        #updates the title
        Name = Name.replace("C:/Users/jamie/OneDrive/Documents/TextFiles/", "")
        note.title(f"{Name} - Notepad")

        File_Status_Name = True
    except:
        pass

#Function for saving file
def Save_File():
    if File_Status_Name:
        txt_file = open(text_file, "w")
        txt_file.write(MainText.get(1.0, END))
        txt_file.close()
    else:
        try:
            Save_As_File()
        except:
            pass

#Function for opening file
def Open_New_File():
    global File_Status_Name
    File_Status_Name = False

    #Updates the status bar
    StatusBar.config(text="New File")
    
    #updates the title
    note.title("New File - Notepad")
    MainText.delete(1.0, END)

#Function for exiting program
def Note_Exit():
    note.destroy()

def cut_text(e):
    global selected
    if e:
        selected = note.clipboard_get()
    else:
        if MainText.selection_get():
            #Grab highlighted text
            selected = MainText.selection_get()
            #delete text
            MainText.delete("sel.first","sel.last")
            note.clipboard_clear()
            note.clipboard_append(selected)

def copy_text(e):
    global selected
    if e:
        selected = note.clipboard_get()
    if MainText.selection_get():
        selected = MainText.selection_get()
        note.clipboard_clear()
        note.clipboard_append(selected)
def paste_text(e):
    global selected
    if e:
        selected = note.clipboard_get()
    else:
        if selected:
            position = MainText.index(INSERT)
            MainText.insert(position, selected)
#Main window widgets

#Creating the status bar at the bottom of the screen
StatusBar = Label(note,text = "File Name", anchor=E )
StatusBar.pack(fill = X, side=BOTTOM, pady=5)

#Creating the main frame
My_frame = Frame(note)
My_frame.pack(side=LEFT,fill=BOTH, expand=YES)

#Creating the top menu
TopMenu = Menu(note)
note.config(menu=TopMenu)

#Creating the scroll bar for the text box
text_scroll = Scrollbar(My_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#Main text box
MainText = Text(My_frame, width="45", height="20",selectbackground="yellow",selectforeground="black", font=("Times New Roman", 12), undo = True ,yscrollcommand=text_scroll.set)
MainText.pack(side=LEFT,fill=BOTH, expand=YES)

#Giving the vertical scroll bar a command
text_scroll.config(command=MainText.yview)

#Creating the file category on the top menu
file_menu = Menu(TopMenu, tearoff=False)
TopMenu.add_cascade(label = "File"   ,menu = file_menu)
file_menu.add_command(label = "New File",command= Open_New_File)
file_menu.add_command(label = "Open",command= Open_File)
file_menu.add_command(label = "Save",command= Save_File)
file_menu.add_command(label = "Save As",command= Save_As_File)
file_menu.add_separator()
file_menu.add_command(label = "Exit",command= Note_Exit)

#Creating the edit category on the top menu
edit_menu = Menu(TopMenu, tearoff=False)
TopMenu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Cut", command = lambda: cut_text(False), accelerator="(Ctrl-x)")
edit_menu.add_command(label = "Copy", command = lambda: copy_text(False), accelerator="(Ctrl-c)")
edit_menu.add_command(label = "Paste", command = lambda: paste_text(False), accelerator="(Ctrl-v)")
edit_menu.add_separator()
edit_menu.add_command(label = "Undo", command = MainText.edit_undo, accelerator="(Ctrl-z)")
edit_menu.add_command(label = "Redo", command = MainText.edit_redo, accelerator="(Ctrl-y)")


#Edit bidings
note.bind('<Control-Key-x>', cut_text)
note.bind('<Control-Key-v>', paste_text)
note.bind('<Control-Key-c>', copy_text)

note.mainloop()