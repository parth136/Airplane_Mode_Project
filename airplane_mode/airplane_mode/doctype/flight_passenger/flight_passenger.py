# Copyright (c) 2024, parth and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document  


class FlightPassenger(Document):
	# @property
	# def full_name(self):
	# 	return f"{self.first_name} {self.last_name}"
    # pass
    
	print("=======================")
	print("=======================")
	print("=======================")
	
	def validate(self):
		# frappe.db.set_value('Flight Passenger', '9', 'first_name', 'fsjdfok')
		# frappe.db.set_value('Flight Passenger', 9, 'last_name', 44)
		self.update_full_name()
		# document = frappe.get_doc('Flight Passenger', self.flight_passenger)
		# print('==================================')
		# print('document')
		# print('==================================')
	def update_full_name(self):
		# frappe.msgprint("Hello from Parth on before save event")
		# frappe.db.set_value('Flight Passenger', str(self.name), 'first_name', str(self.first_name+" "+self.last_name))
		# frappe.db.set_value('Flight Passenger', 11, 'first_name', 'jdksdsjkd')
		# print()
		# print('---->',self.first_name+" "+self.last_name)
		# print('---->',self.full_name)
		# print()
		document = frappe.get_doc('Flight Passenger', '9')
		# document = frappe.get_doc('test_doctype_2', 'test2-001')
		print()
		print(document.first_name)
		print()

		# document.db_set('full_name', document.first_name+" "+document.last_name)
		# document.insert()


	@frappe.whitelist()
	def pyhton_function(data):
		print()
		print(data)
		print()
		data.db_set('full_name', data.first_name+" "+data.last_name)
		data.save()
		return "hello"

		