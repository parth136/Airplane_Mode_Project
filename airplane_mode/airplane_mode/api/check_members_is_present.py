import frappe
from frappe.utils import *
import json

@frappe.whitelist()
def check_crew_members(**args):
    document = frappe.get_list('Members Included In Flight')
    total_member_in_child_table = []
    list1=[]

    print("+++++++++++++++")
    for i in document:
        print(i)
    print("+++++++++++++++")


    # print(len(document))
    for i in range(len(document)):
        # print(i)
        document1 = frappe.get_doc('Members Included In Flight',document[i].name)
        list1.append(document1)
        # print("--------------")
        # print("id----->",document1.name1)
        # print('--------------')
        total_member_in_child_table.append(document1.name1)

    # frappe.msgprint("Helllo")
    # print("+++++++++++++++++++++")
    # print(document)
    # print(document1)
    # print(total_member_in_child_table)
    # print()
    # print("+++++++++++++++++++++")

    # data = json.loads(args['data'])

    # member_in_flight = []
    # for i in data['crew_member']:
    #     member_in_flight.append(i['name'])

    # print('===========================')
    # print(member_in_flight)
    # print('===========================')

    # # document_our = frappe.get_doc('Airplane Flight',)

    return total_member_in_child_table