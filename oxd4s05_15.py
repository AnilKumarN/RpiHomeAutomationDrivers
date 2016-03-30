#!/usr/bin/env python

import serial

class oxd4s05_15:

         ser = serial.Serial("/dev/ttyAMA0",9600)
         tx=""
         rx=""
 

         def __init__():

		tx = ":SETM001$$"
		ser.write(tx)
		rx = ser.read(30)
		return rx


	 def check_module_product_id():
		
		tx = ":A00502$$"
		ser.write(tx)
		rx = ser.read(24)
		return rx

           
         def check_module_module_id():

                tx = ":A003001$$"
                ser.write(tx)
                rx = ser.read(24)
                return rx


         def operate_single_load():

                tx = ":A10600201099$$"
                ser.write(tx)


         def operate_single_load_newversion():

                tx = ":B10021A$$"
                ser.write(tx)


         def operate_all_loads():

                tx = ":B2002AAX00$$"
                ser.write(tx


         def load_status():

                tx = ":B3002$$"
                ser.write(tx)
                rx = ser.read(24)
                return rx


         def default_all_on():

                tx = ":D($$"
                ser.write(tx


         def default_all_off():

                tx = ":D)$$"
                ser.write(tx


         def set_curtain_status():

                tx = ":N1 004 1 1 012 014 $$"
                ser.write(tx


         def disable_curtain():

                tx = ":N1 004 0 0 000 000 $$"
                ser.write(tx


         def curtain_operation():

                tx = ":T 004 1 1 $$"
                ser.write(tx


         def stop_curtain():

                tx = ":T004SX$$"
                ser.write(tx





         
