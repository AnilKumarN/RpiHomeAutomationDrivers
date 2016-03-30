#!/usr/bin/env python

import serial

class ox_ir:

         ser = serial.Serial("/dev/ttyAMA0",9600)
         tx=""
         rx=""
 

         def __init__():

		tx = ":SETM001$$"
		ser.write(tx)
		rx = ser.read(30)
		return rx


	 def check_module_product_id():
		
		tx = ":A00505$$"
		ser.write(tx)
		rx = ser.read(24)
		return rx

           
         def check_module_module_id():

                tx = ":A003001$$"
                ser.write(tx)
                rx = ser.read(24)
                return rx


         def program_scene_events():

                tx = ": PI 002 01 A01 B10021A $$"
                ser.write(tx)


         def confirm_total_events():

                tx = ": PI 002 01 C01$$"
                ser.write(tx)

