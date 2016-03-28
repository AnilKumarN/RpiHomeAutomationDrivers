#!/usr/bin/env python

import serial

class oxd4bc4s:

         ser = serial.Serial("/dev/ttyAMA0",9600)
         tx=""
         rx=""
 

         def __init__(self):

		tx = ":SETM001$$"
		ser.write(tx.encode("hex"))
		rx = ser.read()
		return rx.decode("hex")


	 def check_module_product_id(self):
		
		tx = ":A00503$$"
		ser.write(tx.encode("hex"))
		rx = ser.read()
		return rx.decode("hex")

           
         def check_module_module_id(self):

                tx = ":A003001$$"
                ser.write(tx.encode("hex"))
                rx = ser.read()
                return rx.decode("hex")


         def operate_single_load_100(self):

                tx = ":A10600201099$$"
                ser.write(tx.encode("hex"))


         def operate_single_load_10(self):

                tx = ":B10021A$$"
                ser.write(tx.encode("hex"))


         def operate_all_loads(self):

                tx = ":B2002AAX0$$"
                ser.write(tx.encode("hex")


         def load_status(self):

                tx = ":B3002$$"
                ser.write(tx.encode("hex"))
                rx = ser.read()
                return rx.decode("hex")


         def default_all_on(self):

                tx = ":D($$"
                ser.write(tx.encode("hex")


         def default_all_off(self):

                tx = ":D)$$"
                ser.write(tx.encode("hex")


         def default_all_stepup(self):

                tx = ":DH$$"
                ser.write(tx.encode("hex")


         def default_all_stepdown(self):

                tx = ":DJ$$"
                ser.write(tx.encode("hex")






