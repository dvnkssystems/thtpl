// Copyright (c) 2026, dvnks systems pvt ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on("Visitor Log", {
	refresh(frm) {
		if (!frm.is_new() && !frm.doc.check_out) {
			frm.add_custom_button(__("Check Out"), () => {
				frappe.confirm(
					__("Has the visitor returned the visitor pass?"),
					() =>
						frm
							.set_value({
								check_out: frappe.datetime.now_datetime(),
								pass_returned: 1,
							})
							.then(() => frm.save()),
					() =>
						frm
							.set_value({
								check_out: frappe.datetime.now_datetime(),
								pass_returned: 0,
							})
							.then(() => frm.save())
				);
			}).addClass("btn-primary");
		}
	},
});
