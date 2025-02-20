#!/usr/bin/python3
"""http server"""
import http.server
import socketserver
import json


class http_SubClass(http.server.BaseHTTPRequestHandler):
    """ge√re les reqe√tes tp de type GET"""

    def do_GET(self):
        """http server"""
        if self.path == "/":
            """Accueil"""
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            """Donn√es JSON. Renvoie un objet json"""
            dataset = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(dataset).encode("utf-8"))

        elif self.path == "/info":
            """Informations sur l'API. Renvoie une description json"""
            dataset = {"version": "1.0", "description":
                       "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(dataset).encode("utf-8"))

        elif self.path == "/status":
            """Statut. Le serveur re√pond ok"""
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            """Gestion des erreurs"""
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


"""De√marrage du serveur"""
PORT = 8000
with socketserver.TCPServer(("", PORT), http_SubClass) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
