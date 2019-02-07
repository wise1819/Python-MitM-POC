# -*- coding: utf-8 -*-
"""
Ein Skript das ein "proof of concept" sein sollte. Es läuft als lokaler Service 
um Daten über Rest in das Jaspersoft Studio zu bekommen.
Eine direkte Anbindung ist leider aufgrund des Authentifizierungssystems nicht
möglich.
Den String [input] bitte mit gültigen Einträgen ersetzen.
Beispielanfrage in Jaspersoft Studio = http://127.0.0.1:5000/timerecording/bookings?syncStateTimestamp=0&minDate=2012-10-29
"""
import requests
import json
#Flask muss installiert werden.
from flask import Flask
from flask_restful import Api, Resource,request

class Data(Resource):
    def get(self, query):
        #erneutes bauen der Anfrage
        parameters = request.args
        #erster Parameter muss durch ein Fragezeichen getrennt sein weitere Parameter durch ein "&"
        firstIteration = True
        divider = "?"
        #erneutes anhängen des "Paths".
        newURL = url+"/"+query
        #Die foreach Schleife hängt die Parameter erneut an die URL.
        for arg in parameters:
            if (arg is not None):
                if(not firstIteration):
                    divider="&"
                firstIteration = False
                newURL += divider +str(arg)+"="+str(parameters.get(arg)) 
        
        #Printausgabe dient als Kontrolle. Die Anfrage sollte Äquivalent zu 
        #einer möglichen Anfrage, zu dem BCS-Server, sein.
        print(newURL)
        result = requests.get(newURL,cookies=login.cookies,headers=thisHeaders)
        txt = result.content
        j = json.loads(txt)
        print(j)
        return j
    
app = Flask(__name__)
api = Api(app)

#Path wird an die Klasse übergeben
api.add_resource(Data, "/<path:query>")

#[input] = die Adresse ohne weitere Path Komponenten
url = "[input]/app/rest"
thisBody = {
	"userLogin":"[input]",
	"userPwd":"[input]"
}
thisHeaders = {"content-type": "application/json"}
#Holt sich den Authentifizierungstoken 
login = requests.post(url+"/auth/login",json=thisBody,headers=thisHeaders)
print(login.cookies)


app.run(debug=False)