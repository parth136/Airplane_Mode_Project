// Copyright (c) 2024, Parth and contributors
// For license information, please see license.txt

frappe.ui.form.on("Owner Of Shops", {
	refresh(frm) {

        frappe.call({
            method:
              "airplane_mode.airplane_mode.api.check_shops_owner.check_shop_owners",
            args: {
              data: frm.doc,
            },
            freeze: true,
            freeze_message: "This is freeze message",
            callback(e) {
                let shops_occupied=[]  
              console.log(e);
              for (let i = 0; i < e.message.length; i++) {
                shops_occupied.push(e.message[i]);
              }
              console.log(shops_occupied);
              console.log(frm.doc);
              frm.set_query("shop_name", "owned_shops", function() {
                  return {
                      "filters": {
                          'name': ["Not In", shops_occupied]
                      }
                  };
              });
          },
          });




        let rent_pay = new frappe.ui.Dialog({
          title: 'Enter Rent:',
          fields: [
              {
                  label: 'Rent Amount',
                  fieldname: 'rent_paied',
                  fieldtype: 'Currency',
                  default: 50000.00,
                  read_only:1
              },
          ],
          size: 'small', // small, large, extra-large 
          primary_action_label: 'Pay',
          primary_action(values) {
              // console.log(frm.doc);
              // frm.doc.seat = values.rent_pay
              // cur_frm.refresh()
              frappe.call({
                method:"airplane_mode.airplane_mode.api.rent_pay.set_due_date",
                args:{
                  data:frm.doc,
                },
                freeze:true,
                freeze_message:"Please wait...",
                callback(e){
                  // for (let i = 0; i < e.message.length; i++) {
                  //   console.log(e.message[i]);
                  //   if(i==0){
                  //     frm.doc.last_rent_paid_date = e.message[i]
                  //   }else{
                  //     frm.doc.rent_due_date = e.message[i]
                  //   }
                  // }
                  // frappe.msgprint("Your rent is paid!! Thankyou.")
                }
              })
              cur_frm.refresh()
              rent_pay.hide();
            }
      });



      frm.add_custom_button('Pay Rent',()=>{
        rent_pay.show()
        },"Rent")

	},
});
