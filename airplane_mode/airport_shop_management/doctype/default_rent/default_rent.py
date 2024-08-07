# Copyright (c) 2024, Parth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class DefaultRent(Document):
	def validate(self):
		notification_reminder = self.rent_reminders
		print("++++++++++++++++")
		print(notification_reminder)

		frappe.db.set_value("Notification","Rent Due Reminder","enabled",notification_reminder)
		print("++++++++++++++++")
