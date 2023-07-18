# To compute thermical analysis on excel (.xlsx) files
# Print and/or save pictures with a gradient of temperature 
# Controled via a tkinter interface
# Author : Antoine Kerneis
# Last version : 17/07/2023



import pandas as pd
from tkinter.filedialog  import askdirectory
import os
from tqdm import tqdm
import time
import numpy as np
from PIL import Image
from matplotlib import cm
import matplotlib.pyplot as plt



def Main (cmap = 'inferno', List_treshold = None, Save = True, Show = True):   
    directory=askdirectory()
    
    if Save == True:
        path2save=where_to_save()
    else:
        path2save = None  

    for i in tqdm(os.listdir(directory),"Progress "):  
         if (i.endswith(".xlsx") and not i.startswith("~$")):           
             new_directory=(directory + "/" +str(i))
             assert os.path.isfile(new_directory)
             with open(new_directory,"r") as f :
                 pass
             df_tableau=pd.read_excel( io= new_directory, header=5, index_col="Unnamed: 6", 
                                      usecols=lambda x: x not in ['Unnamed: 0','Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5'], 
                                      converters={'convert_float':False})
             df_Infos=pd.read_excel( io= new_directory, header=3, converters={'convert_float':False}, usecols=lambda x: 'Unnamed' not in x,
                                    nrows=1)
             List_image=tratamiento(df_tableau,df_Infos,List_treshold,path2save,i,cmap, Save)

             if Show == True :
                Image_show(List_image,List_treshold,cmap) 
             time.sleep(0.0001)
    print("End with sucess")
    return None


def tratamiento (df,df_Infos,List_treshold,path2save,name_file,cmap, Save):    #Do the traitment, step by step, of the directory
    List_image=[]
    temp_max=(df_Infos.iloc[0,5]-32)*(5/9)
    for i in range (0,len(List_treshold)): 
        df2use=df.copy()                                                        #create a copy of the dataframe to not change the values of the original one
        df_Celsius=Put2Celsius(df2use)                                          #Convert all °F to °C and return a dataframe in °C
        array=df2array(df_Celsius)                                              #Convert the dataframe to an array
        image=array2image(array,temp_max,List_treshold[i],cmap)                 #Convert the array to an image : normalize each pixel and do the gradient of temperature
        if Save == True:
            name_image=str(name_file[:-4] )+ "_treshold_" +str(List_treshold[i])    #Create file name to save
            image.save(path2save +"/" + name_image + ".png", format="png")          #Save the picture in png
        List_image.append(image)
    return List_image

def Put2Celsius (df): #Convert °F to °C
    row,col=df.shape
    for i in range (row):
        for j in range(col):
            df.iloc[i,j]=(df.iloc[i,j]-32)*(5/9)
    return df


def df2array (df):      #tranform the dataframe into an numpy array
  return df.to_numpy()

def array2image(array,temp_max,treshold,cmap):     #normalise the value of each pixel then tranform the array to an PIL Image
    row,col=np.shape(array)
    temp_min=temp_max-treshold
    for i in range(row):
        for j in range(col):
            array[i][j]=linear(array[i][j],max=temp_max,min=temp_min)

    cm = plt.get_cmap(cmap)  
    colored_image = cm(array)      
    im=Image.fromarray((colored_image[:, :, :3] * 255).astype(np.uint8))
    return im

def linear (x,min,max):     #Create a temperature gradient with a linear function :
    a=1/(max-min)           #If the temperature is less than min (temp_min=temp_max-treshold) set the value to 0
    b=1-a*max               #Else, return a value between 0 and 1
    if x<min:
        return 0
    else:
        return a*x+b


def Image_show(List_image, titles=None,color=None):    #to display image
    ''' display a list of images '''
    n = len(List_image)
    if len(titles)== 1:
        image=List_image[0]
        plt.imshow(image, cmap=color)
        

    else:
        assert titles is None or len(titles) == n, "Titles should have the same length as tensors"
        fig, axs = plt.subplots(1,n)
        for i, (ax, list_image) in enumerate(zip(axs, List_image)):
            image = List_image[i]
            im=ax.imshow(image,cmap=color)
            title = titles[i] if titles is not None else f'Image {i}'
            ax.set_title('Treshold = '+ str(title))
            ax.set_axis_off()     
        fig.colorbar(im,ax=axs.ravel().tolist())
    plt.show()
    return None

def where_to_save ():                        #creates a folder in the designed folder to save the data
     parent_directory=askdirectory(title="Choose where to save the data")
     directory="Save"
     path=os.path.join(parent_directory,directory)
     os.mkdir(path)
     print("Directory created")
     return path
    
        