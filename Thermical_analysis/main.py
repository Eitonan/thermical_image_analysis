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
import pywt
import scipy.stats
import xlwt
import xlrd
from xlutils.copy import copy



def Main (cmap = 'inferno', List_treshold = None, Save = True, Show = True, Hist = False):   
    directory=askdirectory()
    
    if Save == True:
        path2save=where_to_save()
    else:
        path2save = None  
    for name_file in tqdm(os.listdir(directory),"Progress "):  
         if (name_file.endswith(".xlsx") and not name_file.startswith("~$")):           
             new_directory=(directory + "/" +str(name_file))
             assert os.path.isfile(new_directory)
             with open(new_directory,"r") as f :
                 pass
             
             df_tableau=pd.read_excel( io= new_directory, header=5, index_col="Unnamed: 6", 
                                      usecols=lambda x: x not in ['Unnamed: 0','Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5'], 
                                      converters={'convert_float':False})
             df_Infos=pd.read_excel( io= new_directory, header=3, converters={'convert_float':False}, usecols=lambda x: 'Unnamed' not in x,
                                    nrows=1)
             List_image=tratamiento(df_tableau,df_Infos,List_treshold,path2save,name_file,cmap, Save, Hist)

             if Show == True :
                Image_show(List_image,List_treshold,cmap) 
             time.sleep(0.0001)
    print("End with sucess")
    return None


def tratamiento (df,df_Infos,List_treshold,path2save,name_file,cmap, Save, Hist):    #Do the traitment, step by step, of the directory
    List_image=[]
    List_analysis=[]
    temp_max=(df_Infos.iloc[0,5]-32)*(5/9)
    temp_min_glob=(df_Infos.iloc[0,4]-32)*(5/9)

    for i in range (0,len(List_treshold)):
        df2use=df.copy()                                                         #create a copy of the dataframe to not change the values of the original one
        df_Celsius=Put2Celsius(df2use)                                           #Convert all °F to °C and return a dataframe in °C
        array=df2array(df_Celsius)                                               #Convert the dataframe to an array

        image,array_analyse,a,b=array2image(array,temp_max,List_treshold[i],cmap,temp_min_glob)#Convert the array to an image : normalize each pixel and do the gradient of temperature
        List_image.append(image)

        List_analysis = Analyse(array_analyse,a,b,Hist)

        if Save == True:
            name_image=str(name_file[:-5] )+ "_treshold_" +str(List_treshold[i])    #Create file name to save
            image.save(path2save +"/" + name_image + ".png", format="png")          #Save the picture in png
            Workbook_management(List_analysis,name_image,path2save)
                
    return List_image

def Workbook_management(List_analysis,Name_image,path2save):         #Creates and write the analyse inside an .xls doc
    WORKBOOK_PATH = path2save + r"\Workbook.xls"                     #Workbook path
    List_analysis.insert(0,Name_image)
    Title = ['Image','Mean','Standart Deviation','Variance',         #Creates labels for the columns
             'Entropy','Energy','Kurtosis','Skewness','Name Law','Param Law','Sse']
    
    if not os.path.exists(WORKBOOK_PATH):                           #If the worbook doesn't exist, creates it
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet(sheetname="Analysis_" + Name_image)
        for i in range(len(List_analysis)):                         #To write the name of each column                  
            sheet.write(0,i,Title[i])
    else :
        workbook = xlrd.open_workbook(WORKBOOK_PATH)                #If the workbook already exists, opens it and copy it (to not modify the initial data)
        workbook = copy(workbook)
        sheet = workbook.add_sheet(sheetname="Analysis_" + Name_image)
        for i in range(len(Title)):                     
            sheet.write(0,i,Title[i])

    for i in range(len(List_analysis)):                             #to write the data 
        sheet.write(1,i,str(List_analysis[i]))  
    workbook.save(WORKBOOK_PATH)
    return None

def Put2Celsius (df): #Convert °F to °C
    row,col=df.shape
    for i in range (row):
        for j in range(col):
            df.iloc[i,j]=(df.iloc[i,j]-32)*(5/9)
    return df


def df2array (df):      #tranform the dataframe into an numpy array
  return df.to_numpy()

def array2image(array,temp_max,treshold,cmap,temp_min_glob):     #normalise the value of each pixel then tranform the array to an PIL Image
    row,col=np.shape(array)
    if treshold == 'None':                                       #If there is no threshold, return the original picture                                              
        for i in range(row):                                     #with the given colormap
            for j in range(col):
                array[i][j],a,b=linear(array[i][j],max=temp_max,min=temp_min_glob)
    else:
        temp_min=temp_max-treshold
        for i in range(row):
            for j in range(col):
                array[i][j],a,b=linear(array[i][j],max=temp_max,min=temp_min)
    cm = plt.get_cmap(cmap)  
    colored_image = cm(array)      
    im=Image.fromarray((colored_image[:, :, :3] * 255).astype(np.uint8))
    return im,array,a,b

