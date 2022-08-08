from datetime import datetime

now = datetime.now()
now = int(now.strftime("%H"))

if (now >= 19):
    print ("Hora de ir a casa!")
else:
    falta = 19 - now
    print ("Aun te quedan", falta, "hora(s)")