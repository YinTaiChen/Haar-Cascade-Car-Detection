import tkinter as tk
from tkinter import filedialog
import PIL
from PIL import Image, ImageTk
import urllib.request
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import math

import matplotlib.backends.backend_tkagg

myFormats = [('JPEG / JFIF','*.jpg'), ('Windows Bitmap','*.bmp'), ('Portable Pix Map', '*.ppm'), ('Portable Network Graphics','*.png'),('CompuServer GIF','*.gif')]

window = tk.Tk()
window.title('AIP 60647041S')
ww, wh = window.winfo_screenwidth()-200, window.winfo_screenheight()-200

info_1 = tk.Label(window)
info_2 = tk.Label(window)

box1 = tk.Label(window)
box2 = tk.Label(window)
box3 = tk.Label(window)

bar = tk.Menu(window)

def open_image():
    global image
    global directory

    window.image =  filedialog.askopenfilename(initialdir="/", filetypes=myFormats, title='Select a image')
    directory = window.image

    if len(directory) > 0:
        image = Image.open(window.image)
        img = ImageTk.PhotoImage(image)
        img_width, img_height = img.width(), img.height()

        img = resize(image)

        info_1.config(text=window.image)
        info_1.grid(column=1, row=0)

        info_2.config(text=str(img_width)+'x'+str(img_height))
        info_2.grid(column=1, row=1)

        box1.config(image=img, width=ww/2, height=wh+100)
        box1.image = img
        box1.grid(column=1, row=2)

        box2.config(image=img, width=ww/2, height=wh+100)
        box2.image = img
        box2.grid(column=2, row=2)

        image_menu.entryconfigure('Save', state='normal')
        image_menu.entryconfigure('Show', state='normal')
        tool_menu.entryconfigure('Car Detection', state='normal')
        tool_menu.entryconfigure('Undo', state='normal')
# def select_and_show()

def resize(image):
    img = ImageTk.PhotoImage(image)

    img_width, img_height = img.width(), img.height()
    img_w, img_h = img.width(), img.height()

    if img_w > (ww / 2):
        scale = ww / (2 * img_w)
        img_w, img_h = int(img_w * scale), int(img_h * scale)
        image_r = image.resize((img_w, img_h), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image_r)

    if img_h > wh:
        scale = wh / img_h
        img_w, img_h = int(img_w * scale), int(img_h * scale)
        image_r = image.resize((img_w, img_h), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image_r)

    return img

def save_image():
    global to_show

    filename = filedialog.asksaveasfilename(defaultextension="*.*", filetypes=myFormats, title='Save image as...')
    if len(filename) > 0:
        to_show.save(filename)
# def save_image(image)

def undo():
    global image

    image = Image.open(directory)
    img = resize(image)
    box2.config(image=img, width=ww/2, height=wh+100)
    box2.image = img

def car_detection():
    global directory
    global to_show

    ALPHA = 0.1
    cascades = ["1", "11", "13", "22", "39", "42", "187", "342", "723"]
    name = "sample_10"
    test_image = cv2.imread(directory)
    overlay = test_image.copy()
    output = test_image.copy()

    for index in cascades:
        test_gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
        height, width = test_gray.shape

        cascade_directory = "./chosen/"+index+"/cascade.xml"
        if os.path.isfile(cascade_directory):
            div = 1
            car_cascade = cv2.CascadeClassifier(cascade_directory)
            cars = car_cascade.detectMultiScale(test_gray, minSize=(int(height/div), int(width/div)))

            while(len(cars)==0):
                div += 1
                cars = car_cascade.detectMultiScale(test_gray, minSize=(int(height/div), int(width/div)))

            for (x, y, w, h) in cars:
                cv2.rectangle(overlay, (x, y), (x+w, y+h), (0, 0, 255), -1)

        cv2.addWeighted(overlay, ALPHA, output, 1 - ALPHA, 0, output)

    output = output.astype(np.uint8)
    output = PIL.Image.fromarray(output)
    b, g, r = output.split()
    to_show = Image.merge("RGB", (r, g, b))
    output_PIL = resize(to_show)

    box2.config(image=output_PIL, width=ww/2, height=wh+100)
    box2.image = output_PIL
    box2.grid(column=2, row=2)

window_menu = tk.Menu(bar, tearoff=0)

image_menu = tk.Menu(bar, tearoff=0)
bar.add_cascade(label='Image', menu=image_menu)
image_menu.add_command(label='Import', command=open_image)
image_menu.add_separator()
image_menu.add_command(label='Save', command=save_image)
image_menu.add_command(label='Show', command= lambda: to_show.show())

tool_menu = tk.Menu(bar, tearoff=0)
bar.add_cascade(label='Tool', menu=tool_menu)
tool_menu.add_command(label='Car Detection', command=car_detection)
tool_menu.add_separator()
tool_menu.add_command(label='Undo', command=undo)

image_menu.entryconfigure('Save', state='disabled')
image_menu.entryconfigure('Show', state='disabled')
tool_menu.entryconfigure('Car Detection', state='disabled')
tool_menu.entryconfigure('Undo', state='disabled')

window.config(menu=bar)

window.mainloop()
