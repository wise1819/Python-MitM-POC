# Python-MitM-POC
In diesem Repository findet sich der Proof-Of-Concept für einen Python-Server, welcher zwischen JasperSoft Studio und BCS sitzt 
und einen beständigen Zustand beinhaltet, mit dem die Authentifizierung zum BCS-Server hergestellt wird und über mehrere 
Requests von JasperSoft Sudio hinweg erhalten bleibt. Der Code ist so simpel wie möglich gehalten worden.

## Vorbereitung
Flask, flask-restful müssen zur Benutzung der Skripte installiert werden.

    pip install Flask
    
    pip install flask-restful

## Benutzung (merge.py)

1. Im Skript müssen die Adresse und die Nutzerdaten ausgetauscht werden.
2. Service starten (am besten in einer Konsole)
    1. Der Token sollte in der Konsole ausgegebn werden.
3. Im JasperSoft Studio einen neuen `JSON File`-Data-Adapter erstellen.
    1. Als `File/URL` den gewünschten path und variablen angeben. 
    Die Adresse sollte lediglich durch 127.0.0.1:5000 ersetzt werden
        dies würde für unseren Beispielreport so aussehen:
            `http://127.0.0.1:5000/timerecording/bookings?syncStateTimestamp=0&minDate=2012-10-29`.
    2. In den Optionen für den Adapter: Als `Request Type` `POST` angeben
    3.  Alternativ können die Parameter auch in den Optionen für den Adapter angegeben werden.
    
4. Wenn nun ein neuer Report erstellt wird kann der neue Adapter ausgewählt werden. 
    Ab diesem Zeitpunkt ist die Benutzung gleich zu einer lokalen JSON.
