# http-upload
A Python HTTP server that can receive files from remote machines.

They will be uploaded into the current working directory that it is ran.

An easy way to trasnfer files without the need of SSH and compromising usernames.


- WINDOWS POWERSHELL UPLOAD COMMAND
	- `Invoke-RestMethod -Uri <PYTHON_SERVER_IP> -Method Post -Form <PATH_TO_YOUR_FILE>`

- LINUX UPLOAD COMMAND
	- `curl -X POST -F "file=@/path/to/your/file.txt" http://localhost`
