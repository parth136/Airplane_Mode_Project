# Copyright (c) 2024, Parth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Shops(Document):
	# after_insert
	def after_insert(self):
		documents = frappe.db.get_list("Shops",fields=['name', 'airport','owned_by'],)
		print("------------")
		for i in documents:
			print("--->",i)
		print("------------")
		print()
		document2 = frappe.get_list("Airport",fields=['name'])
		# print("+++++++++++++++++++")
		# print(document2)
		# print("+++++++++++++++++++")
		shops_number = []
		avaliable_for_lease = []
		count = 0
		count2 = 0
		for i in document2:
			dict_name={i.name:None}
			dict_owned_by={i.name:None}
			for j in documents:
				if i.name == j.airport:
					count=count+1
					if j.owned_by == None:
						count2=count2+1
			dict_owned_by[i.name]=count2
			avaliable_for_lease.append(dict_owned_by)
			count2=0
			dict_name[i.name]=count
			shops_number.append(dict_name)
			count=0
		
		
		print("000000000")
		print(shops_number)
		print("000000000")
		print()
		print("000000000")
		print(avaliable_for_lease)
		print("000000000")

		for i in range(len(shops_number)):
			for j, k in shops_number[i].items():
				frappe.db.set_value("Airport", j, "number_of_shops", k)

		for i in range(len(avaliable_for_lease)):
			for j, k in avaliable_for_lease[i].items():
				frappe.db.set_value("Airport", j, "number_of_shops_available_for_lease", k)


	# def validate(self):
	

