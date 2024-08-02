// Copyright (c) 2024, Parth and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
    
    refresh(frm) {
        frm.add_web_link(frm.doc.route, "View in Website");

        
    },

    validate(frm){

        console.log("===================");
        console.log(frm.doc);
        console.log("===================");

        frappe.msgprint("hfksjdhfjksd")
        console.log(frm.doc.route);
        console.log(frm.doc.name);
        // frm.doc.website = "https://www.airindia.com/"
        console.log("after: ",frm.doc.route);
        
        if (frm.doc.name === "AirAsia"){
            frm.doc.route = "https://www.airasia.com/en/gb"
            // window.location.route = "https://www.airasia.com/en/gb";
        }else if(frm.doc.name === "Air India"){
            frm.doc.route = "https://www.airindia.com/"         
        }else{
            frm.doc.route = "https://www.goindigo.in/"
            // window.location='https://www.goindigo.in/'
        }
        


        // if (frm.doc.name === "AirAsia"){
        //     frm.doc.website = "https://www.airasia.com/en/gb"
        // }else if(frm.doc.name === "Air India"){
        //     frm.doc.website = "https://www.airindia.com/"         
        // }else{
        //     frm.doc.website = "https://www.goindigo.in/"         
        // }
    }
    // AirAsia, IndiGo, Air India
});
