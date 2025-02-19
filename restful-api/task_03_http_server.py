#!/usr/bin/python3
"""http server"""
import http.server
"""cr√er un serveur HTTP"""
import socketserver
"""g√rer les connexions r√seau"""
import json


class http_SubClass(http.server.BaseHTTPRequestHandler):
    """g√re les requ√tes ™®ht de type GET"""

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
            """Statut. Le serveur r√pond ok"""
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


"""D√marrage du serveur"""
PORT = 8000
"""le serveur √coute sur le port 8000"""
with socketserver.TCPServer(("", PORT), http_SubClass) as httpd:
    """D√marre un serveur TCP utilisant la classe http_SubClass pour g√rer les requ√tes"""
    print("serving at port", PORT)
    httpd.serve_forever()
    """le serveur tourne en continue pour g√rer les requ√tes"""
