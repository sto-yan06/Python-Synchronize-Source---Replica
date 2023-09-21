# © Copyright 2023 by George Stoian
#All rights reserved

#This python script uses 4 arguments to Synchronize Two Folders


import os
import time
import shutil
import hashlib
import datetime
import argparse


class Pathes_as_parameters():

#With this class I made it so the path can be given by the users, and if Replica Directory and LogFile don't exist they are also automatically created

    def parse_args(self):
        parser = argparse.ArgumentParser(description="Folder Synchronization Tool")
        parser.add_argument("--src", required=True, help="Source Folder path")
        parser.add_argument("--dst",  required=True, help="Replica Folder path")
        parser.add_argument("--log", required=True, help="Log File Path")
        parser.add_argument('--interval', type=int, default=0, help="Set the time interval for the code so it can run again (time in minutes please), 0 = One-Time Run")
        return parser.parse_args()

    @staticmethod
    def Source_given(args):
        source_directory_path = args.src
        dir = os.path.join(source_directory_path)
        return source_directory_path


    @staticmethod
    def Replica_path(args): 
        replica_directory_path = args.dst
        dir = os.path.join(replica_directory_path, 'Replica')
        
        if not os.path.exists(dir):
            os.mkdir(dir)
            print(f'No directory found. Created a Replica Directory in {dir}')
        
        return dir

    
    @staticmethod
    def Log_file_path(args):
        
        log_file_path = args.log
        log_file_location = os.path.join(log_file_path, 'LogFile.txt')

        if not os.path.exists(log_file_location):
            with open(log_file_location, 'w') as LogFile:
                LogFile.write('Log File Created\n')

        return log_file_location

class ifModified():

#In this class there is the static method to calculate the checksum size with MD5 Algorithm so it can be used in Folder Synchronization to see if there are any file changes
    
    @staticmethod
    def calculate_checksum(file_path):
        md5_hash = hashlib.md5()
        with open(file_path, 'rb') as file:
            while chunk :=file.read(4096):
                md5_hash.update(chunk)
        return md5_hash.hexdigest()
    
    @staticmethod
    def checktimestamp(file_path):
        try:
            timestamp = os.path.getmtime(file_path)
            timestamp_date_time = datetime.datetime.fromtimestamp(timestamp)
            return timestamp_date_time
        except OSError:
            print(f'Error: Could not get the time stamp for {file_path}')

    
class LoggingOperation():

#In this class it's placed the logging operation method so in any cases it can be modified (it's Date Format, Lenght etc)

    def __init__(self, log_file_path):
        self.log_file_path = log_file_path

    def log_operation(self, message):

        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"[{timestamp}, {message}]"
        with open(self.log_file_path, 'a') as LogFile:
            LogFile.write(log_message + "\n")
        print(log_message)
    
class handleAllCases():

# This should be the main class where the comparison is happening, here are the 4 cases
# Case 1: Create new files in the replica folder if there is any missing file from source
# Case 2: Calculate checksum and get timestamp of each file in Source Folder and if there are no modifications nothing happens
# Case 3: Calculate checksum and get timestamp of each file in Source folder and if there are any changes it updates the Replica Folder
# Case 4: Checks to see if any file from Replica Folder is missing from Source, if it's missing then asks the user to delete it from Replica Folder as well or not

    def __init__(self, args):
        self.log_operation_instance = LoggingOperation(Pathes_as_parameters.Log_file_path(args))
        self.log_operation = self.log_operation_instance.log_operation

    def synchronize_folders(self, args):

        self.log_operation_instance = LoggingOperation(Pathes_as_parameters.Log_file_path(args))
        self.log_operation = self.log_operation_instance.log_operation

        self.source_directory = Pathes_as_parameters.Source_given(args)
        self.replica_directory = Pathes_as_parameters.Replica_path(args)
        self.log_file_path = Pathes_as_parameters.Log_file_path(args)

        for root, _, files in os.walk(self.source_directory):
            for file_name in files:
                source_file_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(source_file_path, self.source_directory)
                replica_file_path = os.path.join(self.replica_directory, relative_path)

                if not os.path.exists(replica_file_path):
                    os.makedirs(os.path.dirname(replica_file_path), exist_ok=True)
                    shutil.copy2(source_file_path, replica_file_path)
                    self.log_operation(f"Created files into Replica Folder: {replica_file_path}")
                else:
                    source_checksum = ifModified.calculate_checksum(source_file_path)
                    replica_checksum = ifModified.calculate_checksum(replica_file_path)
                    source_timestamp = ifModified.checktimestamp(source_file_path)
                    replica_timestamp = ifModified.checktimestamp(replica_file_path)

                    if source_checksum != replica_checksum or source_timestamp != replica_timestamp:
                        shutil.copy2(source_file_path, replica_file_path)
                        self.log_operation(f"Updated {relative_path}")

        for root, dirs, _ in os.walk(self.source_directory):
            for dir_name in dirs:
                source_dir_path = os.path.join(root, dir_name)
                relative_path = os.path.relpath(source_dir_path, self.source_directory)
                replica_dir_path = os.path.join(self.replica_directory, relative_path)

                if not os.path.exists(replica_dir_path):
                    os.makedirs(replica_dir_path)  # Create empty directories
                    self.log_operation(f"Created empty directory in Replica Folder: {replica_dir_path}")
        
        for root, dirs, files in os.walk(self.replica_directory):
            for file_name in files:
                replica_file_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(replica_file_path, self.replica_directory)
                source_file_path = os.path.join(self.source_directory, relative_path)

                if not os.path.exists(source_file_path):
                    user_input = input(f"Do you want to delete {relative_path} ? (y/n) ")
                    if user_input == 'y':
                        os.remove(replica_file_path)
                        self.log_operation(f"Deleted {relative_path} from Replica Folder")

            for dir_name in dirs:
                replica_dir_path = os.path.join(root, dir_name)
                relative_path = os.path.relpath(replica_dir_path, self.replica_directory)
                source_dir_path = os.path.join(self.source_directory, relative_path)

                if not os.path.exists(source_dir_path):
                    user_input = input(f"Do you want to remove the directory {relative_path} ? (y/n)")
                    if user_input == 'y':
                        shutil.rmtree(replica_dir_path)
                        self.log_operation(f"Delete directory {relative_path} from Replica Folder")

        self.log_operation("Synchronization Complete")


#main running method

def main():
    args = Pathes_as_parameters().parse_args()

    if args.interval > 0:
        try:
            while True:
                handler = handleAllCases(args)
                handler.synchronize_folders(args)
                time.sleep(args.interval * 60)
        except KeyboardInterrupt:
            print("Folder Synchronization Stopped")
    else:
        handler = handleAllCases(args)
        handler.synchronize_folders(args)

if __name__ == "__main__":
    main()