# UpPy


![image](https://github.com/user-attachments/assets/c5386554-5fb1-4d26-89cc-b646dc03f754)


A Python HTTP server that runs on port 80 and supports POST method to receive files from remote machines.

Files will be uploaded into the current working directory that `up.py` is ran.

It's an easy way to trasfer files.

The webpage has buttons that can be used.

Below is a list of CLI commands to get the job done.

Windows clients need `curl.exe` for CLI commands which can be found at https://curl.se/windows/.

# USAGE
```
python3 up.py
```


# CLIENT USAGE
- WINDOWS UPLOAD COMMAND
```
curl -X POST -F "file=@c:\path\to\your\file.txt" http://<PYTHON_SERVER_IP>

Invoke-WebRequest -Uri "http://<PYTHON_SERVER_IP>" -Method Post -Form @{file=Get-Item "C:\path\to\your\file.txt"}
```


- LINUX & MAC UPLOAD COMMAND
```
curl -X POST -F "file=@/path/to/your/file.txt" http://<PYTHON_SERVER_IP>
```
