from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import time

root= Tk()
root.title("Eşleştirme Oyunu")

images_name=("bird.png","cat.png","dog.png","donkey.png","horse.png","lion.png","monkey.png","crocodile.png")
global button_image,button,click_button_1,click_button_2,buttons,active_buttons, score
global buttons_click
score=0
buttons_click=0
buttons=[]
active_buttons= []
button_image =[""]*16


class image_assignment:
    def __init__(self):# ekran açıldığında otomatik olarak resimleri dağıtır
        
        while "" in button_image:
            for image in images_name:
                rand=random.randint(0,15)
                if button_image.count(image)<2 and button_image[rand]=="" :
                    button_image[rand] = image
    
def insert_image(buttons,indeks):# tıklanan butona resim yükler ve kaç butona tıkladığını kontrol eder
    global buttons_click,click_button1_indeks,click_button2_indeks,click_button_1,click_button_2
    if buttons["text"]!=" ":
        i="images/"+button_image[indeks]
        button_width = buttons.winfo_width()
        button_height = buttons.winfo_height()
        image = Image.open(i).convert("RGB")
        image = image.resize((button_width, button_height))
        photo = ImageTk.PhotoImage(image)
        buttons.config(image=photo,text=" ", compound=CENTER) 
        buttons.image = photo  # Resim referansını sakla
        buttons_click+=1
        
        if buttons_click==1:
            click_button_1=buttons
            click_button1_indeks = indeks
        else:
            click_button_2=buttons
            click_button2_indeks = indeks
            button_activation_pacification(0,click_button_1,click_button_2)
            
        if buttons_click==2:
             control(click_button1_indeks,click_button_1,click_button2_indeks,click_button_2)

def control(b1,b_1,b2,b_2) :# butonlardan açılan resimlerin eşliğini kontrol eder
    global buttons_click,click_button1_indeks,click_button2_indeks,score
    if button_image[b1] == button_image[b2]:
        score+=1
        score_refresh()
        if score==8:
            messagebox.showinfo("Eşleşme","Tüm Eşleri Buldunuz Tebrikler")
        else:
            messagebox.showinfo("Eşleşme","Eş buldunuz tebrikler")
            active_buttons.append(b_1)
            active_buttons.append(b_2)
            button_activation_pacification(1,0,0)
            
    else:
        game_area.after(1000, lambda: clear_buttons(b_1, b_2))

    buttons_click=0
    click_button1_indeks= None
    click_button2_indeks= None

def clear_buttons(b1,b2):#butonlarda ki resimler eş değilse resimleri kaldırma
    b1.config(image="",text="")
    b2.config(image="",text="")
    b1.image=None
    b2.image=None
    button_activation_pacification(1,0,0)

def button_activation_pacification(activation,i1,i2):# kullanıcı 2 butondan fazla açmasını engelliyor
    global buttons,click_button_indeks

    if activation==1:
        for i in buttons:
             i.config(state="normal")
    else:
        for i in buttons:
            if i in(i1,i2) or i in active_buttons :
                continue
            i.config(state="disabled")
        

def score_refresh():# skor tablosunu güncelliyor
    global score
    score_label= Label(score_area,text=f"Skor : {score}",font=("Arial",20),bg="white")
    score_label.grid(row=0,column=0,padx=10,pady=10)
    

load=image_assignment()
game_area=Frame(root,bg="white")
game_area.grid(row=1,column=0,sticky=S+N+E+W)
score_area=Frame(root,bg="white")
score_area.grid(row=0,column=0,sticky=S+N+E+W)
score_refresh()


for i in range(0,16):# butonlar oluşturuluyor
    button_name=f"button{i}"
    button_name = Button(game_area, font=('Arial 30 bold'), command=lambda i=i: insert_image(buttons[i], i))
    button_name.grid(row=i // 4, column=i % 4, sticky=S + N + E + W)
    buttons.append(button_name)

root.mainloop()
