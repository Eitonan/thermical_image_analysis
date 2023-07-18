from PIL.Image import *
import os
import tkinter
from tkinter.filedialog import askdirectory


directory = askdirectory()
for i in os.listdir(directory):  
         if (i=="Rainbow.gif" or i == "Viridis.gif"):            
             new_directory=(directory + "/" +str(i))
             imgpil = open(new_directory).convert('RGB')
             imgpil = imgpil.rotate(angle=90)
             imgpil = imgpil.resize((37,947))
             imgpil.show()
             name = directory + "/new_"+i
             imgpil.save(name,format="gif")



