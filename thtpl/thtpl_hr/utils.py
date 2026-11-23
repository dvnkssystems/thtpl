# Copyright (c) 2026, dvnks systems pvt ltd and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import add_days, getdate

HR_ROLES = {"HR Manager", "HR User", "System Manager"}


def is_hr_user(user: str | None = None) -> bool:
	return bool(HR_ROLES.intersection(frappe.get_roles(user)))


def validate_own_employee(employee: str | None) -> None:
	"""Employees using self-service may only raise records for themselves."""
	if not employee or is_hr_user():
		return
	if frappe.db.get_value("Employee", employee, "user_id") != frappe.session.user:
		frappe.throw(_("You can only raise this request for yourself."), frappe.PermissionError)


def require(doc, fieldnames: list[str], reason: str) -> None:
	"""Server-side twin of `mandatory_depends_on` (the browser enforces it, imports and the API do not)."""
	missing = [doc.meta.get_label(f) for f in fieldnames if not doc.get(f)]
	if missing:
		frappe.throw(
			_("{0} is mandatory for {1}.").format(", ".join(frappe.bold(_(m)) for m in missing), reason),
			frappe.MandatoryError,
		)


def add_working_days(date, days: int, company: str | None = None):
	"""Add working days, skipping the company's default holiday list (calendar days if it has none)."""
	if not date:
		return None
	holidays = set()
	holiday_list = company and frappe.get_cached_value("Company", company, "default_holiday_list")
	if holiday_list:
		holidays = {
			getdate(d)
			for d in frappe.db.get_all(
				"Holiday",
				filters={"parent": holiday_list, "parenttype": "Holiday List"},
				pluck="holiday_date",
			)
		}
	date = getdate(date)
	added = 0
	while added < days:
		date = add_days(date, 1)
		if date not in holidays:
			added += 1
	return date


def get_default_company() -> str | None:
	return frappe.defaults.get_user_default("Company") or frappe.db.get_single_value(
		"Global Defaults", "default_company"
	)
