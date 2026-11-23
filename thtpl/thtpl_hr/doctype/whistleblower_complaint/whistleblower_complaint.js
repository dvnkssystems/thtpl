// Copyright (c) 2026, dvnks systems pvt ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on("Whistleblower Complaint", {
	onload(frm) {
		if (frm.is_new() && !frm.doc.company) {
			frm.set_value("company", frappe.defaults.get_user_default("Company"));
		}
	},

	refresh(frm) {
		frm.set_intro(
			__(
				"Confidential. Do not contact the person concerned or discuss this case outside the committee."
			),
			"red"
		);
	},
});
