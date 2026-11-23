# Copyright (c) 2026, dvnks systems pvt ltd and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import getdate

from thtpl.thtpl_hr.utils import get_default_company

# Complainant details wiped when a complaint is marked anonymous.
ANONYMOUS_CLEARS = ("complainant", "complainant_name", "complainant_contact", "complainant_relationship")


class WhistleblowerComplaint(Document):
	"""Concern raised under the Fraud and Whistleblower Policy.

	Visible only to the Whistleblower Committee role: HR and line managers do not get access.
	"""

	def validate(self):
		if not self.company:
			self.company = get_default_company()
		if self.anonymous:
			for fieldname in ANONYMOUS_CLEARS:
				self.set(fieldname, None)
		if self.closed_on and getdate(self.closed_on) < getdate(self.complaint_date):
			frappe.throw(_("Closed On cannot be before the date the complaint was received."))
		self.set_status()

	def set_status(self):
		if self.closed_on:
			self.status = "Closed"
		elif self.investigation_started_on:
			self.status = "Under Investigation"
		else:
			self.status = "Open"
