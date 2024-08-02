// Copyright (c) 2024, Parth and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Flight", {
	refresh(frm) {

	},


    on_submit(frm){
        status_of_file = frm.doc.status
        frm.set_value("status", "Completed")
        // frappe.msgprint(frm.doc.status)
    },

});
