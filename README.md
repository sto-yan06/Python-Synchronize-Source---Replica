This Python script is made by George Stoian
It is meant to be used for synchronizing two folders 

# --USAGE OF SCRIPT--

# Terminal Run:

---- Pass the arguments for the script ----

Please put each of the path for the following arguments between quotation mark

   '--src' = Source Folder; 
   '--dst' = Replica Folder; 
   '--log' = Path to create LogFile

Interval argument it can be an simple integer to represent the time interval when the code will re-run and sync again.

   '--interval 0' == It's used for one-time execution of the script

# ===EXAMPLE OF PARAMETERS USAGE===


![Terminal Examples](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/532ad77b-e2c2-4bc2-bdba-f1976506b230)


SOURCE FILE BEFORE EXECUTION:


![Source File Before Exec](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/f56484d9-05af-405f-a509-6bb24b5ffb71)


REPLICA FILE BEFORE EXECUTION:


![Replica Folder Before Exec](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/db63352d-69b8-47a2-b838-1695ef653690)


2. It Creates a Replica Folder and a Log File to specified path and if the folder it does not contain any matching data as the Source, it creates the files into Replica Folder

Console OutPut:


![Console OutPut After Exec](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/8f1c468b-035b-49cb-b0c9-e7363bf30dbd)



Replica Folder After Execution:


![replica Folder After Execution](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/0896c0dc-fd15-421e-8d1c-588026e28562)


Log File After Execution:


![LogFile After Exec](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/4bcfd45a-52a1-43ea-b2c5-1bdf3e611859)



3. It updates the change of any file giving the path for it:

Source File Update:


![Source File Written](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/6f5e5f39-c7dc-46b9-a7b6-131a7c64dcc8)


LogFile Update:


![LogFIle Update](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/00c2c65e-382e-4861-8d02-9e8f61af2fda)


4. If any file / directory it's removed from Source Folder, it asks the user whether to delete it from Replica Folder as well, or not. And it logs the action in LogFile

IN THE FOLLOWING PHOTO I DELETED 'FOLDER5' and 'FILE5':


![Deleted Folder 5 and FIle 5](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/a7c97f5c-8790-4acd-8c87-1b39eb84d5d9)



Terminal OutPut


![Terminal Output](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/f9adad70-2bbe-4e75-ae2b-5679f7f21f20)


LogFile:

![LogFile Deleting](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/8a9cde5e-03f9-4770-8ed0-697e1d4aa987)







