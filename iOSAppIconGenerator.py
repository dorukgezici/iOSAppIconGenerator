#!/usr/bin/env python3

import os, sys
import json
from PIL import Image
from PIL import ImageFilter

valid_images = [".jpg",".png"]
filename = None
for f in os.listdir():
    ext = os.path.splitext(f)[1]
    if ext.lower() in valid_images:
        filename = f
        break

print("\n<- iOS App Icon Generator Script by DG ->\nPlease make sure the script is in the same folder as the image.")
if filename is None:
    sys.exit("Couldn't find an image(.jpg/.png) in the folder. Please try again.")

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

if os.access("AppIcon.appiconset", os.W_OK) == False:
    os.mkdir("AppIcon.appiconset")
file = open("AppIcon.appiconset/Contents.json", mode="w")
json.dump(json_data, file, indent=4, sort_keys=True, separators=(',', ':'))
file.close()

def get_size(image):
    size_str = image["size"]
    i = size_str.find("x")
    size = (float(size_str[:i]),float(size_str[i+1:]))
    scale_str = image["scale"]
    j = scale_str.find("x")
    scale = int(scale_str[:j])
    return (int(scale * float(size[0])), int(scale * float(size[1])))

with open("AppIcon.appiconset/Contents.json", mode="r") as data_file:
    data = json.load(data_file)
    images = data["images"]
    try:
        im = Image.open(filename)
        print("Image found:", im.format, im.size, im.mode)
        print("-"*50)
    except IOError:
        print("Image not found")

for image in images:
    size = get_size(image)
    out = im.resize(size, Image.ANTIALIAS)
    out.save("AppIcon.appiconset/"+image["filename"], format="PNG")
    print("Image generated: {0}".format(size))

print("-"*50, "\nGenerator completed. Copy the 'AppIcon.appiconset' folder to your Xcode project assets and your app icon is good to go!\nGitHub: @dorukgezici -> https://github.com/dorukgezici/iOSAppIconGenerator.git\n")
