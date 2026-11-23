// Copyright (c) 2026, dvnks systems pvt ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on("Policy Acknowledgement", {
	setup(frm) {
		frm.set_query("hr_policy", () => ({
			filters: { requires_acknowledgement: 1, is_active: 1 },
		}));
		frm.set_query("hr_representative", () => ({ filters: { status: "Active" } }));
	},

	onload(frm) {
		if (frm.is_new() && !frm.doc.employee) {
			frappe.db
				.get_value("Employee", { user_id: frappe.session.user, status: "Active" }, "name")
				.then((r) => r.message?.name && frm.set_value("employee", r.message.name));
		}
		if (frm.is_new() && frm.doc.hr_policy && !(frm.doc.items || []).length) {
			frm.trigger("hr_policy");
		}
	},

	refresh(frm) {
		frm.set_df_property("items", "cannot_add_rows", true);
		frm.set_df_property("items", "cannot_delete_rows", true);
	},

	hr_policy(frm) {
		if (!frm.doc.hr_policy) return;
		frappe
			.call({
				method: "thtpl.thtpl_hr.doctype.policy_acknowledgement.policy_acknowledgement.get_policy_template",
				args: { policy: frm.doc.hr_policy },
			})
			.then(({ message: t }) => {
				frm.set_value({ acknowledgement_intro: t.intro, declaration: t.declaration });
				frm.clear_table("items");
				t.statements.forEach((statement) => frm.add_child("items", { statement }));
				frm.refresh_field("items");
			});
	},
});
