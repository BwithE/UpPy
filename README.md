# http-upload
A Python HTTP server that runs on port 80 and receives files from remote machines.

They will be uploaded into the current working directory that it's ran.

It's an easy way to trasnfer files without the need of SSH and compromising usernames.

The webpage has buttons that can be used, however, below is a list of CLI commands to get the job done.

# USAGE
`python3 upload-server.py`


# CLIENT USAGE
- WINDOWS POWERSHELL UPLOAD COMMAND
	- `Invoke-RestMethod -Uri <PYTHON_SERVER_IP> -Method Post -Form <PATH_TO_YOUR_FILE>`

- LINUX UPLOAD COMMAND
	- `curl -X POST -F "file=@/path/to/your/file.txt" http://<PYTHON_SERVER_IP>`
