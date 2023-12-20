from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

leitor = SimpleMFRC522()

GPIO.setup(18, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

acesso = False

print("Aproxime a tag")

while True:
    id,texto = leitor.read()
    if id == 771459753502:
        print("Acesso liberado")
        acesso = True
        GPIO.output(15, True)
        sleep(3)
        GPIO.output(15, False)
    else:
        print("Acesso negado")
        acesso = False
        GPIO.output(18, True)
        sleep(3)
        GPIO.output(18, False)
