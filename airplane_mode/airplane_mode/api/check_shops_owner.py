import frappe
from frappe.utils import *
import json

@frappe.whitelist()
def check_shop_owners(data):
    document = frappe.get_list('Owned Shops')
    # print("+++++++++++++")
    # for i in document:
    #     print(i.name)
    # print("+++++++++++++")

    total_shops_owned =[]
    for i in range(len(document)):
        # print(i)
        document1 = frappe.get_doc('Owned Shops',document[i].name)
        total_shops_owned.append(document1.shop_name)
    return total_shops_owned