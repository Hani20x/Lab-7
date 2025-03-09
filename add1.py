# Доп.задание
import requests
import tkinter as tk
from PIL import Image, ImageTk
import io
import random


def get_random_url():
    number = random.randint(1, 123)
    return f"https://randomfox.ca/images/{number}.jpg"


def update_image():
    url = get_random_url()
    response = requests.get(url)
    image_data = Image.open(io.BytesIO(response.content))
    img = ImageTk.PhotoImage(image_data)
    label.config(image=img)
    label.image = img


window = tk.Tk()
window.title("Генератор картинок")
label = tk.Label(window)
label.pack()
button = tk.Button(window, text="Случайное изображение", command=update_image)
button.place(relx=0.5, rely=0.9, anchor="center")

update_image()
window.mainloop()