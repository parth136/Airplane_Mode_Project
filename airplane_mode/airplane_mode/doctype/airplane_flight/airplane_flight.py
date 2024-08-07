# Copyright (c) 2024, Parth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	def validate(self):

		frappe.msgprint("hkijhkj")
		document = frappe.db.get_list("Airplane Ticket",  filters={
        					'flight': self.name
    					},
						fields=["gate_no", 'name']
						)	
		# document.db_set("gate_no",self.gate_number)
		for i in document:
			print("----------->",i)
			frappe.db.set_value("Airplane Ticket", i.name, "gate_no", self.gate_number)