// Copyright (c) 2024, Parth and contributors
// For license information, please see license.txt



frappe.ui.form.on("Shops", {
	refresh(frm) {
        
        frappe.call({
            method:
              "airplane_mode.airplane_mode.api.set_rent.set_rent",
            args: {
            },
            freeze: true,
            freeze_message: "This is freeze message",
            callback(e) {
                frm.doc.rent=e.message
                console.log(e.message);
          },
          });


          frm.doc.letter_head = "Payment Recite Letter Head";
	},
});
