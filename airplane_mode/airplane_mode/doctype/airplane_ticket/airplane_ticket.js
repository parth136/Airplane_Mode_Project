// Copyright (c) 2024, Parth and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
    
    refresh(frm) {
        
	},
    
    
    
    
    after_save(frm) {
        
        console.log("----------------",frm.doc.status);
        let data = frm.doc
        
        frappe.call({
            doc:frm.doc,
            method:"flight_addons_function",
            args:{
              data:data
            },
            freeze:true,
            freeze_message:"This is freeze message...",
            callback(e){
                //   console.log(e);
                frappe.msgprint(e.message)
            }
            
        })
	},
    
    
    
    // on_submit
    before_submit(frm){
        
        if(frm.doc.status !== "Boarded"){
            frappe.throw("You Cannot submit the document")
            // return false
        }
    },
    
    
    

});
