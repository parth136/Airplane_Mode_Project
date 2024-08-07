import frappe
import json
from datetime import datetime, date, timedelta

# 'last_rent_paid_date': '2024-08-07', 'rent_due_date': '2024-09-06'
@frappe.whitelist()
def set_due_date(data):
    
    data = json.loads(data)

    date_object = datetime.strptime(data["rent_due_date"], '%Y-%m-%d').date()

    # return_list = []
    new_last_paid_date = date.today()
    new_rent_due_date = date_object + timedelta(days=30)
    
    # return_list.append(new_last_paid_date)
    # return_list.append(new_rent_due_date)

    frappe.db.set_value('Owner Of Shops', data['name'], "last_rent_paid_date",new_last_paid_date)
    frappe.db.set_value('Owner Of Shops', data['name'], "rent_due_date",new_rent_due_date)


    document = frappe.get_list("Shops", filters={"owned_by":data['name1']}, fields=[ "name", "name1", "last_rent_paid_date", "date_of_expiry"])

    frappe.db.set_value("Shops", document[0].name,"last_rent_paid_date",new_last_paid_date)
    frappe.db.set_value("Shops", document[0].name,"date_of_expiry",new_rent_due_date)


    # frappe.db.set_value()
    return None