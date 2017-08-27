#!/usr/bin/env python2.7  
import RPi.GPIO as GPIO
import time
import subprocess
GPIO.setmode(GPIO.BCM)

#boton = 23
#rojo = GPIO.output(18,GPIO.HIGH)
#amarillo = 
#verde = 

# GPIO 23 set up as input. It is pulled up to stop false signals  
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

print "Make sure you have a button connected so that when pressed"  
print "it will connect GPIO port 23 (pin 16) to GND (pin 6)\n"  
#raw_input("Press Enter when ready\n>")  

print "Waiting for falling edge on port 23"  
# now the program will do nothing until the signal on port 23   
# starts to fall towards zero. This is why we used the pullup
# to keep the signal high and prevent a false interrupt  
while True:
    try:  
        print "\n mantener el color previo"
        GPIO.wait_for_edge(23, GPIO.FALLING)  
        print "\nreset colores"
        print "\nponer color amarillo" 
        ret = subprocess.call("/home/pablo.vera/Documents/tfg/deploy.sh", shell=True)
        if ret == 0:
            print "\nponer color verde"
        else:
            print "\nponer color rojo"
    except KeyboardInterrupt:  
        GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  
