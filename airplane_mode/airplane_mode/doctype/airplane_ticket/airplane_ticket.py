# Copyright (c) 2024, Parth and contributors
# For license information, please see license.txt

import frappe
import random, string
from frappe.model.document import Document


class AirplaneTicket(Document):
	

	# before_insert

	
	# def seat_no(self):

	# 	document = frappe.get_doc(self.doctype, self.name)
	# 	print("--------------------")
	# 	print(document)
	# 	print('---------------------')

	# 	data = self.seat
	# 	int_part = int(random.random()*100)
	# 	str_part = str.capitalize(random.choice(string.ascii_letters))
	# 	seat_no = str(int_part)+str_part
		
	# 	frappe.db.set_value('Airplane Ticket', 'IndiGo-008-07-2024-BOM-to-CCU-027', "seat", seat_no)
	# 	print('=======')
	# 	print('999999999999')
	# 	print('=======')
		
	# 	# str_part = random.randrange(['A-Z'])

	# 	# document.db_set('email', 'def@hhh.com')
	# 	# document.db_set('seat',seat_no)
	# 	# document.save()

	# 	# frappe.db.set_value('Client Side Scripting', 'PPP-007', 'age', 44)










	
	# @frappe.whitelist()
	# def status_check(data):
	# 	print("++++++++++++")
	# 	print(type(data.status))
	# 	print("++++++++++++")
	# 	if data.status != "Boarded":
	# 		frappe.throw("You cannot submit the ticket because you havent boarded")
	# 		# return 0
	# 	# else:
	# 	# 	frappe.msgprint("You have boarded the flight. Thankyou")
	# 	return None	
	# 	# print("++++++++++++")









	@frappe.whitelist()
	def flight_addons_function(data):
		# print()
		# print('----->',data)
		# print()
		# document.get('test_child_doc')[1].name
		print('============')
		# print(data.get('add_ons')[1].name)
		print('============')
		# frappe.delete_doc('test_doctype_1', 'test-019')
		# name = data.get('add_ons')[1].name
		
		# frappe.delete_doc('airplane_ticket_add_on_item', name)

		# child_document = frappe.get_doc("", name)
		# child_document.delete()
		

		addons_cost = 0.0
		add_ons_list = []
		for add_ons in data.add_ons:
			if add_ons.item in add_ons_list:
				continue
			add_ons_list.append(add_ons.item)
			# print(add_ons.amount)
			addons_cost = addons_cost + add_ons.amount
			# if add_ons.item in addons:
			# 	break
			# addons.append(addons.item)
		add_ons_list=[]

		total_amount = data.flight_price + addons_cost

		print('+++++++++++',total_amount)

		data.db_set('total_amount', total_amount)
		data.save()
		
		print('============')
		return None
	

	
	def before_insert(self):
		# document = frappe.get_doc(self.doctype, self.name)
		# print("--------------------")
		# print(document)
		# print('---------------------')

		# data = self.seat

		# seat no. logic with python
		# int_part = int(random.random()*100)
		# str_part = str.capitalize(random.choice(string.ascii_letters))
		# seat_no = str(int_part)+str_part
		
		# frappe.db.set_value(self.doctype, self.name, "seat", str(seat_no))
		# frappe.msgprint('kkkkk')
		# self.db_set("seat", seat_no)
		# self.seat = seat_no
		# self.save()
		print('=======')
		# print('999999999999', seat_no, self.name)
		print('=======')
		
		# self.seat_no()

	def before_insert(self):
		print("----------")
		
		flight_var = self.flight
		flight_split = flight_var.split('-')
		check = 0
		airline_name=""
		for i in flight_split:
			if check > 1:
				break
			if check == 0:
				airline_name = i+'-'
			else:
				airline_name = airline_name + i
			check = check+1

		document = frappe.get_doc("Airplane", airline_name)



		# getting all the tickets in that flight

		document2 = frappe.db.get_all('Airplane Ticket',

				fields=['name'],
				order_by='name desc',
				# group_by='flight',
				# as_tuple=1,
				# unique=0
		)

		count = 0
		for i in document2:
			# print('+++++++',i)
			if airline_name in str(i):
				# print(i)
				count = count + 1

		if count >= document.capacity:
			frappe.throw("Flight is full, you cant get ticket. Sorry.")
		print("----------")
	


# SELECT * FROM `tabairplane_ticket_add_on_item`;








