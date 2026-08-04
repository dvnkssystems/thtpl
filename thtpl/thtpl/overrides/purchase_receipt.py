import frappe
from frappe.utils import flt


def update_po_rejected_qty(doc, method=None):
	"""Roll up rejected qty from this Purchase Receipt onto the linked
	Purchase Order(s), on both submit and cancel of the Purchase Receipt."""
	purchase_orders = {row.purchase_order for row in doc.items if row.purchase_order}

	for purchase_order in purchase_orders:
		_recalculate_rejected_qty(purchase_order)


def _recalculate_rejected_qty(purchase_order):
	rejected_by_po_item = dict(
		frappe.db.sql(
			"""
			select pri.purchase_order_item, sum(pri.rejected_qty)
			from `tabPurchase Receipt Item` pri
			inner join `tabPurchase Receipt` pr on pr.name = pri.parent
			where pri.purchase_order = %s and pr.docstatus = 1
			group by pri.purchase_order_item
			""",
			purchase_order,
		)
	)

	total_rejected_qty = 0.0
	for po_item_name in frappe.get_all(
		"Purchase Order Item", filters={"parent": purchase_order}, pluck="name"
	):
		item_rejected_qty = flt(rejected_by_po_item.get(po_item_name))
		frappe.db.set_value(
			"Purchase Order Item", po_item_name, "rejected_qty", item_rejected_qty, update_modified=False
		)
		total_rejected_qty += item_rejected_qty

	frappe.db.set_value(
		"Purchase Order", purchase_order, "total_rejected_qty", total_rejected_qty, update_modified=False
	)
