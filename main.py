import os
import time
import shutil


directory = os.getcwd()
source = 'source'
replica = 'replica'
sync_interval = 3600

class ReplicaSourceLog():

# In this class, I made a static method to check the existance of each directory and file

    @staticmethod
    def checkifexistSource():
        if os.path.exists('source'):
            print('Existing Directory...')
        else:
            os.makedirs('source')
            print('Created New Source Directory')
    
    @staticmethod
    def checkifexistReplica():
        if os.path.exists('replica'):
            print('Existing Directory...')
        else:
            os.makedirs('replica')
            print('Created New Replica Directory')
    
    @staticmethod
    def checkifexistsLOGFILE():
        logfile_path = os.path.join(directory, 'LogFile.txt')

        if os.path.exists(logfile_path):
            print('Existing Log File')
        else:
            with open(logfile_path, 'w') as LogFile:
                print('Created a Log File')

class FolderSynchronizationOperations():

    #In this class i made some methods for every synchronization step that I tought it would be necessary

    def __init__(self):
        self.source_path = os.path.join(directory, source)
        self.replica_path = os.path.join(directory, replica)
        self.log_path = os.path.join(directory, 'LogFile.txt')
            
    def log_operation(self, message):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"[{timestamp}, {message}]"
        with open(self.log_path, 'a') as log_file:
            log_file.write(log_message + "\n")
        print(log_message)

# Here in the copy_item method it is used os and shutil libraries so using 'os' I could get the path for each file and directory and using 'shutil' I could manage the whole root directory
# And made it also to log when a directory is overridden, just copied, or a file is copied
# I also added an exception so I could identify the error easier  

    def copy_item(self, source_item, replica_item):
        try:
            if os.path.isdir(source_item):
                if os.path.exists(replica_item):
                    self.log_operation(f"Overriding Directory: {os.path.relpath(replica_item, self.replica_path)}")
                    shutil.rmtree(replica_item)
                shutil.copytree(source_item, replica_item)
                self.log_operation(f"Directory Copied: {os.path.relpath(replica_item, self.replica_path)}")
            else:
                shutil.copy2(source_item, replica_item)
                self.log_operation(f"File Copied: {os.path.relpath(replica_item, self.replica_path)}")
        except Exception as e:
            self.log_operation(f"Error copying {os.path.relpath(source_item, self.source_path)}: {str(e)}")

# folder_sync method uses the previous methods to check if there are existing directories and logfiles so the process could be done
# after  checking it logs that a synchronization is happening and proceed to use the copy_item method for directories and files

    def folder_sync(self):
        
        replica_log = ReplicaSourceLog()
        replica_log.checkifexistReplica()
        replica_log.checkifexistSource()
        replica_log.checkifexistSource()

        self.log_operation("Synchronizing Folders...")

        for root, dirs, files in os.walk(self.source_path):
            for directory in dirs:
                source_dir = os.path.join(root, directory)
                replica_dir = os.path.join(self.replica_path, os.path.relpath(source_dir, self.source_path))
                self.copy_item(source_dir, replica_dir)

            for file in files:
                source_file = os.path.join(root, file)
                replica_file = os.path.join(self.replica_path, os.path.relpath(source_file, self.source_path))
                self.copy_item(source_file, replica_file)

if __name__ == "__main__":
    while True:
        folder_items = FolderSynchronizationOperations()
        folder_items.folder_sync()
        time.sleep(sync_interval)     # It uses the input given as seconds to sleep between running the code again so it can synchronize periodically