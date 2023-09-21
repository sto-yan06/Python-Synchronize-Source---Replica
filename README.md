The script uses two libraries 'os' and 'shutil' to manage windows directories, files and their paths.
It has a 'sync_interval' constant so it can re-run after that time.
it also creates three elements in case that they not exist: Source Directory, Replica Directory and LogFile.txt
For 'folder trees' it uses the 'shutil' library so it can override the whole subdirectories in order to fully synchronize.
