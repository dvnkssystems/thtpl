# Copyright (c) 2026, dvnks systems pvt ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import cint


class MisconductType(Document):
	def autoname(self):
		"""Minor-01 … Minor-08, Major-01 … Major-28: numbered per category, as in the Disciplinary Policy."""
		prefix = f"{self.category}-"
		existing = frappe.get_all("Misconduct Type", filters={"name": ["like", f"{prefix}%"]}, pluck="name")
		last = max((cint(n.rsplit("-", 1)[-1]) for n in existing), default=0)
		self.name = f"{prefix}{last + 1:02d}"
