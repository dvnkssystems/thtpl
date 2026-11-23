# Copyright (c) 2026, dvnks systems pvt ltd and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import add_months, getdate

from thtpl.thtpl_hr.utils import require

# Fields each action type needs (mirrors `mandatory_depends_on` in the form).
REQUIRED_BY_TYPE = {
	"Verbal Caution": ["details"],
	"Verbal Warning": ["details"],
	"Show Cause Notice": ["details", "explanation_within"],
	"Warning Letter": ["warning_regarding", "issue", "details", "improvement_period"],
	"Warning Notice for Poor Performance": ["improvement_tasks", "improvement_period"],
	"Suspension": ["details", "suspension_from", "suspension_to"],
	"Decision Making Leave": ["details"],
	"Absconding Notice": ["employee_address", "absent_since", "report_within"],
}

# Disciplinary Policy: how long each record stays in effect (months).
VALIDITY_MONTHS = {
	"Verbal Caution": 1,  # "may remain valid for a period of up to One month"
	"Verbal Warning": 1,  # "will remain in effect for One month"
	"Warning Letter": 3,  # written warning: "three to six months based on the nature of the misconduct"
	"Suspension": 3,  # "will remain in effect for three months"
}


class DisciplinaryAction(Document):
	def validate(self):
		require(self, REQUIRED_BY_TYPE.get(self.action_type, []), _(self.action_type))
		self.validate_dates()
		self.validate_previous_action()
		self.set_valid_till()
		self.set_status()

	def validate_dates(self):
		if (
			self.suspension_from
			and self.suspension_to
			and getdate(self.suspension_to) < getdate(self.suspension_from)
		):
			frappe.throw(_("Suspension To cannot be before Suspension From."))
		if self.absent_since and getdate(self.absent_since) > getdate(self.action_date):
			frappe.throw(_("Absent Since cannot be after the notice date."))

	def validate_previous_action(self):
		if not self.previous_action:
			return
		if self.previous_action == self.name:
			frappe.throw(_("Previous Action cannot be this record itself."))
		if frappe.db.get_value("Disciplinary Action", self.previous_action, "employee") != self.employee:
			frappe.throw(
				_("Previous Action {0} belongs to a different employee.").format(self.previous_action)
			)

	def set_valid_till(self):
		months = VALIDITY_MONTHS.get(self.action_type)
		if months and not self.valid_till:
			self.valid_till = add_months(getdate(self.action_date), months)

	def before_update_after_submit(self):
		self.set_status()

	def on_cancel(self):
		self.db_set("status", "Cancelled")

	def set_status(self):
		if self.docstatus == 0:
			self.status = "Draft"
		elif self.docstatus == 2:
			self.status = "Cancelled"
		elif self.closed_on:
			self.status = "Closed"
		elif self.response_received_on:
			self.status = "Response Received"
		else:
			self.status = "Issued"