def linear (x,min,max):     #Create a temperature gradient with a linear function :
    a=1/(max-min)           #If the temperature is less than min (temp_min=temp_max-treshold) set the value to 0
    b=1-a*max               #Else, return a value between 0 and 1
    if x<min:
        return 0,a,b
    else:
        return a*x+b,a,b


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
     directory="Save test"
     path=os.path.join(parent_directory,directory)
     os.mkdir(path)
     print("Directory created")
     return path
    

def Analyse (array_after_treshold,a,b,Hist):                         #array_after_treshold : array of the final picture
    array_temp=arraylin2arraytemp(array_after_treshold,a,b)          #array of temperature
    non0array = Non0array(array_temp)
    List_analysis=[]
    mean = Mean(non0array)
    std = Standart_deviation(non0array)
    variance = Variance(non0array)
    entropy = Entropy(non0array)
    energy = Energy(non0array)
    kurtosis = Kurtosis(non0array)
    skewness = Skewness(non0array)
    name_ley,param_ley,sse = Histogramme(non0array,Show_hist = Hist)
    List_analysis.append(mean)
    List_analysis.append(std)
    List_analysis.append(variance)
    List_analysis.append(entropy)
    List_analysis.append(energy)
    List_analysis.append(kurtosis)
    List_analysis.append(skewness)
    List_analysis.append(name_ley)
    List_analysis.append(param_ley)
    List_analysis.append(sse)
    #print(f"Mean :{mean}    | Std :{std}    |Variance:{variance}    | Entropy :{entropy}    |Energy:{energy}    |Kurtosis:{kurtosis}    |Skewness:{skewness}")
    return List_analysis

def Non0array(array):                                       #Creates a 1xlen(array) array with onlt non-zeros values
    row,col=array.shape
    L=[]
    for i in range(row):
        for j in range(col):
            if array[i][j]!=0:
                L.append(array[i][j])
    non0array=np.array(L)
    return non0array

def arraylin2arraytemp (array,a,b):                         #Convert the array of linear value (after treshold) to the array temperature
    row,col=array.shape
    array_temp=array.copy()
    for i in range(row):
        for j in range(col):
            if array_temp[i][j]!=0:
                array_temp[i][j]=(array[i][j]-b)/a
    return array_temp

def Mean (array):                                           #Calculate the mean of the temperature
    mean = array.mean()
    return   mean 

def Standart_deviation (array):                             #Calculate the standart deviation of the temperature
    std=array.std()
    return std

def Variance (array):                                       #Calculate the variance of the temperature
    return array.std()**2

def Entropy (array):                                        #Compute the entropy of the array
    entropy=scipy.stats.entropy(array).mean()               #Raise an error if a row or a col is empty (only 0). Return NaN
    return entropy

def Energy (array):                                         #Compute the energy of the picture. A high energy means a high 
    array=np.transpose(array)                               #contrast betwenn pixels
    im=Image.fromarray((array * 255).astype(np.uint8))
    _, (cH, cV, cD) = pywt.dwt2(im, 'db1')
    energy = (cH**2 + cV**2 + cD**2).sum()/(im.size[0]*im.size[1])
    return energy

def Kurtosis (array):                                       #Calculate the kurtosis of the array
    kurtosis=scipy.stats.kurtosis(array)
    return kurtosis 

def Skewness (array):                                       #Calculate the skewness of the array
    skewness = scipy.stats.skew(array)
    return skewness

def Histogramme (array,Show_hist):                          #Calculate the optimal law for the data and display (or not) the histogramme
    y, x = np.histogram(array, bins=15, density=True)
    x = (x + np.roll(x, -1))[:-1] / 2.0
    dist_names = ['norm', 'beta','gamma', 'pareto', 't', 'lognorm', 'invgamma', 'invgauss',  'loggamma', 'alpha', 'chi', 'chi2']
    sse = np.inf
    # For each law name in dist_names
    for name in dist_names:
                dist=getattr(scipy.stats, name)
                param=dist.fit(array)
                loc = param[-2]
                scale = param[-1]
                arg = param[:-2]
                pdf = dist.pdf(x, *arg, loc=loc, scale=scale)
                model_sse = np.sum((y - pdf)**2)
                #print(f"Model : {name}\tSse : {model_sse}")
                if model_sse < sse :
                     sse = model_sse
                     best_pdf = pdf
                     best_param=param
                     best_name = name
                     
    if Show_hist == True: 
        plt.figure(figsize=(12,8))
        plt.plot(x, y, label="Données")
        plt.plot(x, best_pdf, label=best_name, linewidth=3)
        plt.legend(loc='upper right')
        plt.show()

    return best_name,best_param,sse
