// Copyright (c) 2026, dvnks systems pvt ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on("PoSH Complaint", {
	onload(frm) {
		if (frm.is_new() && !frm.doc.company) {
			frm.set_value("company", frappe.defaults.get_user_default("Company"));
		}
	},

	refresh(frm) {
		frm.set_intro(
			__(
				"Confidential. All proceedings, identities, documents and findings must remain strictly confidential (Section 16, PoSH Act 2013)."
			),
			"red"
		);
		frm.trigger("highlight_overdue");
	},

	highlight_overdue(frm) {
		const today = frappe.datetime.get_today();
		const pairs = [
			["respondent_informed_on", "respondent_informed_due"],
			["preliminary_response_on", "preliminary_response_due"],
			["complainant_informed_on", "complainant_informed_due"],
			["preliminary_assessment_on", "preliminary_assessment_due"],
			["inquiry_completed_on", "inquiry_due"],
			["final_report_on", "final_report_due"],
			["employer_action_on", "employer_action_due"],
			["appeal_decided_on", "appeal_due"],
		];
		const overdue = pairs
			.filter(
				([done, due]) =>
					!frm.doc[done] && frm.doc[due] && frm.doc[due] < today && !frm.doc.closed_on
			)
			.map(([done]) => __(frappe.meta.get_label(frm.doctype, done, frm.doc.name)));
		if (overdue.length) {
			frm.dashboard.set_headline_alert(
				`<span class="indicator red">${__("Overdue")}: ${overdue.join(", ")}</span>`
			);
		} else {
			frm.dashboard.clear_headline();
		}
	},
});
