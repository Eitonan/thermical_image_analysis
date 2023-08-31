# To control and add parameters to the analysis of thermical picture
# Print and/or save pictures 
# Choose the colormap and the values of the treshold (max number of threshold : 4)
# Author : Antoine Kerneis
# Last version : 17/07/2023



import tkinter as tk
from tkinter import *
import os
from PIL import ImageTk,Image
import main


class Display(object):

    def __init__(self): 
        self.images = []
        self.imgIndex = 0
        self.master= Tk()
        self.master.title("Choose parameters")
        self.ImgName='list_not_empty'
        self.framePhoto = Frame(self.master, bg='gray50',relief = RAISED, width=800, height=600, bd=4)
        self.framePhoto.pack(side='right')
        self.save_var = BooleanVar()
        self.show_var = BooleanVar()
        self.hist_var = BooleanVar()


        # Place Widgets
        prevBtn = Button(self.framePhoto, text='Previous', command=lambda s=self: s.getImgOpen('prev')).place(x=140, y=300, anchor=SE)
        nextBtn = Button(self.framePhoto, text='Next', command=lambda s=self: s.getImgOpen('next')).place(x=310, y=300, anchor=SE)
        RunBtn = Button(self.framePhoto, text= 'Run' , command=lambda s=self: s.Run(), bg = 'light blue', width= 10).place(x=700,y=300, anchor=SE)
        Txt_label = Label(master=self.framePhoto,text ='Enter the values of threshold',justify='center').place(x=50,y=85,width=200)
        Txt_color_label = Label(master=self.framePhoto,text ='Select a colormap',justify='center').place(x=85,y=230,width=250)
        SaveBtn = Checkbutton(self.framePhoto, text= 'Save image and analysis', variable= self.save_var).place(x=170, y= 425, anchor= SE)
        ShowBtn = Checkbutton(self.framePhoto, text= 'Show image', variable= self.show_var).place(x=350, y= 425, anchor= SE)
        HistBtn = Checkbutton(self.framePhoto, text= 'Show Histogramme', variable= self.hist_var).place(x=280, y= 475, anchor= SE)


        # Place Entry

        self.treshold_1_entry = tk.Entry(self.framePhoto,justify='center')
        self.treshold_1_entry.place(x=75,y=120)

        self.treshold_2_entry = tk.Entry(self.framePhoto,justify='center')
        self.treshold_2_entry.place(x=75,y=135)

        self.treshold_3_entry = tk.Entry(self.framePhoto,justify='center')
        self.treshold_3_entry.place(x=75,y=150)

        self.treshold_4_entry = tk.Entry(self.framePhoto,justify='center')
        self.treshold_4_entry.place(x=75,y=165)
        
        self.getImgList('./Colormap','.gif')
        mainloop()

    def getImgList(self, path, ext):    #Run through the given directory to get the colormap image
        imgList = [os.path.normcase(f) for f in os.listdir(path)]
        imgList = [os.path.join(path, f) for f in imgList if os.path.splitext(f)[1] == ext]
        self.images.extend(imgList)   

    
    
    def getImgName(self):     #Give the name of the file (here the name of the colormap for display convenience)
       path=self.images[self.imgIndex]
       name=str(path[11:-4])
       return name
       
    def isfloat (self,string):
      if string is None:
        return False
      try:
        float(string)
        return True
      except:
        return False
      
    def getListTreshold (self):   #Give the list of threshodl values given by the user. If the user didn't give one (''), don't generate an error
       
       treshold_1 = self.treshold_1_entry.get()
       treshold_2 = self.treshold_2_entry.get()
       treshold_3 = self.treshold_3_entry.get()
       treshold_4 = self.treshold_4_entry.get()

       ListTreshold = []
       
       if treshold_1 != '':
          if self.isfloat(treshold_1) and float(treshold_1)!=0.0:
            treshold_1 = float(treshold_1)
            ListTreshold.append(treshold_1)
          else:
            treshold_1 = str('None')
            ListTreshold.append(treshold_1)

       if treshold_2 != '':
          if self.isfloat(treshold_2) and float(treshold_2)!=0.0:
            treshold_2 = float(treshold_2)
            ListTreshold.append(treshold_2)
          else:
            treshold_2 = str('None')
            ListTreshold.append(treshold_2)
        
       if treshold_3 != '':
          if self.isfloat(treshold_3) and float(treshold_3)!=0.0:
            treshold_3 = float(treshold_3)
            ListTreshold.append(treshold_3)
          else:
            treshold_3 = str('None')
            ListTreshold.append(treshold_3)
        
       if treshold_4 != '':
          if self.isfloat(treshold_4) and float(treshold_4)!=0.0:
            treshold_4 = float(treshold_4)
            ListTreshold.append(treshold_4)
          else:
            treshold_4 = str('None')
            ListTreshold.append(treshold_4)
       
       return ListTreshold
    
    
    
    def Run(self):      #Run the traitment. If no colormap was selectionnated, default colormap is inferno
        
        List = self.getListTreshold()
        Save = self.save_var.get()
        Show = self.show_var.get()
        Hist = self.hist_var.get()
        if self.ImgName == 'list_not_empty':
           self.ImgName='inferno'
        main.Main(self.ImgName, List, Save, Show, Hist)
        
        return None

    def getImgOpen(self,seq):       #Run through all the image name and display the current image
        if seq=='ZERO':
         self.imgIndex = 0
        elif (seq == 'prev'):
            if (self.imgIndex == 0):
             self.imgIndex = len(self.images)-1
            else:
             self.imgIndex -= 1
        elif(seq == 'next'):   
            if(self.imgIndex == len(self.images)-1):
             self.imgIndex = 0
            else:
              self.imgIndex += 1 

        self.ImgName=self.getImgName()
        self.text = Label(text = self.ImgName).place(x=460,y=520,width=100)
        self.masterImg = Image.open(self.images[self.imgIndex]) 
        self.masterImg.thumbnail((400,400))
        self.img = ImageTk.PhotoImage(self.masterImg)
        label = Label(image=self.img)
        label.image = self.img # keep a reference!
        label.pack()
        label.place(x=500,y=100)
        return   
     
d = Display()
d.getImgOpen('next')





