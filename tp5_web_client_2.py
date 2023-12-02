import http.client

host = "127.0.0.1"
port = 8080

# Créez une connexion au serveur
conn = http.client.HTTPConnection(host, port)

# Envoyez une requête GET à "/"
conn.request("GET", "/htdocs/toto.html")

# Obtenez la réponse du serveur
response = conn.getresponse()

# Affichez le statut de la réponse
print("Status:", response.status)

# Affichez le contenu de la réponse
print("Response:")
print(response.read().decode("utf-8"))

# Fermez la connexion
conn.close()
