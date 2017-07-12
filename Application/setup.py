# -*- coding: utf-8 -*-

from setuptools import setup
#import macholib_patch

APP = ['iOSAppIconGenerator.py']
APP_NAME = "iOSAppIconGenerator"
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'packages': 'PIL',
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "Generates iOS App Icons.",
        'CFBundleIdentifier': "com.dorukgezici.iOSAppIconGenerator",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': u"Copyright © 2017, Doruk Gezici, All Rights Reserved"
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
