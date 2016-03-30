#!/usr/bin/env python

import serial

class ox_rtc:

         ser = serial.Serial("/dev/ttyAMA0",9600)
         tx=""
         rx=""
 

         def __init__():

		tx = ":SETM001$$"
		ser.write(tx)
		rx = ser.read(30)
		return rx


	 def check_module_product_id():
		
		tx = ":A00507$$"
		ser.write(tx)
		rx = ser.read(24)
		return rx

           
         def check_module_module_id():

                tx = ":A003001$$"
                ser.write(tx)
                rx = ser.read(24)
                return rx


         def program_scene_events():

                tx = ": PR 002 01 A01 B10021A $$"
                ser.write(tx)


         def confirm_total_events():

                tx = ": PR 002 01 C01$$"
                ser.write(tx)


         def rtc_set_time_prog():

                tx = ":PT003 01 M111111111111 D1111111 T131610$$"
                ser.write(tx)



         def gate_set_time():

                tx = ": GA250814145500$$"
                ser.write(tx)



         def gate_req_time():

                tx = ":GB000$$"
                ser.write(tx)
		rx = ser.read(28)
                rx2 = ser.read(30)
		return rx


         def gate_req_date():

                tx = ":GB000$$"
                ser.write(tx)
                rx = ser.read(30)
		return rx


