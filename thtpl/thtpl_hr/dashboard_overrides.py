# Copyright (c) 2026, dvnks systems pvt ltd and contributors
# For license information, please see license.txt

from frappe import _


def get_dashboard_for_employee(data):
	# PoSH and whistleblower complaints are deliberately left out: they are restricted to their committees.
	data["transactions"].append(
		{
			"label": _("Policies & Discipline"),
			"items": ["Policy Acknowledgement", "Disciplinary Action", "ID Card Request"],
		}
	)
	return data
