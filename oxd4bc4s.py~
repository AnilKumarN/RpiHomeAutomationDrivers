#!/usr/bin/env python

import serial

class oxd4bc4s:

         ser = serial.Serial("/dev/ttyAMA0",9600)
         tx=""
         rx=""
 

         def __init__():

		tx = ":SETM001$$"
		ser.write(tx)
		rx = ser.read(15)
		return rx


	 def check_module_product_id():
		
		tx = ":A00503$$"
		ser.write(tx)
		rx = ser.read(12)
		return rx

           
         def check_module_module_id():

                tx = ":A003001$$"
                ser.write(tx)
                rx = ser.read(12)
                return rx


         def operate_single_load_100():

                tx = ":A10600201099$$"
                ser.write(tx)


         def operate_single_load_10():

                tx = ":B10021A$$"
                ser.write(tx)


         def operate_all_loads():

                tx = ":B2002AAX0$$"
                ser.write(tx)


         def load_status():

                tx = ":B3002$$"
                ser.write(tx)
                rx = ser.read(12)
                return rx


         def default_all_on():

                tx = ":D($$"
                ser.write(tx)


         def default_all_off():

                tx = ":D)$$"
                ser.write(tx)


         def default_all_stepup():

                tx = ":DH$$"
                ser.write(tx)


         def default_all_stepdown():

                tx = ":DJ$$"
                ser.write(tx)







