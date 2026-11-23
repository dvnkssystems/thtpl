# Copyright (c) 2026, dvnks systems pvt ltd and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import get_datetime


class VisitorLog(Document):
	def validate(self):
		if self.check_out and get_datetime(self.check_out) < get_datetime(self.check_in):
			frappe.throw(_("Check-out Time cannot be before Check-in Time."))
		self.status = "Checked Out" if self.check_out else "Checked In"
