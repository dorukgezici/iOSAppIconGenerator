#!/usr/bin/env python3

import os, sys, json, subprocess
from PIL import Image, ImageFilter
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory

class Data:
    supported_img_types = [".jpg", ".png"]
    image_path = ""
    save_path = os.path.dirname(__file__)
    if ".app" in save_path:
        while not save_path.endswith(".app"):
            save_path = os.path.dirname(save_path)

json_data = {
    "images":[
        {
            "idiom":"iphone",
            "size":"20x20",
            "scale":"2x",
            "filename":"Icon-App-20x20@2x.png"
        },
        {
            "idiom":"iphone",
            "size":"20x20",
            "scale":"3x",
            "filename":"Icon-App-20x20@3x.png"
        },
        {
            "idiom":"iphone",
            "size":"29x29",
            "scale":"1x",
            "filename":"Icon-App-29x29@1x.png"
        },
        {
            "idiom":"iphone",
            "size":"29x29",
            "scale":"2x",
            "filename":"Icon-App-29x29@2x.png"
        },
        {
            "idiom":"iphone",
            "size":"29x29",
            "scale":"3x",
            "filename":"Icon-App-29x29@3x.png"
        },
        {
            "idiom":"iphone",
            "size":"40x40",
            "scale":"2x",
            "filename":"Icon-App-40x40@2x.png"
        },
        {
            "idiom":"iphone",
            "size":"40x40",
            "scale":"3x",
            "filename":"Icon-App-40x40@3x.png"
        },
        {
            "idiom":"iphone",
            "size":"57x57",
            "scale":"1x",
            "filename":"Icon-App-57x57@1x.png"
        },
        {
            "idiom":"iphone",
            "size":"57x57",
            "scale":"2x",
            "filename":"Icon-App-57x57@2x.png"
        },
        {
            "idiom":"iphone",
            "size":"60x60",
            "scale":"2x",
            "filename":"Icon-App-60x60@2x.png"
        },
        {
            "idiom":"iphone",
            "size":"60x60",
            "scale":"3x",
            "filename":"Icon-App-60x60@3x.png"
        },
        {
            "idiom":"ipad",
            "size":"20x20",
            "scale":"1x",
            "filename":"Icon-App-20x20@1x.png"
        },
        {
            "idiom":"ipad",
            "size":"20x20",
            "scale":"2x",
            "filename":"Icon-App-20x20@2x.png"
        },
        {
            "idiom":"ipad",
            "size":"29x29",
            "scale":"1x",
            "filename":"Icon-App-29x29@1x.png"
        },
        {
            "idiom":"ipad",
            "size":"29x29",
            "scale":"2x",
            "filename":"Icon-App-29x29@2x.png"
        },
        {
            "idiom":"ipad",
            "size":"40x40",
            "scale":"1x",
            "filename":"Icon-App-40x40@1x.png"
        },
        {
            "idiom":"ipad",
            "size":"40x40",
            "scale":"2x",
            "filename":"Icon-App-40x40@2x.png"
        },
        {
          "size" : "50x50",
          "idiom" : "ipad",
          "filename" : "Icon-Small-50x50@1x.png",
          "scale" : "1x"
        },
        {
          "size" : "50x50",
          "idiom" : "ipad",
          "filename" : "Icon-Small-50x50@2x.png",
          "scale" : "2x"
        },
        {
            "idiom":"ipad",
            "size":"72x72",
            "scale":"1x",
            "filename":"Icon-App-72x72@1x.png"
        },
        {
            "idiom":"ipad",
            "size":"72x72",
            "scale":"2x",
            "filename":"Icon-App-72x72@2x.png"
        },
        {
            "idiom":"ipad",
            "size":"76x76",
            "scale":"1x",
            "filename":"Icon-App-76x76@1x.png"
        },
        {
            "idiom":"ipad",
            "size":"76x76",
            "scale":"2x",
            "filename":"Icon-App-76x76@2x.png"
        },
        {
            "idiom":"ipad",
            "size":"83.5x83.5",
            "scale":"2x",
            "filename":"Icon-App-83.5x83.5@2x.png"
        }
    ],
    "info":{
        "version":1,
        "author":"Doruk Gezici"
    }
}

