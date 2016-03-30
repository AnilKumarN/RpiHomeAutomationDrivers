#!/usr/bin/env python

import serial

class oxd5s05:

	ser = serial.Serial("/dev/ttyAMA0",9600)
	tx=""
	rx=""

	def __init__():

		tx = ":SETM001$$"
		ser.write(tx)
		rx = ser.read(15)
		return rx


	def check_module_product_id():
		
		tx = ":A00510$$"
		ser.write(tx)
		rx = ser.read(12)
		return rx

	def check_module_product_id():
		
		tx = ":A003001$$"
		ser.write(tx)
		rx = ser.read(12)
		return rx


	def operate_single_load():

		tx = ":B10021A$$"
		ser.write(tx)


	def operate_all_loads():

		tx = ":B2002AAX00$$"
		ser.write(tx)

	def check_load_status():

		tx = ":B3002$$"
		ser.write(tx)
		rx = ser.read(12)
		return rx

	def default_on():
		
		tx = ":D($$"
		ser.write(tx)

	def default_off():

		tx = ":D)$$"
		ser.write(tx)
