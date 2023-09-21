This Python script is made by George Stoian
It is meant to be used for synchronizing two folders 

--USAGE OF SCRIPT--

Terminal Run:

1. ---- Pass the arguments for the script ----

Please put each of the path for the following arguments between quotation mark

   '--src' = Source Folder; 
   '--dst' = Replica Folder; 
   '--log' = Path to create LogFile

Interval argument it can be an simple integer to represent the time interval when the code will re-run and sync again.

'--interval 0' == It's used for one-time execution of the script

===EXAMPLE OF PARAMETERS USAGE===

![Terminal Examples](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/598c1672-d353-4a85-b162-c3f49b112a71)

SOURCE FILE BEFORE EXECUTION:

![Source File Before Exec](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/9f521ddd-1a08-49bc-81f5-6b6b66b31aab)

REPLICA FILE BEFORE EXECUTION:

![Replica Folder Before Exec](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/bec8ed10-81d6-4bf9-b234-22e411062ddd)



2. It Creates a Replica Folder and a Log File to specified path and if the folder it does not contain any matching data as the Source, it creates the files into Replica Folder

Console OutPut:

![Console OutPut After Exec](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/f9af2e70-6671-45f1-b9a9-9dd2dad017f8)

Replica Folder After Execution:

![replica Folder After Execution](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/a3a5184a-cac2-46d1-8e87-5c79f61cff8d)

Log File After Execution:

![LogFile After Exec](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/c9972be6-4282-4fc9-af2c-bb80ea6dd33d)

3. It updates the change of any file giving the path for it:

Source File Update:

![Source File Written](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/d2011f8b-9702-40ce-9b29-0639a5e2bcf8)

LogFile Update:

![LogFIle Update](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/5eecb588-0d8f-4e01-874e-3f4f624980f4)

4. If any file / directory it's removed from Source Folder, it asks the user whether to delete it from Replica Folder as well, or not. And it logs the action in LogFile

IN THE FOLLOWING PHOTO I DELETED 'FOLDER5' and 'FILE5':

![Deleted Folder 5 and FIle 5](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/56023f19-0ad0-40b9-a7ec-c48d105f7bb3)

Terminal OutPut

![Terminal Output](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/d568d5d5-b697-4972-869a-c6048bca175c)

LogFile:

![LogFile Deleting](https://github.com/sto-yan06/Python-Synchronize-Source---Replica/assets/116439554/25a04d1d-2cfc-496a-869c-43ac08a886d7)