def get_image_path():
    Data.image_path = askopenfilename()
    choose_file_button.configure(bg="green")
    choose_save_button.update()
    return Data.image_path

def get_save_path():
    Data.save_path = askdirectory()
    choose_save_button.update()
    choose_save_button.configure(bg="green")
    return Data.save_path


def get_size(image):
    size_str = image["size"]
    i = size_str.find("x")
    size = (float(size_str[:i]),float(size_str[i+1:]))
    scale_str = image["scale"]
    j = scale_str.find("x")
    scale = int(scale_str[:j])
    return (int(scale * float(size[0])), int(scale * float(size[1])))

def open_saved():
    subprocess.call(["open", Data.save_path + "/AppIcon.appiconset"])


def run():
    if Data.image_path == "":
        output_label["text"] = "Choose the image file first."
        return
    if os.access("{}/AppIcon.appiconset".format(Data.save_path), os.W_OK) == False:
        os.mkdir("{}/AppIcon.appiconset".format(Data.save_path))
    file = open("{}/AppIcon.appiconset/Contents.json".format(Data.save_path), mode="w")
    json.dump(json_data, file, indent=4, sort_keys=True, separators=(',', ':'))
    file.close()

    with open("{}/AppIcon.appiconset/Contents.json".format(Data.save_path), mode="r") as data_file:
        data = json.load(data_file)
        images = data["images"]
        try:
            im = Image.open(Data.image_path)
            output_label["text"] = "Image specs: {} {} {}\n{}\n".format(im.format, im.size, im.mode, "-"*35)
            for image in images:
                size = get_size(image)
                out = im.resize(size, Image.ANTIALIAS)
                out.save("{}/AppIcon.appiconset/{}".format(Data.save_path, image["filename"]), format="PNG")
                output_label["text"] += "Image generated: {}\n".format(size)
            open_saved_button.grid(row=1, column=0, columnspan=2, sticky=tk.W+tk.E)
        except IOError:
            output_label["text"] = "Please select a supported image file."


def clear():
    output_label["text"] = ""
    open_saved_button.grid_remove()
    Data.image_path = ""
    Data.save_path = os.path.dirname(__file__)
    if ".app" in Data.save_path:
        while not Data.save_path.endswith(".app"):
            Data.save_path = os.path.dirname(Data.save_path)

root = tk.Tk()
root.title("iOS App Icon Generator by @dorukgezici")
root.geometry("640x480+350+150")

choose_frame = tk.Frame(root)
choose_frame.pack(padx=30, pady=30)

choose_file_labelframe = tk.LabelFrame(choose_frame, text="Choose Image File")
choose_file_labelframe.grid(row=0, column=0, padx=10)
choose_file_button = tk.Button(choose_file_labelframe, text="Image", command=get_image_path)
choose_file_button.pack()

choose_save_labelframe = tk.LabelFrame(choose_frame, text="Choose Path to Save")
choose_save_labelframe.grid(row=0, column=1, padx=10)
choose_save_button = tk.Button(choose_save_labelframe, text="Directory", command=get_save_path)
choose_save_button.pack()

open_saved_button = tk.Button(choose_frame, text="Show in Finder", command=open_saved)
open_saved_button.grid(row=1, column=0, columnspan=2, sticky=tk.W+tk.E)
open_saved_button.grid_remove()

output_label = tk.Label(root, text="")
output_label.pack()

control_frame = tk.Frame(root)
control_frame.pack()

run_button = tk.Button(control_frame, text="RUN", command=run)
run_button.pack(side="left")

clear_button = tk.Button(control_frame, text="CLEAR", command=clear)
clear_button.pack(side="left")

quit_button = tk.Button(control_frame, text="QUIT", command=root.destroy)
quit_button.pack(side="right")

root.lift()
root.mainloop()
