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





   ![alt tag](https://user-images.githubusercontent.com/125255391/254378567-27fef47a-6de7-44d1-ae3a-d3bff91aeb8d.png)
        





3) Open the picture editor (either by double-clicking on it or this icon)  

      ![alt tag](https://user-images.githubusercontent.com/125255391/254378686-76425d9b-8a56-4bc6-b6e5-dfbaab5bcdb7.png)
   
4) It opens this :


   ![alt tag](https://user-images.githubusercontent.com/125255391/254378757-81a7f8a6-8ad9-4745-91e1-7d12be32d977.png)

6) Select the back temperature and emisivity depending on your case


    ![alt tag](https://user-images.githubusercontent.com/125255391/254378834-94d77632-f64c-4924-9cec-d1475412c4b5.png)

8) Select the type of marker you wish to use (can be any shape) and select the region you wish perform the analysis onto. Don’t use more  than one marker ! It will create an error otherwise. 
     ![alt tag](https://user-images.githubusercontent.com/125255391/254378909-f42aaecf-248e-4bb8-9c24-ab709553816e.png)









9) Click the « Accept » then right click on the picture and select « Exportar ». This window will open.
     ![alt tag](https://user-images.githubusercontent.com/125255391/254378987-e8665483-52e3-4592-ab54-68664e7c5ce0.png)

10) Select « Markers only » and export in a txt file. It should looks like this :
     ![alt tag](https://user-images.githubusercontent.com/125255391/254379025-33f21900-b5d9-497b-95a5-253298b20307.png)



11) Open Excel and open the txt file created.
     ![alt tag](https://user-images.githubusercontent.com/125255391/254379086-4d458e33-9c5d-4e45-b94e-da50f0f9b268.png)
     ![alt tag](https://user-images.githubusercontent.com/125255391/254379146-7bddfc60-bed8-4d8d-8e90-3a086d0e0dbe.png)
     ![alt tag](https://user-images.githubusercontent.com/125255391/254379198-e437d414-a8ae-42a9-8a96-f7c633aae214.png)






12) You should have this :
    ![alt tag](https://user-images.githubusercontent.com/125255391/254379249-e9ba2619-4556-469d-92f3-49a624d72536.png)
 
Make sure to have the « Etiqueta » in line 5 and « A0 » in line 6. Then save the file in .xlsx extension.

11) Open the program and run the file named « tkinter_interface ». This window should open : 
     ![alt tag](https://user-images.githubusercontent.com/125255391/254379327-cf465cac-816d-4b16-af60-0117c6fdd5ca.png)




You can choose the values of the treshold here :
  ![alt tag](https://user-images.githubusercontent.com/125255391/254379364-84392cbd-b274-4ce2-8cf2-254449499d6b.png)

 
The colormap here : 
    ![alt tag](https://user-images.githubusercontent.com/125255391/254379409-cf7156d0-c14a-41f1-aa68-fa9a3f0b0ac6.png)
 
You can choose to save and/or show the picture by clicking here :
     ![alt tag](https://user-images.githubusercontent.com/125255391/254379453-94afe1e1-7921-4484-a885-d023919731b6.png)
     
Then, run and enjoy.


























