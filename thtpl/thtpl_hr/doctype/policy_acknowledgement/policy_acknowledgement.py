# Copyright (c) 2026, dvnks systems pvt ltd and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

from thtpl.thtpl_hr.utils import validate_own_employee


class PolicyAcknowledgement(Document):
	def validate(self):
		validate_own_employee(self.employee)
		if self.docstatus == 0 and self.hr_policy:
			self.sync_with_policy()

	def sync_with_policy(self):
		"""Statements always mirror the policy while in draft; ticks survive for unchanged statements."""
		template = _get_template(self.hr_policy)
		ticked = {row.statement for row in self.items if row.acknowledged}
		if [row.statement for row in self.items] != template["statements"]:
			self.set(
				"items",
				[{"statement": s, "acknowledged": 1 if s in ticked else 0} for s in template["statements"]],
			)
		self.form_title = template["form_title"]
		self.acknowledgement_intro = template["intro"]
		self.declaration = template["declaration"]

	def before_submit(self):
		policy = frappe.db.get_value(
			"HR Policy", self.hr_policy, ["is_active", "requires_acknowledgement"], as_dict=True
		)
		if not (policy and policy.is_active and policy.requires_acknowledgement):
			frappe.throw(
				_("Policy {0} is not active for acknowledgement.").format(frappe.bold(self.hr_policy))
			)

		unticked = [str(row.idx) for row in self.items if not row.acknowledged]
		if unticked:
			frappe.throw(
				_("Tick every acknowledgement before submitting. Unticked rows: {0}").format(
					", ".join(unticked)
				)
			)
		if not self.agreed_to_declaration:
			frappe.throw(_("Confirm the Employee Declaration before submitting."))


def _get_template(policy: str) -> dict:
	doc = frappe.get_cached_doc("HR Policy", policy)
	return {
		"form_title": doc.acknowledgement_form_title,
		"intro": doc.acknowledgement_intro,
		"declaration": doc.declaration,
		"statements": [row.statement for row in doc.acknowledgement_statements],
	}


@frappe.whitelist()
def get_policy_template(policy: str) -> dict:
	frappe.has_permission("HR Policy", "read", policy, throw=True)
	return _get_template(policy)
