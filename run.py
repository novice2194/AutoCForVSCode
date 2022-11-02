#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: BeYoung
# Date: 2022/11/1 20:37
# Software: PyCharm
from __future__ import print_function

import os
import ctypes, sys

DRIVE = None
BASE_PATH = None
IGNORE_FILE = ["README.md"]


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        print(e)
        return False


def init_var():  # init var
    global DRIVE, BASE_PATH
    DRIVE = os.getenv("SystemDrive")  # drive path
    BASE_PATH = os.getcwd()  # base path
    print(f"{DRIVE=}\n{BASE_PATH=}\n")


def install_mingw():
    global BASE_PATH, DRIVE
    if DRIVE is not None:
        windows_path = DRIVE
        if BASE_PATH is not None:
            windows_path = str(windows_path) + "\\mingw64"
            mingw_path = str(BASE_PATH) + "\\mingw64"
            print(f"{windows_path=}\n{mingw_path=}")
            # todo:Remember to cancel
            os.system(f"copy {mingw_path} {windows_path}")
            os.system(f"path=%path%;{windows_path}")
            pass


def install_plug():
    global BASE_PATH
    code_path = input("Code PATH:\n")
    if BASE_PATH is not None:
        plug_path = str(BASE_PATH) + "\\plug"
        print(os.listdir(plug_path))
        for plug_file in os.listdir(plug_path):
            global IGNORE_FILE
            if plug_file in IGNORE_FILE:
                continue

            plug_file_abs_path = plug_path + f"\\{plug_file}"
            print(f"Path:{plug_file_abs_path}\nInstalling:{plug_file}\n")
            # todo:Remember to cancel
            os.system(f"{code_path} {plug_file_abs_path}")
            pass


def install_vscode():
    vscode_path = os.getcwd() + "\\vscode\\download.exe"
    print(f"{vscode_path}\n")
    try:
        # todo:Remember to cancel
        os.system(f"{vscode_path}")
        pass
    except Exception as e:
        print(e)


def install():
    install_vscode()
    install_plug()
    install_mingw()


if __name__ == "__main__":
    if is_admin():
        init_var()
        install()
    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:  # in python2.x
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
