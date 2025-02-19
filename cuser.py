# -*- coding: utf-8 -*-

from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox,Spinbox
import psycopg2
import bcrypt
import subprocess
import sys
import os



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def create_user(username, password, email_address, permissions_id):
    # Λαμβάνουμε την τιμή από το Spinbox
    try:
        # Σύνδεση με τη βάση δεδομένων PostgreSQL
        connection = psycopg2.connect(
            user="postgres",
            password="123456",
            host="localhost",
            port="5432",
            database="StoreManager",
            client_encoding='UTF8'
        )
        cursor = connection.cursor()

        # Κρυπτογράφηση του κωδικού χρήστη
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Εισαγωγή νέου χρήστη στη βάση δεδομένων
        
        insert_query = "INSERT INTO users (username, password, email) VALUES (LOWER(%s), %s, LOWER(%s)) RETURNING id"
        cursor.execute(insert_query, (username, hashed_password.decode('utf-8'),email_address))
        
        user_id = cursor.fetchone()[0]
        
        insert_permission_query = "INSERT INTO user_permissions (user_id, permissions_id) VALUES (%s, %s)"
        cursor.execute(insert_permission_query, (user_id, permissions_id,))
        
        connection.commit()
        print("Επιτυχής εισαγωγή δεδομένων στη βάση")
        # Έλεγχος εάν η εισαγωγή ήταν επιτυχής
        
        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "User created successfully!")
            #subprocess.call(["python", "login.py"])
            #sys.exit()
            
        else:
            messagebox.showerror("Error", "Failed to create user.")
            
        # Clear the Entry fields
        entry_1.delete(0, 'end')
        entry_2.delete(0, 'end')
        entry_3.delete(0, 'end')
        
    except (Exception, psycopg2.Error) as error:
        messagebox.showerror("Error", f"Error while connecting to PostgreSQL: {error}")
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")   

def on_login_button_click():
    username = entry_1.get()
    password = entry_2.get()
    email_address = entry_3.get()
    permissions_id = spinbox.get()
    create_user(username, password, email_address, permissions_id)

def on_enter_key_pressed_in_name(event):
    entry_2.focus_set()
    
def on_enter_key_pressed_in_password(event):
    entry_3.focus_set()


def on_enter_key_pressed_in_email(event):
    button_1.focus_set()
    on_login_button_click()
            
window = tk.Tk()
window.title("Cuser")
window.geometry("304x450")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 450,
    width = 304,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    304.0,
    49.0,
    fill="#D6D6D6",
    outline="")

canvas.create_text(
    32.0,
    12.0,
    anchor="nw",
    text="StoreManager Pro",
    fill="#000000",
    font=("KronaOne Regular", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: create_user (entry_1.get(), entry_2.get(),entry_3.get(), spinbox.get() ),
    relief="flat"
)

button_1.place(
    x=160.0,
    y=383.0,
    width=128.0,
    height=32.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))

entry_bg_1 = canvas.create_image(
    132.0,
    156.0,
    image=entry_image_1
)

entry_1 = Entry(
    bd=0,
    bg="#EBEBEB",
    fg="#000716",
    highlightthickness=0
)

entry_1.place(
    x=22.0,
    y=92.0,
    width=220.0,
    height=20.0
)

entry_1.bind("<Return>", on_enter_key_pressed_in_name)

canvas.create_text(
    12.0,
    120.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Inter", 16 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))

entry_bg_2 = canvas.create_image(
    132.0,
    103.0,
    image=entry_image_2
)

entry_2 = Entry(
    bd=0,
    bg="#EBEBEB",
    fg="#000716",
    highlightthickness=0,
    show="*"
)

entry_2.place(
    x=22.0,
    y=145.0,
    width=220.0,
    height=20.0
)

entry_2.bind("<Return>", on_enter_key_pressed_in_password)


canvas.create_text(
    12.0,
    67.0,
    anchor="nw",
    text="Name",
    fill="#000000",
    font=("Inter", 16 * -1)
)

######Email address entry###### entry_3
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))

entry_bg_3 = canvas.create_image(
    132.0,
    235.0,
    image=entry_image_3
)

entry_3 = Entry(
    bd=0,
    bg="#EBEBEB",
    fg="#000716",
    highlightthickness=0
    #show="*"
)


entry_3.place(
    x=22.0,
    y=220.0,
    width=220.0,
    height=20.0
)

entry_3.bind("<Return>", on_enter_key_pressed_in_email)

#entry_2
canvas.create_text(
    12.0,
    190.0,
    anchor="nw",
    text="Email address",
    fill="#000000",
    font=("Inter", 16 * -1)
)


spinbox = Spinbox(window, 
                from_=1, 
                to=3, 
                width=10, 
                relief="sunken", 
                repeatdelay=500, 
                repeatinterval=100,
                font=("Inter", 16 * -1),
                bg="lightgrey", 
                fg="blue", )

spinbox.place(
    x=22.0,
    y=290.0,
    width=70.0,
    height=20.0
)
# Setting options for the Spinbox
spinbox.config(state="normal", cursor="hand2", bd=3, justify="center", wrap=True)

canvas.create_text(
    12.0,
    260.0,
    anchor="nw",
    text="Level",
    fill="#000000",
    font=("Inter", 16 * -1)
)


window.resizable(False, False)
window.mainloop()
