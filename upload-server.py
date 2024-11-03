import http.server
import socketserver
import os
from urllib.parse import parse_qs

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
                file_content = part.split(b'\r\n\r\n')[1].split(b'\r\n')[0]
                
                # save the file to the current directory
                with open(os.path.join(os.getcwd(), filename), 'wb') as f:
                    f.write(file_content)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'File uploaded successfully!')

    def do_GET(self):
        # host the upload form
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'''
            <html>
                <body>
                    <form action="" method="post" enctype="multipart/form-data">
                        <input type="file" name="file" />
                        <input type="submit" value="Upload" />
                    </form>
                </body>
            </html>
        ''')

PORT = 80
with socketserver.TCPServer(("", PORT), UploadHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
