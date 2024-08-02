frappe.ready(function(e) {
	// bind events here
	// frappe.web_form.set_value('flight', frm.doc.flight)
	// value = frappe.web_form.get_value('flight');
	// console.log(value);
	const urlParams = new URLSearchParams(window.location.search);
	const my_param = urlParams.get('flight');
	
	console.log("============",urlParams, e);

	// frappe.web_form.set_value('flight', 'IndiGo-008-07-2024')
})

// doc.status=="Scheduled"