# Copyright (c) 2026, dvnks systems pvt ltd and contributors
# For license information, please see license.txt

"""Seed THTPL HR masters from the client's documents (runs once; never overwrites site edits).

- HR Policy: the 24 THTPL policies (text as in the client's .docx), with the Code of Conduct
  Acknowledgement Form statements on the Code of Conduct policy.
- Misconduct Type: the 8 minor and 28 major acts listed in the Disciplinary Policy.
"""

import json
import os

import frappe


def execute():
	base = frappe.get_app_path("thtpl", "thtpl_hr", "setup_data")

	with open(os.path.join(base, "misconduct_types.json"), encoding="utf-8") as fh:
		for row in json.load(fh):
			if not frappe.db.exists("Misconduct Type", row):
				frappe.get_doc({"doctype": "Misconduct Type", **row}).insert(ignore_permissions=True)

	with open(os.path.join(base, "hr_policies.json"), encoding="utf-8") as fh:
		for row in json.load(fh):
			if not frappe.db.exists("HR Policy", row["policy_name"]):
				frappe.get_doc({"doctype": "HR Policy", **row}).insert(ignore_permissions=True)
