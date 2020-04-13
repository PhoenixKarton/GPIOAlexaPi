import RPi.GPIO as GPIO
import fauxmo

class GpioPlugin(fauxmo.plugins.FauxmoPlugin):
 def __init__(self, pin, name, port):
  super().__init__(name=name, port=port)
  self.pin = pin
  self.state = 0
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(self.pin, GPIO.OUT)
  
 def on(self) -> bool:
  GPIO.output(self.pin, GPIO.HIGH)
  self.state = True
  return True
 
 def off(self) -> bool:
  GPIO.output(self.pin, GPIO.LOW)
  self.state = False
  return True

 def get_state(self) -> str:
  if self.state:
   return "on"
  elif not self.state:
   return "off"
  return "unknown"
