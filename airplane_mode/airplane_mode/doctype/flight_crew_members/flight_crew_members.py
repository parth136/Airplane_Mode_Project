# Copyright (c) 2024, Parth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class FlightCrewMembers(Document):
	
	def validate(self):
		self.full_name = self.first_name +" "+self.last_name
