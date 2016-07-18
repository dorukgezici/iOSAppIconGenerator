# iOSAppIconGenerator
iOSAppIconGenerator - written in Python by @dorukgezici

Hello fellow iOS Developers! Today I decided to stop using makeappicon.com to generate my app icons. Instead, I coded a small script in Python which works like a charm. You put the image you want to use as your app icon in the same directory as the script and the script will generate all the resized images you need and put them in the Xcode format “AppIcon.appiconset” folder. The only thing left for you to do is to drag that folder in your Xcode project assests.

How to use my script:

1)  You have to have python 3.x installed. Look at python.org for instructions.

2)  Download the script "iOSAppIconGenerator.py".

3)  The image you want to use must be in the same folder as the script (*.png or *.jpg).

4)  You have two options for running the script. You can run it with Python Launcher if you installed python from python.org or you can just run it from terminal. So 2 options are:
  - Just right click the script and open with Python Launcher. The script will automatically find the image in its current     folder and create a new folder within with resized images and a contents.json file.
  - Change directory (cd) to the directory you have the script and the picture from terminal. Then run this command without the quotes: “python3 iOSAppIconGenerator.py” or “python iOSAppIconGenerator.py”.

The asset folder is ready! Just drag the created folder in your Xcode project assets. Don’t forget to delete the old empty asset folder named “AppIcon” and rename the new folder to the same name.
Please keep in mind that this is just a 2 hours project and the script has no error handling whatsoever. So if you come across any bugs leave a comment below!
