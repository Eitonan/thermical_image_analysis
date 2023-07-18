# Thermical image analysis
Allows you to make a temperature gradient of a portion of a thermical image using Smartview
Hello, welcome to the "How to use" guide !

    I) Installation

    Please be sure to have installed all the following librairies :
                                                          				  -tkinter
                                                         				   -os
                                                         				   -pillow
                                                       					     -pandas
                                                        					    -tqdm
                                                       					     -time
                                                        					    -numpy
                                                         				   -mathplotlib
    Most of them are already installed, but if you doubt, you can try using the command pip -install "name_librairy" in the terminal.
The program runs using the version 3.9.7 of python.

    II) Utilisation

    Once all the librairies are downloaded, you can try to run the code. 
    It allows, for now, only excel (.xslx) files. Please, follow the following steps :

        1) Open Smartview. I use the free version of it. I never tried with Smartview R&D but it should work.
        2) Open a picture

        





3) Open the picture editor (either by double-clicking on it or this icon)  

4) It opens this :
 

5) Select the back temperature and emisivity depending on your case
 

6) Select the type of marker you wish to use (can be any shape) and select the region you wish perform the analysis onto. Don’t use more  than one marker ! It will create an error otherwise. 
 









7) Click the « Accept » then right click on the picture and select « Exportar ». This window will open.
 

8) Select « Markers only » and export in a txt file. It should looks like this :
 



9) Open Excel and open the txt file created.
 
 








10) You should have this :
 
Make sure to have the « Etiqueta » in line 5 and « A0 » in line 6. Then save the file in .xlsx extension.
11) Open the program and run the file named « tkinter_interface ». This window should open : 
 




You can choose the values of the treshold here :
 
The colormap here : 
 
You can choose to save and/or show the picture by clicking here :
 
Then, run and enjoy.


























