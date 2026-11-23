# Copyright (c) 2026, dvnks systems pvt ltd and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class HRPolicy(Document):
	def validate(self):
		if self.requires_acknowledgement:
			if not self.acknowledgement_form_title:
				self.acknowledgement_form_title = _("{0} Acknowledgement Form").format(self.policy_name)
			if not self.acknowledgement_statements:
				frappe.throw(
					_(
						"Add at least one acknowledgement statement, or untick Requires Employee Acknowledgement."
					)
				)
