import frappe
from frappe.utils import *
import json

@frappe.whitelist()
def set_rent(**args):
    # print("===================")
    # # print(args)
    # print("===================")
    document = frappe.get_doc("Default Rent")
    # print("++++++++++++++++++")
    # print(document.default_rent_amount)
    rent_amount = document.default_rent_amount
    # print("++++++++++++++++++")
    # frappe.set_value("")
    return rent_amount
