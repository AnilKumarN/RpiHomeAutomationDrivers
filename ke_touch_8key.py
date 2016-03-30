#!/usr/bin/env python

import serial

class ke_touch_8key:

         ser = serial.Serial("/dev/ttyAMA0",9600)
         tx=""
         rx=""
 

         def __init__():

		tx = ":SETM001$$"
		ser.write(tx)
		rx = ser.read(30)
		return rx


	 def check_module_product_id():
		
		tx = ":A00513$$"
		ser.write(tx)
		rx = ser.read(24)
		return rx

           
         def check_module_module_id():

                tx = ":A003001$$"
                ser.write(tx)
                rx = ser.read(24)
                return rx


         def program_scene_events():

                tx = ": PK 002 01 A01 B10021A $$"
                ser.write(tx)


         def confirm_total_events():

                tx = ": PK 002 01 C01$$"
                ser.write(tx)


