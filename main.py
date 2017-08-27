#!/usr/bin/env python2.7  
import RPi.GPIO as GPIO
import time
import subprocess
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#boton = 23
#rojo = GPIO.output(22,GPIO.HIGH)
#amarillo = GPIO.output(27,GPIO.HIGH) 
#verde = GPIO.output(17,GPIO.HIGH)

#setup color leds
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

# GPIO 23 set up as input. It is pulled up to stop false signals  
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

#Make sure you have a button connected so that when pressed it will connect GPIO 23 to GND

#at first setup show all leds to prove the script is on
GPIO.output(17,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH) 
GPIO.output(22,GPIO.HIGH) 

# now the program will do nothing until the signal on port 23   
# starts to fall towards zero. This is why we used the pullup
# to keep the signal high and prevent a false interrupt  
while True:
    try:  
        GPIO.wait_for_edge(23, GPIO.FALLING)  
        #reset colores
        GPIO.output(17,GPIO.LOW)
        GPIO.output(27,GPIO.LOW) 
        GPIO.output(22,GPIO.LOW) 
        #en proceso, poner color amarillo
        GPIO.output(27,GPIO.HIGH) 
        ret = subprocess.call("/home/pablo.vera/Documents/tfg/deploy.sh", shell=True)
        if ret == 0:
            #todo bien, poner color verde
            GPIO.output(27,GPIO.LOW) 
            GPIO.output(17,GPIO.HIGH) 
        else:
            # ha ido mal, poner color rojo
            GPIO.output(27,GPIO.LOW) 
            GPIO.output(22,GPIO.HIGH) 
    except KeyboardInterrupt:  
        GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  
