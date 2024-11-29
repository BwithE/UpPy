import socket
import http.server
import socketserver
import os

class UploadHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # handles file upload
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # assumes the form field is 'file'
        boundary = self.headers['Content-Type'].split('=')[1].encode()
        parts = post_data.split(boundary)

        for part in parts:
            if b'filename=' in part:
                # extract the filename
                filename = part.split(b'filename=')[1].split(b'\r\n')[0].strip(b'"').decode('utf-8')
                
                # file content starts after the first \r\n\r\n sequence
                # everything after the first \r\n\r\n and before the next \r\n boundary is the file content
                try:
                    file_content = part.split(b'\r\n\r\n')[1]  # This skips the headers part
                except IndexError:
                    continue  # Skip empty parts or malformed data
                
                # Remove any trailing boundary markers
                if file_content.endswith(b'--'):
                    file_content = file_content[:-2]

                # save the file to the current directory
                with open(os.path.join(os.getcwd(), filename), 'wb') as f:
                    f.write(file_content)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'File uploaded successfully!')

    def do_GET(self):
        # host the upload form with a darker theme and purple button
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'''
            <html>
            <title>UpPy</title>
                <head>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            height: 100vh;
                            margin: 0;
                            background-color: #2c2f38;  /* Dark background */
                            color: #e0e0e0;  /* Light text color */
                        }
                        .container {
                            padding: 30px;
                            border-radius: 8px;
                            background-color: #3a3f47;  /* Darker background for the box */
                            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
                            text-align: center;
                            width: 100%;
                            max-width: 400px;
                        }
                        h1 {
                            color: #f1f1f1;  /* Light text color for the heading */
                            margin-bottom: 20px;
                        }
                        input[type="file"] {
                            margin-bottom: 20px;
                            padding: 10px;
                            border-radius: 5px;
                            border: 1px solid #555;
                            background-color: #555;
                            color: #fff;
                        }
                        input[type="submit"] {
                            padding: 10px 20px;
                            border: none;
                            background-color: #8e44ad;  /* Purple button */
                            color: white;
                            font-size: 16px;
                            cursor: pointer;
                            border-radius: 5px;
                        }
                        input[type="submit"]:hover {
                            background-color: #9b59b6;  /* Lighter purple on hover */
                        }
                    </style>
                </head>
                <body>
                    <div class="container">
                        <h1>Upload Your File</h1>
                        <form action="" method="post" enctype="multipart/form-data">
                            <input type="file" name="file" />
                            <br>
                            <input type="submit" value="Upload" />
                        </form>
                    </div>
                </body>
            </html>
        ''')

class ThreadingHTTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def create_server():
    handler = UploadHandler
    server = ThreadingHTTPServer(("", 80), handler)

    # Allow the socket to reuse the address and port immediately
    server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)  # Optional (for high-performance systems)
    
    return server

server = create_server()
print(f"Serving on port 80")
server.serve_forever()
