# Copyright (c) 2026, dvnks systems pvt ltd and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import add_days, add_months, getdate

from thtpl.thtpl_hr.utils import add_working_days, get_default_company, require


class PoSHComplaint(Document):
	"""Complaint under the PoSH Policy (Sexual Harassment of Women at Workplace Act, 2013).

	Visible only to the PoSH Internal Committee role: HR and line managers do not get access.
	"""

	def validate(self):
		if not self.company:
			self.company = get_default_company()
		if self.complainant_is_employee:
			require(self, ["complainant"], _("an employee complainant"))
		if self.respondent_is_employee:
			require(self, ["respondent"], _("an employee respondent"))
		self.validate_dates()
		self.set_due_dates()
		self.set_status()

	def validate_dates(self):
		if getdate(self.incident_date) > getdate(self.complaint_date):
			frappe.throw(_("Date of Incident cannot be after the date the complaint was received."))
		# PoSH Policy: "A complaint must be submitted in writing within 3 months of the incident."
		if getdate(self.complaint_date) > add_months(getdate(self.incident_date), 3):
			frappe.msgprint(
				_(
					"This complaint was received more than 3 months after the incident. "
					"Record the Internal Committee's reasons for accepting it."
				),
				indicator="orange",
				alert=True,
			)
		if (
			self.appeal_filed_on
			and self.final_report_on
			and getdate(self.appeal_filed_on) > add_days(getdate(self.final_report_on), 90)
		):
			frappe.msgprint(
				_("The appeal was filed more than 90 days after the final report."),
				indicator="orange",
				alert=True,
			)

	def set_due_dates(self):
		"""Timelines from the PoSH Policy, 'Inquiry Process & Timelines'."""
		received = self.complaint_date
		self.respondent_informed_due = add_working_days(received, 3, self.company)
		self.preliminary_response_due = add_working_days(received, 3, self.company)
		self.complainant_informed_due = add_working_days(received, 5, self.company)
		self.preliminary_assessment_due = add_days(received, 15)
		self.inquiry_due = add_days(received, 90)
		self.final_report_due = add_days(self.inquiry_completed_on, 10) if self.inquiry_completed_on else None
		self.employer_action_due = add_days(self.final_report_on, 60) if self.final_report_on else None
		self.appeal_due = (
			add_working_days(self.appeal_filed_on, 5, self.company) if self.appeal_filed_on else None
		)

	def set_status(self):
		if self.closed_on:
			self.status = "Closed"
		elif self.appeal_filed_on and not self.appeal_decided_on:
			self.status = "Under Appeal"
		elif self.employer_action_on:
			self.status = "Action Taken"
		elif self.inquiry_completed_on:
			self.status = "Inquiry Completed"
		elif self.respondent_informed_on or self.preliminary_assessment_on:
			self.status = "Under Inquiry"
		else:
			self.status = "Open"
