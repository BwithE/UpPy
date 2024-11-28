import http.server
import socketserver
import os
from cgi import FieldStorage

class UploadHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_type = self.headers.get('Content-Type')

        if 'multipart/form-data' in content_type:
            # Parse the multipart form data
            form = FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'}
            )
            if 'file' in form:
                # Save the uploaded file
                file_item = form['file']
                filename = file_item.filename
                file_content = file_item.file.read()
                
                with open(os.path.join(os.getcwd(), filename), 'wb') as f:
                    f.write(file_content)
                
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'File uploaded successfully!')
            else:
                self.send_error(400, b"No file field in the form")
        else:
            self.send_error(400, b"Unsupported Content-Type")

    def do_GET(self):
        # Host an upload form for testing in the browser
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