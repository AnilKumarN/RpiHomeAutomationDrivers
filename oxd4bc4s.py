#!/usr/bin/env python

import serial

class oxd4bc4s:

         ser = serial.Serial("/dev/ttyAMA0",9600)
         tx=""
         rx=""
 

         def __init__():

		tx = ":SETM001$$"
		ser.write(tx.encode("hex"))
		rx = ser.read(30)
		return rx.decode("hex")


	 def check_module_product_id():
		
		tx = ":A00503$$"
		ser.write(tx.encode("hex"))
		rx = ser.read(24)
		return rx.decode("hex")

           
         def check_module_module_id():

                tx = ":A003001$$"
                ser.write(tx.encode("hex"))
                rx = ser.read(24)
                return rx.decode("hex")


         def operate_single_load_100():

                tx = ":A10600201099$$"
                ser.write(tx.encode("hex"))


         def operate_single_load_10():

                tx = ":B10021A$$"
                ser.write(tx.encode("hex"))


         def operate_all_loads():

                tx = ":B2002AAX0$$"
                ser.write(tx.encode("hex")


         def load_status():

                tx = ":B3002$$"
                ser.write(tx.encode("hex"))
                rx = ser.read(24)
                return rx.decode("hex")


         def default_all_on():

                tx = ":D($$"
                ser.write(tx.encode("hex")


         def default_all_off():

                tx = ":D)$$"
                ser.write(tx.encode("hex")


         def default_all_stepup():

                tx = ":DH$$"
                ser.write(tx.encode("hex")


         def default_all_stepdown():

                tx = ":DJ$$"
                ser.write(tx.encode("hex")







