// Copyright (c) 2026, dvnks systems pvt ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on("ID Card Request", {
	onload(frm) {
		if (frm.is_new() && !frm.doc.employee) {
			frappe.db
				.get_value("Employee", { user_id: frappe.session.user, status: "Active" }, "name")
				.then((r) => r.message?.name && frm.set_value("employee", r.message.name));
		}
	},

	refresh(frm) {
		if (frm.doc.docstatus === 1 && frm.perm[1]?.write) {
			if (!frm.doc.approved_by) {
				frm.add_custom_button(__("Approve"), () => {
					frm.set_value({ approved_by: frappe.session.user });
					frm.save("Update");
				});
			}
			if (!frm.doc.id_card_issued_date) {
				frm.add_custom_button(__("Mark ID Card Issued"), () => {
					frm.set_value({ id_card_issued_date: frappe.datetime.get_today() });
					frm.save("Update");
				});
			}
		}
	},

	request_type(frm) {
		if (frm.doc.request_type === "Replacement (Lost/Damaged)" && !frm.doc.replacement_fee) {
			frm.set_value("replacement_fee", 250);
		}
	},
});
