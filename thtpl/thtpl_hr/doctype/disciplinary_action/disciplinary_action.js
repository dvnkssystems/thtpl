// Copyright (c) 2026, dvnks systems pvt ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on("Disciplinary Action", {
	setup(frm) {
		frm.set_query("previous_action", () => ({
			filters: { employee: frm.doc.employee, docstatus: 1, name: ["!=", frm.doc.name] },
		}));
		frm.set_query("appraisal", () => ({ filters: { employee: frm.doc.employee } }));
	},

	refresh(frm) {
		frm.trigger("show_active_actions");
		if (frm.doc.docstatus === 1) {
			frm.add_custom_button(__("Escalate"), () => {
				frappe.new_doc("Disciplinary Action", {
					employee: frm.doc.employee,
					misconduct_type: frm.doc.misconduct_type,
					previous_action: frm.doc.name,
				});
			});
		}
	},

	employee(frm) {
		frm.trigger("show_active_actions");
	},

	show_active_actions(frm) {
		frm.set_intro("");
		if (!frm.doc.employee || frm.doc.docstatus !== 0) return;
		frappe.db
			.get_list("Disciplinary Action", {
				filters: {
					employee: frm.doc.employee,
					docstatus: 1,
					valid_till: [">=", frappe.datetime.get_today()],
					name: ["!=", frm.doc.name],
				},
				fields: ["name", "action_type", "valid_till"],
				order_by: "action_date desc",
			})
			.then((rows) => {
				if (!rows.length) return;
				const list = rows
					.map(
						(r) =>
							`${r.action_type} (${r.name}, valid till ${frappe.datetime.str_to_user(
								r.valid_till
							)})`
					)
					.join(", ");
				frm.set_intro(
					__("Active disciplinary records for this employee: {0}", [list]),
					"orange"
				);
			});
	},
});
