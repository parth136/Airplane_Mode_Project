# Copyright (c) 2024, Parth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import date, timedelta

class OwnerOfShops(Document):
# after_insert
	def after_insert(self):
		# frappe.db.set_value("Owned Shops", "", "gate_no", self.gate_number)
		document = self.get("owned_shops")
		print("============")
		for i in document:
			i.owned_by = self.name
			
			frappe.db.set_value("Shops", i.shop_name, "owned_by", self.name)
			frappe.db.set_value("Shops", i.shop_name, "last_rent_paid_date", date.today())
			frappe.db.set_value("Shops", i.shop_name, "date_of_expiry", date.today() + timedelta(days=30))
			
		print("============")
		if self.owned_shops:
			self.last_rent_paid_date = date.today()
			self.rent_due_date = date.today() + timedelta(days=30)
		# document2=frappe.get_doc("")
		# print("99999999999999")
		# for i in self.get("owned_shops"):
		# 	print("{0}".format(i.shop_name))
		# print("9999999999999999")


	
		
		
