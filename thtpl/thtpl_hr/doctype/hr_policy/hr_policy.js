// Copyright (c) 2026, dvnks systems pvt ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on("HR Policy", {
	refresh(frm) {
		if (!frm.is_new() && frm.doc.requires_acknowledgement && frm.doc.is_active) {
			frm.add_custom_button(
				__("Policy Acknowledgement"),
				() => {
					frappe.new_doc("Policy Acknowledgement", { hr_policy: frm.doc.name });
				},
				__("Create")
			);
		}
	},
});
