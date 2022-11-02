#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: BeYoung
# Date: 2022/11/1 20:37
# Software: PyCharm

import os, pathlib
from win32comext.shell import shell, shellcon

DRIVE = None
BASE_PATH = None
IGNORE_FILE = ["README.md"]


def init_var():  # init var
    global DRIVE, BASE_PATH
    DRIVE = os.getenv("SystemDrive")  # drive path
    BASE_PATH = os.getcwd()  # base path
    print(f"{DRIVE=}\n{BASE_PATH=}\n")


def install_mingw():
    windows_path = shell.SHGetPathFromIDList(shell.SHGetSpecialFolderLocation(0, shellcon.CSIDL_WINDOWS))
    print(f"{windows_path=}")
    pass


def install_plug():
    global BASE_PATH
    if BASE_PATH is not None:
        plug_path = str(BASE_PATH) + "\\plug"
        print(os.listdir(plug_path))
        for plug_file in os.listdir(plug_path):
            global IGNORE_FILE
            if plug_file in IGNORE_FILE:
                continue

            plug_file_abs_path = plug_path + f"\\{plug_file}"
            print(f"Path:{plug_file_abs_path}\nInstalling:{plug_file}\n")
            # os.system(f"code {plug_file_abs_path}")
            pass


def install_vscode():
    vscode_path = os.getcwd() + "\\vscode\\download.exe"
    print(f"{vscode_path}\n")
    try:
        # os.system(f"{vscode_path}")
        pass
    except Exception as e:
        print(e)


def install():
    install_vscode()
    install_plug()
    install_mingw()


if __name__ == "__main__":
    init_var()
    install()
