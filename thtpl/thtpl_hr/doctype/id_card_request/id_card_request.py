# Copyright (c) 2026, dvnks systems pvt ltd and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

from thtpl.thtpl_hr.utils import require, validate_own_employee

NEW_CARD = "New ID Card"
REPLACEMENT = "Replacement (Lost/Damaged)"
# ID Card Request Form (Thtpl/012): "A penalty/replacement fee of ₹ 250 (or as per company policy)"
DEFAULT_REPLACEMENT_FEE = 250


class IDCardRequest(Document):
	def validate(self):
		validate_own_employee(self.employee)
		if self.request_type != NEW_CARD:
			require(self, ["reason"], _("a replacement or update request"))
		if self.request_type == REPLACEMENT:
			if self.replacement_fee is None or (self.is_new() and not self.replacement_fee):
				self.replacement_fee = DEFAULT_REPLACEMENT_FEE
		else:
			self.replacement_fee = 0
		self.set_status()

	def before_submit(self):
		if not self.declaration:
			frappe.throw(_("Accept the declaration before submitting the request."))

	def before_update_after_submit(self):
		self.set_status()

	def on_cancel(self):
		self.db_set("status", "Cancelled")

	def set_status(self):
		if self.docstatus == 0:
			self.status = "Draft"
		elif self.docstatus == 2:
			self.status = "Cancelled"
		elif self.id_card_issued_date:
			self.status = "Issued"
		elif self.approved_by:
			self.status = "Approved"
		else:
			self.status = "Requested"
