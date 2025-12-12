from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns(filters)
    data = get_data(filters)
    return columns, data

def get_columns(filters):
    columns = [
        {"fieldname": "date", "label": _("Date"), "fieldtype": "Date", "width": 120},
        {"fieldname": "work_order", "label": _("Work Order:Link/Work Order"), "fieldtype": "Link", "width": 150},
        {"fieldname": "item_code", "label": _("Item Code:Link/Item"), "fieldtype": "Link", "width": 120},
        {"fieldname": "item_name", "label": _("Item Name"), "fieldtype": "Data", "width": 200},
        {"fieldname": "produced_qty", "label": _("Produced Qty"), "fieldtype": "Float", "width": 100},
        {"fieldname": "rejected_qty", "label": _("Rejected Qty"), "fieldtype": "Float", "width": 100},
        {"fieldname": "rejection_reason", "label": _("Rejection Reason"), "fieldtype": "Text", "width": 200},
        {"fieldname": "status", "label": _("Status"), "fieldtype": "Data", "width": 100},
    ]
    return columns

def get_data(filters):
    conditions = []
    if filters.get("from_date"):
        conditions.append(f"wo.creation >= '{filters['from_date']}'")
    if filters.get("to_date"):
        conditions.append(f"wo.creation <= '{filters['to_date']}'")
    if filters.get("item_code"):
        conditions.append(f"wo.item_code = '{filters['item_code']}'")

    if conditions:
        conditions_clause = " AND " + " AND ".join(conditions)
    else:
        conditions_clause = ""

    data = frappe.db.sql(f"""SELECT
                DATE(wo.creation) as date,
                wo.name as work_order,
                wo.item_code,
                wo.item_name,
                wo.produced_qty,
                wo.rejected_quantity as rejected_qty,
                wo.rejection_reason,
                wo.status
            FROM
                `tabWork Order` wo
            WHERE
                wo.docstatus = 1 {conditions_clause}
            ORDER BY
                wo.creation DESC
        """, as_dict=1)
    return data