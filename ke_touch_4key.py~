#!/usr/bin/env python

import serial

class ke_touch_4key:

         ser = serial.Serial("/dev/ttyAMA0",9600)
         tx=""
         rx=""
 

         def __init__(self):

		tx = ":SETM001$$"
		ser.write(tx.encode("hex"))
		rx = ser.read(30)
		return rx.decode("hex")


	 def check_module_product_id(self):
		
		tx = ":A00514$$"
		ser.write(tx.encode("hex"))
		rx = ser.read(24)
		return rx.decode("hex")

           
         def check_module_module_id(self):

                tx = ":A003001$$"
                ser.write(tx.encode("hex"))
                rx = ser.read(24)
                return rx.decode("hex")


         def program_scene_events(self):

                tx = ": PK 002 01 A01 B10021A $$"
                ser.write(tx.encode("hex"))


         def confirm_total_events(self):

                tx = ": PK 002 01 C01$$"
                ser.write(tx.encode("hex"))


