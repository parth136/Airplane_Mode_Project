# Copyright (c) 2024, Parth and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):	
	columns = [
		{
			"fieldname":"airline",
			"label":"Airline",
			"fieldtype":"Link",
			"options":"airline",
			"width":150
		},
		{
			"fieldname":"revenue",
			"label":"Revenue",
			"fieldtype":"Currency",
			"width":100
		}
	]
	
	
	airplanes_amount = frappe.get_all("Airplane Ticket",fields=["flight","total_amount"])
	airline = frappe.get_all("Airline", fields="name", order_by="name asc")

	
	print("==================")
	
	amount_list = []
	for i in airline:
		temp = 0
		for j in airplanes_amount:
			if i['name'] in j['flight']:
				temp = temp + j['total_amount']
		amount_list.append({i['name']:int(temp)})
			# print(i['name'])

	# for j in airplanes_amount:
	# 	print(j['total_amount'])

	data = []
	for i in amount_list:
		data.append(i)

	print(list(amount_list[0].keys())[0])
	print("==================")
	print("DATA: ",data)
	
	
	data = [{"airline":list(amount_list[0].keys())[0], "revenue":list(amount_list[0].values())[0]}, {"airline":list(amount_list[1].keys())[0], "revenue":list(amount_list[1].values())[0]}, {"airline":list(amount_list[2].keys())[0], "revenue":list(amount_list[2].values())[0]}]
	

	chart = {
		'data':{
			'labels':[list(amount_list[0].keys())[0],list(amount_list[1].keys())[0],list(amount_list[2].keys())[0]],
			'datasets':[{'values':[list(amount_list[0].values())[0],list(amount_list[1].values())[0],list(amount_list[2].values())[0]]}]
			},
			'type':'donut',
			'height':300,
			}


	total = list(amount_list[0].values())[0] + list(amount_list[1].values())[0] + list(amount_list[2].values())[0]

	report_summary = [
		{
			"label":"Total Amount:", 
			"value":total,
			'indicator':'Green'
		}
	]
	return columns, data, None, chart, report_summary
