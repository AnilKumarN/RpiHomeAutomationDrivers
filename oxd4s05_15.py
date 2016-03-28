#!/usr/bin/env python

import serial

class oxd4s05_15:

         ser = serial.Serial("/dev/ttyAMA0",9600)
         tx=""
         rx=""
 

         def __init__(self):

		tx = ":SETM001$$"
		ser.write(tx.encode("hex"))
		rx = ser.read()
		return rx.decode("hex")


	 def check_module_product_id(self):
		
		tx = ":A00502$$"
		ser.write(tx.encode("hex"))
		rx = ser.read()
		return rx.decode("hex")

           
         def check_module_module_id(self):

                tx = ":A003001$$"
                ser.write(tx.encode("hex"))
                rx = ser.read()
                return rx.decode("hex")


         def operate_single_load(self):

                tx = ":A10600201099$$"
                ser.write(tx.encode("hex"))


         def operate_single_load_newversion(self):

                tx = ":B10021A$$"
                ser.write(tx.encode("hex"))


         def operate_all_loads(self):

                tx = ":B2002AAX00$$"
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


         def set_curtain_status(self):

                tx = ":N1 004 1 1 012 014 $$"
                ser.write(tx.encode("hex")


         def disable_curtain(self):

                tx = ":N1 004 0 0 000 000 $$"
                ser.write(tx.encode("hex")


         def curtain_operation(self):

                tx = ":T 004 1 1 $$"
                ser.write(tx.encode("hex")


         def stop_curtain(self):

                tx = ":T004SX$$"
                ser.write(tx.encode("hex")





         
