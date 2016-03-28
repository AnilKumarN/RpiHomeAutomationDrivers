#!/usr/bin/env python

import serial

class ox_rtc:

         ser = serial.Serial("/dev/ttyAMA0",9600)
         tx=""
         rx=""
 

         def __init__(self):

		tx = ":SETM001$$"
		ser.write(tx.encode("hex"))
		rx = ser.read(30)
		return rx.decode("hex")


	 def check_module_product_id(self):
		
		tx = ":A00507$$"
		ser.write(tx.encode("hex"))
		rx = ser.read(24)
		return rx.decode("hex")

           
         def check_module_module_id(self):

                tx = ":A003001$$"
                ser.write(tx.encode("hex"))
                rx = ser.read(24)
                return rx.decode("hex")


         def program_scene_events(self):

                tx = ": PR 002 01 A01 B10021A $$"
                ser.write(tx.encode("hex"))


         def confirm_total_events(self):

                tx = ": PR 002 01 C01$$"
                ser.write(tx.encode("hex"))


         def rtc_set_time_prog(self):

                tx = ":PT003 01 M111111111111 D1111111 T131610$$"
                ser.write(tx.encode("hex"))



         def gate_set_time(self):

                tx = ": GA250814145500$$"
                ser.write(tx.encode("hex"))



         def gate_req_time(self):

                tx = ":GB000$$"
                ser.write(tx.encode("hex"))
		rx = ser.read(28)
                rx2 = ser.read(30)
		return rx.decode("hex")


         def gate_req_date(self):

                tx = ":GB000$$"
                ser.write(tx.encode("hex"))
                rx = ser.read(30)
		return rx.decode("hex")


