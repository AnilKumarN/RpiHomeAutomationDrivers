#!/usr/bin/env python

import serial

class oxd5s05:

	ser = serial.Serial("/dev/ttyAMA0",9600)
	tx=""
	rx=""

	def __init__():

		tx = ":SETM001$$"
		ser.write(tx.encode("hex"))
		rx = ser.read(30)
		return rx.decode("hex")


	def check_module_product_id():
		
		tx = ":A00510$$"
		ser.write(tx.encode("hex"))
		rx = ser.read(24)
		return rx.decode("hex")

	def check_module_product_id():
		
		tx = ":A003001$$"
		ser.write(tx.encode("hex"))
		rx = ser.read(24)
		return rx.decode("hex")


	def operate_single_load():

		tx = ":B10021A$$"
		ser.write(tx.encode("hex"))


	def operate_all_loads():

		tx = ":B2002AAX00$$"
		ser.write(tx.encode("hex"))

	def check_load_status():

		tx = ":B3002$$"
		ser.write(tx.encode("hex"))
		rx = ser.read(24)
		return rx.decode("hex")

	def default_on():
		
		tx = ":D($$"
		ser.write(tx.encode("hex"))

	def default_off():

		tx = ":D)$$"
		ser.write(tx.encode("hex"))
