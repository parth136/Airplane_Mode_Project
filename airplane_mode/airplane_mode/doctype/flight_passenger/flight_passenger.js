// Copyright (c) 2024, Parth and contributors
// For license information, please see license.txt

frappe.ui.form.on("Flight Passenger", {
	after_save(frm) {

        let data = frm.doc
        frappe.call({
            doc:frm.doc,
            method:"pyhton_function",
            args:{
              data:data
            },
            freeze:true,
            freeze_message:"This is freeze message...",
            callback(e){
            //   console.log(e);
            frappe.msgprint(e)
            }
    
          })
	},
});
