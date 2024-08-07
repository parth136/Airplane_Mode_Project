// Copyright (c) 2024, Parth and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Flight", {
  refresh(frm) {},

  on_submit(frm) {
    status_of_file = frm.doc.status;
    frm.set_value("status", "Completed");
    // frappe.msgprint(frm.doc.status)
  },

  refresh(frm) {
    let members = [];
    console.log(frm.doc);
    frappe.call({
      method:
        "airplane_mode.airplane_mode.api.check_members_is_present.check_crew_members",
      args: {
        data: frm.doc,
      },
      freeze: true,
      freeze_message: "This is freeze message",
      callback(e) {
        console.log(e);
        for (let i = 0; i < e.message.length; i++) {
          members.push(e.message[i]);
        }
        console.log(members);
        console.log(frm.doc);
        frm.set_query("name1", "crew_member", function() {
            return {
                "filters": {
                    'name': ["Not In", members]
                }
            };
        });
    },
    });

    //     frm.fields_dict["crew_member"].get_query = function (doc, cdt, cdn) {
    //       return {
    //         filters: {
    //           name1: ["not in", members],
    //         },   
    //     };
    // };
    
    


    // frm.fields_dict['crew_member'].get_query = function(doc, cdt, cdn) {
    //     return {
    //         filters: {
    //             name1:members
    //         },
    //         // no_create: 1, // Disable "Create New Item"
    //         // query: 'erpnext.controllers.queries.linked_document_query',
    //         // searchfield: 'item_code'
    //     };
    // };

    // frm.set_query("name1", "Members Included In Flight", function() {
    //     return {
    //         "filters": {
    //             'name1': members
    //         }
    //     };
    // });

    // frm.fields_dict.members_included_in_flight.grid.update_docfield_property(
    //     "name1",
    //     "options",
    //     ["".concat(["hello"])]
    //     // [“”].concat([“val 1”, “val 2”, “val 3”])
    //     );

    // frm.set_query("name1", "Members Included In Flight", function() {
    //     console.log("Hereeeeeee");
    //     // return {
    //     //     "filters": {
    //     //         "name1": "",
    //     //         // "group_or_ledger": "Ledger"
    //     //     }
    //     // };
    //     frappe.msgprint("sjgfosdjf")
    //     return null
    // });
  

  },

  
  

});

frappe.ui.form.on("Members Included In Flight", {
  // whenever "state" field is changed
  //     refresh(frm) {
  //         frappe.msgprint("sjgfosdjf")
  //         frm.set_query("name1", () => {
  //             return {
  //             filters: {
  //                 "name1": "hello" // whatever state is selected
  //             }
  //         }
  //     });
  // }
  //   refresh(frm) {
  //     console.log("=========",members);
  //     frm.set_query("name1", "Members Included In Flight", function () {
  //       return {
  //         filters: {
  //           name1: ["Not In", members],
  //         },
  //       };
  //     });
  //   },
});
