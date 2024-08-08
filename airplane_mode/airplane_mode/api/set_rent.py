import frappe
from frappe.utils import *
import json
import json

@frappe.whitelist()
def set_rent(**args):
    print("===================")
    data = json.loads(args["data"])
    print(data)
    print("===================")
    document = frappe.get_doc("Default Rent")
    # print("++++++++++++++++++")
    # print(document.default_rent_amount)
    rent_amount = document.default_rent_amount
    # print("++++++++++++++++++")
    # frappe.set_value("")
    frappe.db.set_value('Shops', data['name'], "rent",rent_amount)

    
    return None
