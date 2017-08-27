#!/usr/bin/env python2.7  
import RPi.GPIO as GPIO
import time
import subprocess
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW) 
GPIO.output(22,GPIO.LOW)
