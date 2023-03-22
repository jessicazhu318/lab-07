# EE 250: Lab 7

import RPi.GPIO as GPIO
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

if __name__ == '__main__':
   while True:
      # Set GPIO to use BCM numbers
      GPIO.setmode(GPIO.BCM)
   
      # 1. Blink LED 5x w/ on/off intervals of 500ms
   
      LED_pin = 17
   
      # Set LED pin as output
      GPIO.setup(LED_pin, GPIO.OUT)
   
      for i in range(5):
         GPIO.output(LED_pin, GPIO.HIGH)	# Turn LED on
         time.sleep(0.5)			# LED stays on for 500 ms
         GPIO.output(LED_pin, GPIO.LOW)		# Turn LED off
         time.sleep(0.5)			# LED stays off for 500 ms
   
   
      # 2. For ~5sec, read output of Grove light sensor w/ intervals of 100ms
      #and print raw value along w/ text "bright" or "dark" (determine 
      #threshold through experimentation)
   
      light_sensor_channel = 0	   # MCP3008 channel wired to light sensor
      light_threshold = 150	   # Differentiate between bright and dark
   
      # Software SPI configuration
      CLK  = 11
      MISO = 9 
      MOSI = 10
      CS   = 8
      mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
   
      for i in range(50):	   # Time interval: 50 * 0.1 = 5 sec
         # Read light sensor
         light_raw_value = mcp.read_adc(light_sensor_channel)	
         # Determine bright or dark and print raw ADC light channel value
         if light_raw_value > light_threshold:
            print("Raw value of light sensor: ", light_raw_value, " - bright")
         else:
            print("Raw value of light sensor: ", light_raw_value, " - dark")
         time.sleep(0.1)	   # Wait 100 ms
   
   
      # 3. Blink LED 4x w/ on/off intervals of 200ms
   
      for i in range(4):
         GPIO.output(LED_pin, GPIO.HIGH)	# Turn LED on
         time.sleep(0.2)			# LED stays on for 200 ms
         GPIO.output(LED_pin, GPIO.LOW)		# Turn LED off
         time.sleep(0.2)			# LED stays off for 200 ms

   
      # 4. For ~5sec, read output of Grove sound sensor w/ intervals of 100ms
      #and print raw value, if sensor is tapped (ie. sound magnitude exceeds
      #threshold decided from experiment), LED should turn on for 100ms

      sound_sensor_channel = 1	   # MCP3008 channel wired to sound sensor
      sound_threshold = 450	   # Threshold to turn on LED
   
      for i in range(50):	   # Time interval: 50 * 0.1 = 5 sec
         # Read sound sensor
         sound_raw_value = mcp.read_adc(sound_sensor_channel)
         # Print raw ADC sound channel value
         print("Raw value of sound sensor: ", sound_raw_value)	
         # Determine if LED should be turned on
         if sound_raw_value > sound_threshold:
            GPIO.output(LED_pin, GPIO.HIGH)	# Turn LED on
            time.sleep(0.1)			# Wait 100 ms
            GPIO.output(LED_pin, GPIO.LOW)	# Turn LED off
         else:
            time.sleep(0.1)			# Wait 100 ms
   
      # Cleanup LED pin
      GPIO.cleanup(LED_pin)
   
