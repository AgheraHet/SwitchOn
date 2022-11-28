# SwitchOn.IO Internship Assignment

Here I have developed a small python code which will read the data from the database which is having unit ID and status(Good or Bad) and then it will show the whole data with image realted to that unit ID and the status.

## prerequisite

To run this project you need proper setup of **python** and **MongoDB**

## Tech Stack

**Database:** MongoDB

**Language:** python

## library

- opencv
- pyside2
- PyQt5
- Pyautogui
- pymongo
- numpy
- sys
- datetime
- os

## Installation

Install all the Libraries using following commands

```bash
    pip install opencv-python
    pip install PySide2
    pip install PyAutoGUI
    pip install pymongo
    pip install numpy
```

## Tools

- **Designer:** I have used this tool to design the whole GUI also with help of this we can get python code of the GUI.

## Files & Folders

### pic

This folder contains 100 images of botttles. All the images in this folder are named 1 to 100(unit ID)

### insertIntoDB.py

This python file will first generat 10 random numbers and then it will read simply do the entry in database. When index is found in 10 random numbers it will put a status as **Bad** otherwise it will put status as **GOOD**

### tab_ui.py

This file contains the code which is helpful to create GUI.

### main.py

This pyhton file is the main part of the project this file will first read the data from the Database and then it will show the image and status of each and every data entry on new window also this window will contain 3 difffrent tab name All,Good,Bad. So that user can easily indentify all the Good and Bad botttles

## Steps

### step 1

First of all run **insertIntoDB.py** file in your python envirinment after installing all the libraries.

- It will fisrt generate 10 random numbers.

- We will assign status as **Bad** to those images which is having index which is present in random numbers.

- Then it will simply insert all the data in to MonogDB. In this it will create a Database named **SwitchOn** and then it will insert all the data in the collection called **Status**. In each document it will contain sku_id(which is generated according to timestamp),Unit ID and status.

- Below images show the data and collection and also data which is intserted.
- Here I have defined 10 Bad and 90 Good images. (index of bad images may different from the image as it is generate randomly)

![image](https://drive.google.com/uc?export=view&id=1r2FAvAmp1S5buISUuP-xzVGlK-gRY2jk)

![image](https://drive.google.com/uc?export=view&id=1z7TH_LHhWJfXBndn1tYnM93-3QJRHVvT)

### step 2

Now run **main.py** file.

- Now new window will open which will have 3 different tab (All, Good, Bad)

![image](https://drive.google.com/uc?export=view&id=1HoOoqaF0IYhhlZvIpxb22Idln7W72EED)

- Tab with name Bad will contain all the Bad bottles

![image](https://drive.google.com/uc?export=view&id=1iuPxiZSD2dgMeczUbP4YmclV-kx3NhB7)

- Tab with name Good will contain all the Good bottles

![image](https://drive.google.com/uc?export=view&id=1ipSAlunO9x-LQKl1mHMvY3AZ4OSohLkP)
