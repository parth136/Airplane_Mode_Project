// Copyright (c) 2024, Parth and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
    
    // refresh(frm){

    // },
    
    
    refresh(frm) {
        // let data = ""
        let d = new frappe.ui.Dialog({
            title: 'Enter Seat No.',
            fields: [
                {
                    label: 'Seat No',
                    fieldname: 'seat_no',
                    fieldtype: 'Data'
                },
            ],
            size: 'small', // small, large, extra-large 
            primary_action_label: 'Assign',
            primary_action(values) {
                console.log(frm.doc);
                d.hide();
                frm.doc.seat = values.seat_no
                cur_frm.refresh()
            }
    
        });

        frm.add_custom_button('Assign Seat',()=>{
                d.show()
            },"Action")
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
