import os
import json
from datetime import datetime

# --- Configuration ---
APP_NAME = "thtpl"
BASE_PATH = os.getcwd() # Or specify your bench apps directory, e.g., "/path/to/your/bench/apps"

# Define the custom fields data
custom_fields_data = [
  {
    "doctype": "Item",
    "fieldname": "design_change_notes",
    "label": "Design Change Notes",
    "fieldtype": "Table MultiSelect",
    "options": "Design Change Note",
    "insert_after": "item_code",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Project",
    "fieldname": "design_inputs",
    "label": "Design Inputs",
    "fieldtype": "Text",
    "insert_after": "description",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Project",
    "fieldname": "related_design_changes",
    "label": "Related Design Changes",
    "fieldtype": "Table MultiSelect",
    "options": "Design Change Note",
    "insert_after": "design_inputs",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Quotation",
    "fieldname": "enquiry_review_status",
    "label": "Enquiry Review Status",
    "fieldtype": "Select",
    "options": "Draft\nReviewed\nApproved\nRejected",
    "insert_after": "order_type",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": "Draft",
    "module": APP_NAME
  },
  {
    "doctype": "Quotation",
    "fieldname": "enquiry_review_notes",
    "label": "Enquiry Review Notes",
    "fieldtype": "Text",
    "insert_after": "enquiry_review_status",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Issue",
    "fieldname": "complaint_category",
    "label": "Complaint Category",
    "fieldtype": "Select",
    "options": "Product Quality\nService\nDelivery\nOther",
    "insert_after": "subject",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Issue",
    "fieldname": "root_cause_analysis",
    "label": "Root Cause Analysis",
    "fieldtype": "Text",
    "insert_after": "description",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Issue",
    "fieldname": "corrective_action",
    "label": "Corrective Action",
    "fieldtype": "Text",
    "insert_after": "root_cause_analysis",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Issue",
    "fieldname": "preventive_action",
    "label": "Preventive Action",
    "fieldtype": "Text",
    "insert_after": "corrective_action",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Supplier",
    "fieldname": "evaluation_status",
    "label": "Evaluation Status",
    "fieldtype": "Select",
    "options": "New\nUnder Evaluation\nApproved\nRejected",
    "insert_after": "supplier_group",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": "New",
    "module": APP_NAME
  },
  {
    "doctype": "Supplier",
    "fieldname": "approved_for_items",
    "label": "Approved for Items",
    "fieldtype": "Table MultiSelect",
    "options": "Item",
    "insert_after": "evaluation_status",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Supplier",
    "fieldname": "next_audit_date",
    "label": "Next Audit Date",
    "fieldtype": "Date",
    "insert_after": "approved_for_items",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Supplier",
    "fieldname": "audit_history",
    "label": "Audit History",
    "fieldtype": "Table MultiSelect",
    "options": "External Provider Audit Report",
    "insert_after": "next_audit_date",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Item",
    "fieldname": "shelf_life_days",
    "label": "Shelf Life (Days)",
    "fieldtype": "Int",
    "insert_after": "has_batch_no",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Batch",
    "fieldname": "mfg_date",
    "label": "Manufacturing Date",
    "fieldtype": "Date",
    "insert_after": "expiry_date",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Maintenance Request",
    "fieldname": "breakdown_analysis",
    "label": "Breakdown Analysis",
    "fieldtype": "Text",
    "insert_after": "description",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Maintenance Request",
    "fieldname": "root_cause",
    "label": "Root Cause",
    "fieldtype": "Small Text",
    "insert_after": "breakdown_analysis",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Maintenance Request",
    "fieldname": "corrective_actions",
    "label": "Corrective Actions",
    "fieldtype": "Text",
    "insert_after": "root_cause",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Maintenance Request",
    "fieldname": "preventive_actions",
    "label": "Preventive Actions",
    "fieldtype": "Text",
    "insert_after": "corrective_actions",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Maintenance Request",
    "fieldname": "analysis_report_attachment",
    "label": "Analysis Report Attachment",
    "fieldtype": "Attach",
    "insert_after": "preventive_actions",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Maintenance Schedule",
    "fieldname": "procedure_attachment",
    "label": "Procedure Attachment",
    "fieldtype": "Attach",
    "insert_after": "description",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Production Plan",
    "fieldname": "capacity_plan_attachment",
    "label": "Capacity Plan Attachment",
    "fieldtype": "Attach",
    "insert_after": "sales_order",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Work Order",
    "fieldname": "rejected_quantity",
    "label": "Rejected Quantity",
    "fieldtype": "Float",
    "insert_after": "qty",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": "0",
    "module": APP_NAME
  },
  {
    "doctype": "Work Order",
    "fieldname": "rejection_reason",
    "label": "Rejection Reason",
    "fieldtype": "Text",
    "insert_after": "rejected_quantity",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Work Order",
    "fieldname": "daily_log_attachment",
    "label": "Daily Log Attachment",
    "fieldtype": "Attach",
    "insert_after": "rejection_reason",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Asset",
    "fieldname": "is_calibratable",
    "label": "Is Calibratable",
    "fieldtype": "Check",
    "insert_after": "is_stock_item",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": "0",
    "module": APP_NAME
  },
  {
    "doctype": "Asset",
    "fieldname": "last_calibration_date",
    "label": "Last Calibration Date",
    "fieldtype": "Date",
    "insert_after": "is_calibratable",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Asset",
    "fieldname": "calibration_frequency_days",
    "label": "Calibration Frequency (Days)",
    "fieldtype": "Int",
    "insert_after": "last_calibration_date",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Asset",
    "fieldname": "next_calibration_date",
    "label": "Next Calibration Date",
    "fieldtype": "Date",
    "insert_after": "calibration_frequency_days",
    "read_only": 1,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Training Event",
    "fieldname": "effectiveness_verified",
    "label": "Effectiveness Verified",
    "fieldtype": "Check",
    "insert_after": "status",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": "0",
    "module": APP_NAME
  },
  {
    "doctype": "Training Event",
    "fieldname": "verification_date",
    "label": "Verification Date",
    "fieldtype": "Date",
    "insert_after": "effectiveness_verified",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Training Event",
    "fieldname": "verification_notes",
    "label": "Verification Notes",
    "fieldtype": "Text",
    "insert_after": "verification_date",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Employee",
    "fieldname": "induction_training_status",
    "label": "Induction Training Status",
    "fieldtype": "Select",
    "options": "Not Started\nIn Progress\nCompleted",
    "insert_after": "status",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": "Not Started",
    "module": APP_NAME
  },
  {
    "doctype": "Employee",
    "fieldname": "induction_completion_date",
    "label": "Induction Completion Date",
    "fieldtype": "Date",
    "insert_after": "induction_training_status",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  },
  {
    "doctype": "Operation",
    "fieldname": "related_sop",
    "label": "Related SOP",
    "fieldtype": "Link",
    "options": "Standard Operating Procedure",
    "insert_after": "quality_inspection",
    "read_only": 0,
    "reqd": 0,
    "hidden": 0,
    "default": None,
    "module": APP_NAME
  }
]

# Define DocType structures (excluding the child DocType `Auditor Details` which is nested)
doctypes_to_create = {
    "Design Change Request": {
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0, "autoname": "format:DCR-{YY}-{MM}-{#####}",
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "title", "fieldtype": "Data", "label": "Title", "reqd": 1},
  {"fieldname": "request_date", "fieldtype": "Date", "label": "Request Date", "default": "Today", "reqd": 1},
  {"fieldname": "requested_by", "fieldtype": "Link", "label": "Requested By", "options": "Employee", "reqd": 1},
  {"fieldname": "description", "fieldtype": "Small Text", "label": "Description of Change", "reqd": 1},
  {"fieldname": "reason_for_change", "fieldtype": "Text", "label": "Reason for Change", "reqd": 1},
  {"fieldname": "proposed_change", "fieldtype": "Text", "label": "Proposed Change Details"},
  {"fieldname": "impact_analysis", "fieldtype": "Text", "label": "Impact Analysis"},
  {"fieldname": "affected_items", "fieldtype": "Table MultiSelect", "label": "Affected Items/BOMs", "options": "Item"},
  {"fieldname": "status", "fieldtype": "Select", "label": "Status", "options": "Draft\\nSubmitted\\nApproved\\nRejected\\nImplemented", "default": "Draft", "reqd": 1},
  {"fieldname": "attachment", "fieldtype": "Attach", "label": "Attachment"}
 ],
 "index_web_pages_for_search": 1, "is_submittable": 1, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "Design Change Request", "owner": "Administrator",
 "permissions": [
  {"create": 1, "delete": 1, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "System Manager", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "Manufacturing User", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "Quality Manager", "share": 1, "write": 1}
 ],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 1, "track_seen": 0, "track_views": 0, "naming_series": "DCR-"
}
        """,
        "child_doctypes": []
    },
    "Design Change Note": {
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0, "autoname": "format:DCN-{YY}-{MM}-{#####}",
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "title", "fieldtype": "Data", "label": "Title", "reqd": 1},
  {"fieldname": "dcr_reference", "fieldtype": "Link", "label": "DCR Reference", "options": "Design Change Request"},
  {"fieldname": "change_date", "fieldtype": "Date", "label": "Change Date", "default": "Today", "reqd": 1},
  {"fieldname": "approved_by", "fieldtype": "Link", "label": "Approved By", "options": "Employee", "reqd": 1},
  {"fieldname": "description_of_change", "fieldtype": "Text", "label": "Description of Implemented Change", "reqd": 1},
  {"fieldname": "new_specifications", "fieldtype": "Text", "label": "New Specifications"},
  {"fieldname": "effective_date", "fieldtype": "Date", "label": "Effective Date", "reqd": 1},
  {"fieldname": "version_number", "fieldtype": "Data", "label": "New Version Number", "reqd": 1},
  {"fieldname": "attachment", "fieldtype": "Attach", "label": "Attachment"}
 ],
 "index_web_pages_for_search": 1, "is_submittable": 0, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "Design Change Note", "owner": "Administrator",
 "permissions": [
  {"create": 1, "delete": 1, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "System Manager", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "Manufacturing User", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "Quality Manager", "share": 1, "write": 1}
 ],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 1, "track_seen": 0, "track_views": 0, "naming_series": "DCN-"
}
        """,
        "child_doctypes": []
    },
    "Tender": {
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0, "autoname": "format:TEND-{FY}-{#####}",
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "tender_id", "fieldtype": "Data", "label": "Tender ID", "reqd": 1, "unique": 1},
  {"fieldname": "opportunity", "fieldtype": "Link", "label": "Opportunity", "options": "Opportunity"},
  {"fieldname": "customer", "fieldtype": "Link", "label": "Customer", "options": "Customer", "reqd": 1},
  {"fieldname": "submission_date", "fieldtype": "Date", "label": "Submission Date", "reqd": 1},
  {"fieldname": "closing_date", "fieldtype": "Date", "label": "Closing Date"},
  {"fieldname": "tender_value", "fieldtype": "Currency", "label": "Tender Value"},
  {"fieldname": "status", "fieldtype": "Select", "label": "Status", "options": "Draft\\nSubmitted\\nUnder Review\\nWon\\nLost", "default": "Draft", "reqd": 1},
  {"fieldname": "attachment", "fieldtype": "Attach", "label": "Attachment"},
  {"fieldname": "submission_checklist", "fieldtype": "Table", "label": "Submission Checklist", "options": "Tender Checklist Item"}
 ],
 "index_web_pages_for_search": 1, "is_submittable": 0, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "Tender", "owner": "Administrator",
 "permissions": [
  {"create": 1, "delete": 1, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "System Manager", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "Sales User", "share": 1, "write": 1}
 ],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 1, "track_seen": 0, "track_views": 0, "naming_series": "TEND-"
}
        """,
        "child_doctypes": ["Tender Checklist Item"]
    },
    "Tender Checklist Item": { # Child DocType
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0,
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "item", "fieldtype": "Data", "label": "Checklist Item", "reqd": 1},
  {"fieldname": "completed", "fieldtype": "Check", "label": "Completed"},
  {"fieldname": "notes", "fieldtype": "Small Text", "label": "Notes"}
 ],
 "index_web_pages_for_search": 0, "is_submittable": 0, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "Tender Checklist Item", "owner": "Administrator",
 "permissions": [],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 0, "track_seen": 0, "track_views": 0, "istable": 1
}
        """,
        "child_doctypes": []
    },
    "Customer Feedback": {
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0, "autoname": "format:CFB-{YY}-{MM}-{#####}",
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "customer", "fieldtype": "Link", "label": "Customer", "options": "Customer", "reqd": 1},
  {"fieldname": "feedback_date", "fieldtype": "Date", "label": "Feedback Date", "default": "Today", "reqd": 1},
  {"fieldname": "survey_type", "fieldtype": "Select", "label": "Survey Type", "options": "General\\nProduct\\nService\\nDelivery", "reqd": 1},
  {"fieldname": "rating", "fieldtype": "Int", "label": "Rating (1-5)", "options": "1\\n2\\n3\\n4\\n5"},
  {"fieldname": "comments", "fieldtype": "Text", "label": "Comments"},
  {"fieldname": "action_taken", "fieldtype": "Text", "label": "Action Taken"},
  {"fieldname": "status", "fieldtype": "Select", "label": "Status", "options": "New\\nIn Progress\\nClosed", "default": "New", "reqd": 1}
 ],
 "index_web_pages_for_search": 1, "is_submittable": 0, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "Customer Feedback", "owner": "Administrator",
 "permissions": [
  {"create": 1, "delete": 1, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "System Manager", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "Sales User", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "Quality Manager", "share": 1, "write": 1}
 ],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 1, "track_seen": 0, "track_views": 0, "naming_series": "CFB-"
}
        """,
        "child_doctypes": []
    },
    "External Provider Audit Plan": {
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0, "autoname": "format:EPAP-{audit_year}-{#####}",
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "title", "fieldtype": "Data", "label": "Title", "reqd": 1},
  {"fieldname": "audit_year", "fieldtype": "Int", "label": "Audit Year", "default": "2025", "reqd": 1},
  {"fieldname": "planned_start_date", "fieldtype": "Date", "label": "Planned Start Date", "reqd": 1},
  {"fieldname": "planned_end_date", "fieldtype": "Date", "label": "Planned End Date", "reqd": 1},
  {"fieldname": "auditors", "fieldtype": "Table", "label": "Auditors", "options": "Auditor Details"},
  {"fieldname": "scope", "fieldtype": "Text", "label": "Scope of Audit", "reqd": 1},
  {"fieldname": "status", "fieldtype": "Select", "label": "Status", "options": "Draft\\nPlanned\\nIn Progress\\nCompleted", "default": "Draft", "reqd": 1},
  {"fieldname": "attachment", "fieldtype": "Attach", "label": "Attachment"}
 ],
 "index_web_pages_for_search": 1, "is_submittable": 0, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "External Provider Audit Plan", "owner": "Administrator",
 "permissions": [
  {"create": 1, "delete": 1, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "System Manager", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "Quality Manager", "share": 1, "write": 1},
  {"create": 0, "delete": 0, "email": 0, "export": 0, "print": 0, "read": 1, "report": 0, "role": "Auditor", "share": 0, "write": 0}
 ],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 1, "track_seen": 0, "track_views": 0, "naming_series": "EPAP-"
}
        """,
        "child_doctypes": ["Auditor Details"]
    },
    "Auditor Details": { # Child DocType
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0,
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "auditor", "fieldtype": "Link", "label": "Auditor", "options": "Employee", "reqd": 1},
  {"fieldname": "role", "fieldtype": "Data", "label": "Role (Lead/Team)", "reqd": 1}
 ],
 "index_web_pages_for_search": 0, "is_submittable": 0, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "Auditor Details", "owner": "Administrator",
 "permissions": [],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 0, "track_seen": 0, "track_views": 0, "istable": 1
}
        """,
        "child_doctypes": []
    },
    "External Provider Audit Report": {
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0, "autoname": "format:EPAR-{YY}-{MM}-{#####}",
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "audit_plan_ref", "fieldtype": "Link", "label": "Audit Plan Reference", "options": "External Provider Audit Plan", "reqd": 1},
  {"fieldname": "provider", "fieldtype": "Link", "label": "External Provider (Supplier)", "options": "Supplier", "reqd": 1},
  {"fieldname": "audit_date", "fieldtype": "Date", "label": "Audit Date", "default": "Today", "reqd": 1},
  {"fieldname": "lead_auditor", "fieldtype": "Link", "label": "Lead Auditor", "options": "Employee", "reqd": 1},
  {"fieldname": "findings", "fieldtype": "Text", "label": "Audit Findings"},
  {"fieldname": "non_conformities", "fieldtype": "Table", "label": "Non Conformities", "options": "Non Conformity Detail"},
  {"fieldname": "observations", "fieldtype": "Text", "label": "Observations"},
  {"fieldname": "recommendations", "fieldtype": "Text", "label": "Recommendations"},
  {"fieldname": "overall_rating", "fieldtype": "Int", "label": "Overall Rating (1-5)", "options": "1\\n2\\n3\\n4\\n5"},
  {"fieldname": "status", "fieldtype": "Select", "label": "Status", "options": "Draft\\nSubmitted\\nApproved\\nClosed", "default": "Draft", "reqd": 1},
  {"fieldname": "attachment", "fieldtype": "Attach", "label": "Attachment (Audit Report Document)"},
  {"fieldname": "next_audit_due", "fieldtype": "Date", "label": "Next Audit Due Date"}
 ],
 "index_web_pages_for_search": 1, "is_submittable": 1, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "External Provider Audit Report", "owner": "Administrator",
 "permissions": [
  {"create": 1, "delete": 1, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "System Manager", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "Quality Manager", "share": 1, "write": 1},
  {"create": 0, "delete": 0, "email": 0, "export": 0, "print": 0, "read": 1, "report": 0, "role": "Auditor", "share": 0, "write": 0}
 ],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 1, "track_seen": 0, "track_views": 0, "naming_series": "EPAR-"
}
        """,
        "child_doctypes": ["Non Conformity Detail"]
    },
    "Non Conformity Detail": { # Child DocType
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0,
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "description", "fieldtype": "Small Text", "label": "Description", "reqd": 1},
  {"fieldname": "severity", "fieldtype": "Select", "label": "Severity", "options": "Minor\\nMajor\\nCritical", "reqd": 1},
  {"fieldname": "corrective_action_required", "fieldtype": "Text", "label": "Corrective Action Required"},
  {"fieldname": "due_date", "fieldtype": "Date", "label": "Due Date"},
  {"fieldname": "status", "fieldtype": "Select", "label": "Status", "options": "Open\\nClosed", "default": "Open", "reqd": 1}
 ],
 "index_web_pages_for_search": 0, "is_submittable": 0, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "Non Conformity Detail", "owner": "Administrator",
 "permissions": [],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 0, "track_seen": 0, "track_views": 0, "istable": 1
}
        """,
        "child_doctypes": []
    },
    "Calibration Record": {
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0, "autoname": "format:CAL-{YY}-{MM}-{#####}",
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "instrument", "fieldtype": "Link", "label": "Instrument (Asset)", "options": "Asset", "reqd": 1},
  {"fieldname": "calibration_date", "fieldtype": "Date", "label": "Calibration Date", "default": "Today", "reqd": 1},
  {"fieldname": "calibrated_by", "fieldtype": "Link", "label": "Calibrated By", "options": "Employee", "reqd": 1},
  {"fieldname": "next_due_date", "fieldtype": "Date", "label": "Next Due Date", "reqd": 1},
  {"fieldname": "calibration_certificate", "fieldtype": "Attach", "label": "Calibration Certificate"},
  {"fieldname": "status", "fieldtype": "Select", "label": "Status", "options": "Calibrated\\nDue\\nOverdue\\nOut of Calibration", "default": "Calibrated", "reqd": 1}
 ],
 "index_web_pages_for_search": 1, "is_submittable": 0, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "Calibration Record", "owner": "Administrator",
 "permissions": [
  {"create": 1, "delete": 1, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "System Manager", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "Maintenance User", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "Quality Manager", "share": 1, "write": 1}
 ],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 1, "track_seen": 0, "track_views": 0, "naming_series": "CAL-"
}
        """,
        "child_doctypes": []
    },
    "Welder Qualification": {
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0, "autoname": "format:WQD-{welder}-{qualification_id}",
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "welder", "fieldtype": "Link", "label": "Welder (Employee)", "options": "Employee", "reqd": 1},
  {"fieldname": "qualification_id", "fieldtype": "Data", "label": "Qualification ID", "reqd": 1, "unique": 1},
  {"fieldname": "process", "fieldtype": "Select", "label": "Welding Process", "options": "SMAW\\nGTAW\\nFCAW\\nMIG\\nTIG\\nOther", "reqd": 1},
  {"fieldname": "material_group", "fieldtype": "Data", "label": "Material Group Qualified For", "reqd": 1},
  {"fieldname": "thickness_range", "fieldtype": "Data", "label": "Thickness Range Qualified For"},
  {"fieldname": "qualification_date", "fieldtype": "Date", "label": "Qualification Date", "reqd": 1},
  {"fieldname": "expiry_date", "fieldtype": "Date", "label": "Expiry Date", "reqd": 1},
  {"fieldname": "continuity_record", "fieldtype": "Table", "label": "Welding Continuity Record", "options": "Welding Continuity Log"},
  {"fieldname": "certificate_attachment", "fieldtype": "Attach", "label": "Certificate Attachment"}
 ],
 "index_web_pages_for_search": 1, "is_submittable": 0, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "Welder Qualification", "owner": "Administrator",
 "permissions": [
  {"create": 1, "delete": 1, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "System Manager", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "HR Manager", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "Quality Manager", "share": 1, "write": 1}
 ],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 1, "track_seen": 0, "track_views": 0, "naming_series": "WQD-"
}
        """,
        "child_doctypes": ["Welding Continuity Log"]
    },
    "Welding Continuity Log": { # Child DocType
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0,
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "date", "fieldtype": "Date", "label": "Date", "reqd": 1},
  {"fieldname": "work_performed", "fieldtype": "Small Text", "label": "Work Performed (Details)", "reqd": 1},
  {"fieldname": "supervisor", "fieldtype": "Link", "label": "Supervisor", "options": "Employee"}
 ],
 "index_web_pages_for_search": 0, "is_submittable": 0, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "Welding Continuity Log", "owner": "Administrator",
 "permissions": [],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 0, "track_seen": 0, "track_views": 0, "istable": 1
}
        """,
        "child_doctypes": []
    },
    "Deviation Note": {
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0, "autoname": "format:DEV-{YY}-{MM}-{#####}",
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "reference_doc", "fieldtype": "Data", "label": "Reference Document/Process"},
  {"fieldname": "deviation_date", "fieldtype": "Date", "label": "Deviation Date", "default": "Today", "reqd": 1},
  {"fieldname": "reported_by", "fieldtype": "Link", "label": "Reported By", "options": "Employee", "reqd": 1},
  {"fieldname": "description", "fieldtype": "Text", "label": "Description of Deviation", "reqd": 1},
  {"fieldname": "proposed_solution", "fieldtype": "Text", "label": "Proposed Solution"},
  {"fieldname": "approver", "fieldtype": "Link", "label": "Approved By", "options": "Employee"},
  {"fieldname": "approval_date", "fieldtype": "Date", "label": "Approval Date"},
  {"fieldname": "status", "fieldtype": "Select", "label": "Status", "options": "Draft\\nSubmitted\\nApproved\\nRejected\\nClosed", "default": "Draft", "reqd": 1},
  {"fieldname": "attachment", "fieldtype": "Attach", "label": "Attachment"}
 ],
 "index_web_pages_for_search": 1, "is_submittable": 1, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "Deviation Note", "owner": "Administrator",
 "permissions": [
  {"create": 1, "delete": 1, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "System Manager", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "Quality User", "share": 1, "write": 1},
  {"create": 0, "delete": 0, "email": 0, "export": 0, "print": 0, "read": 1, "report": 0, "role": "Quality Auditor", "share": 0, "write": 0}
 ],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 1, "track_seen": 0, "track_views": 0, "naming_series": "DEV-"
}
        """,
        "child_doctypes": []
    },
    "Safety Incident": {
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0, "autoname": "format:SINC-{YY}-{MM}-{#####}",
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "incident_date", "fieldtype": "Date", "label": "Incident Date", "default": "Today", "reqd": 1},
  {"fieldname": "incident_time", "fieldtype": "Time", "label": "Incident Time"},
  {"fieldname": "location", "fieldtype": "Data", "label": "Location", "reqd": 1},
  {"fieldname": "reported_by", "fieldtype": "Link", "label": "Reported By", "options": "Employee", "reqd": 1},
  {"fieldname": "affected_personnel", "fieldtype": "Table", "label": "Affected Personnel", "options": "Affected Person"},
  {"fieldname": "description", "fieldtype": "Text", "label": "Description of Incident", "reqd": 1},
  {"fieldname": "severity", "fieldtype": "Select", "label": "Severity", "options": "Minor\\nModerate\\nMajor", "reqd": 1},
  {"fieldname": "root_cause", "fieldtype": "Text", "label": "Root Cause Analysis"},
  {"fieldname": "corrective_actions", "fieldtype": "Text", "label": "Corrective Actions Taken"},
  {"fieldname": "preventive_actions", "fieldtype": "Text", "label": "Preventive Actions Proposed"},
  {"fieldname": "status", "fieldtype": "Select", "label": "Status", "options": "Open\\nInvestigated\\nClosed", "default": "Open", "reqd": 1},
  {"fieldname": "attachment", "fieldtype": "Attach", "label": "Attachment"}
 ],
 "index_web_pages_for_search": 1, "is_submittable": 1, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "Safety Incident", "owner": "Administrator",
 "permissions": [
  {"create": 1, "delete": 1, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "System Manager", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "HR User", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "Safety User", "share": 1, "write": 1}
 ],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 1, "track_seen": 0, "track_views": 0, "naming_series": "SINC-"
}
        """,
        "child_doctypes": ["Affected Person"]
    },
    "Affected Person": { # Child DocType
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0,
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "person", "fieldtype": "Link", "label": "Affected Person", "options": "Employee"},
  {"fieldname": "injury_type", "fieldtype": "Small Text", "label": "Injury Type"},
  {"fieldname": "medical_attention", "fieldtype": "Check", "label": "Medical Attention Required"}
 ],
 "index_web_pages_for_search": 0, "is_submittable": 0, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "Affected Person", "owner": "Administrator",
 "permissions": [],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 0, "track_seen": 0, "track_views": 0, "istable": 1
}
        """,
        "child_doctypes": []
    },
    "Safety Equipment Register": {
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0, "autoname": "format:SER-{equipment_name}-{#####}",
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "equipment_name", "fieldtype": "Data", "label": "Equipment Name", "reqd": 1},
  {"fieldname": "asset", "fieldtype": "Link", "label": "Linked Asset (Optional)", "options": "Asset"},
  {"fieldname": "location", "fieldtype": "Data", "label": "Location", "reqd": 1},
  {"fieldname": "last_inspection_date", "fieldtype": "Date", "label": "Last Inspection Date", "reqd": 1},
  {"fieldname": "next_inspection_date", "fieldtype": "Date", "label": "Next Inspection Date", "reqd": 1},
  {"fieldname": "status", "fieldtype": "Select", "label": "Status", "options": "OK\\nNeeds Service\\nOut of Order", "default": "OK", "reqd": 1},
  {"fieldname": "inspection_log", "fieldtype": "Table", "label": "Inspection Log", "options": "Equipment Inspection Log"}
 ],
 "index_web_pages_for_search": 1, "is_submittable": 0, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "Safety Equipment Register", "owner": "Administrator",
 "permissions": [
  {"create": 1, "delete": 1, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "System Manager", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "Maintenance User", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "Safety User", "share": 1, "write": 1}
 ],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 1, "track_seen": 0, "track_views": 0, "naming_series": "SER-"
}
        """,
        "child_doctypes": ["Equipment Inspection Log"]
    },
    "Equipment Inspection Log": { # Child DocType
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0,
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "inspection_date", "fieldtype": "Date", "label": "Inspection Date", "reqd": 1},
  {"fieldname": "inspected_by", "fieldtype": "Link", "label": "Inspected By", "options": "Employee"},
  {"fieldname": "condition", "fieldtype": "Text", "label": "Condition/Notes", "reqd": 1},
  {"fieldname": "action_taken", "fieldtype": "Text", "label": "Action Taken"}
 ],
 "index_web_pages_for_search": 0, "is_submittable": 0, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "Equipment Inspection Log", "owner": "Administrator",
 "permissions": [],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 0, "track_seen": 0, "track_views": 0, "istable": 1
}
        """,
        "child_doctypes": []
    },
    "Document Register": {
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0, "autoname": "format:DOCREG-{document_id}",
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "document_id", "fieldtype": "Data", "label": "Document ID", "reqd": 1, "unique": 1},
  {"fieldname": "document_name", "fieldtype": "Data", "label": "Document Name", "reqd": 1},
  {"fieldname": "document_type", "fieldtype": "Select", "label": "Document Type", "options": "Internal\\nExternal\\nCustomer Drawing\\nStandard\\nSOP", "reqd": 1},
  {"fieldname": "revision", "fieldtype": "Data", "label": "Revision"},
  {"fieldname": "issue_date", "fieldtype": "Date", "label": "Issue Date", "default": "Today", "reqd": 1},
  {"fieldname": "effective_date", "fieldtype": "Date", "label": "Effective Date"},
  {"fieldname": "owner", "fieldtype": "Link", "label": "Document Owner", "options": "Employee"},
  {"fieldname": "related_doctype", "fieldtype": "Small Text", "label": "Related DocType (e.g., Customer, Project)"},
  {"fieldname": "related_document", "fieldtype": "Dynamic Link", "label": "Related Document", "options": "related_doctype"},
  {"fieldname": "attachment", "fieldtype": "Attach", "label": "Document File"},
  {"fieldname": "status", "fieldtype": "Select", "label": "Status", "options": "Draft\\nIssued\\nSuperseded\\nObsolete", "default": "Issued", "reqd": 1}
 ],
 "index_web_pages_for_search": 1, "is_submittable": 0, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "Document Register", "owner": "Administrator",
 "permissions": [
  {"create": 1, "delete": 1, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "System Manager", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "Document Controller", "share": 1, "write": 1}
 ],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 1, "track_seen": 0, "track_views": 0, "naming_series": "DOCREG-"
}
        """,
        "child_doctypes": []
    },
    "Mock Drill Report": {
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0, "autoname": "format:MDR-{drill_date}-{#####}",
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "drill_date", "fieldtype": "Date", "label": "Drill Date", "default": "Today", "reqd": 1},
  {"fieldname": "drill_type", "fieldtype": "Select", "label": "Drill Type", "options": "Fire\\nEvacuation\\nFirst Aid\\nOther", "reqd": 1},
  {"fieldname": "scenario", "fieldtype": "Text", "label": "Scenario/Objective", "reqd": 1},
  {"fieldname": "participants", "fieldtype": "Table", "label": "Participants", "options": "Drill Participant"},
  {"fieldname": "observations", "fieldtype": "Text", "label": "Observations"},
  {"fieldname": "areas_for_improvement", "fieldtype": "Text", "label": "Areas for Improvement"},
  {"fieldname": "recommendations", "fieldtype": "Text", "label": "Recommendations"},
  {"fieldname": "report_by", "fieldtype": "Link", "label": "Reported By", "options": "Employee", "reqd": 1},
  {"fieldname": "attachment", "fieldtype": "Attach", "label": "Attachment"}
 ],
 "index_web_pages_for_search": 1, "is_submittable": 0, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "Mock Drill Report", "owner": "Administrator",
 "permissions": [
  {"create": 1, "delete": 1, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "System Manager", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "Safety User", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "HR User", "share": 1, "write": 1}
 ],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 1, "track_seen": 0, "track_views": 0, "naming_series": "MDR-"
}
        """,
        "child_doctypes": ["Drill Participant"]
    },
    "Drill Participant": { # Child DocType
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0,
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "employee", "fieldtype": "Link", "label": "Employee", "options": "Employee", "reqd": 1}
 ],
 "index_web_pages_for_search": 0, "is_submittable": 0, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "Drill Participant", "owner": "Administrator",
 "permissions": [],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 0, "track_seen": 0, "track_views": 0, "istable": 1
}
        """,
        "child_doctypes": []
    },
    "Standard Operating Procedure": {
        "json": """
{
 "allow_copy": 0, "allow_import": 0, "allow_rename": 0, "autoname": "format:SOP-{sop_id}",
 "creation": "2025-12-12 12:00:00.000000", "custom": 0, "docstatus": 0, "doctype": "DocType",
 "editable_grid": 1, "engine": "InnoDB",
 "fields": [
  {"fieldname": "sop_id", "fieldtype": "Data", "label": "SOP ID", "reqd": 1, "unique": 1},
  {"fieldname": "title", "fieldtype": "Data", "label": "Title", "reqd": 1},
  {"fieldname": "version", "fieldtype": "Data", "label": "Version", "default": "1.0", "reqd": 1},
  {"fieldname": "effective_date", "fieldtype": "Date", "label": "Effective Date", "default": "Today", "reqd": 1},
  {"fieldname": "reviewed_by", "fieldtype": "Link", "label": "Reviewed By", "options": "Employee"},
  {"fieldname": "next_review_date", "fieldtype": "Date", "label": "Next Review Date"},
  {"fieldname": "department", "fieldtype": "Link", "label": "Department", "options": "Department"},
  {"fieldname": "content", "fieldtype": "Text Editor", "label": "SOP Content"},
  {"fieldname": "attachment", "fieldtype": "Attach", "label": "Attachment (PDF version)"},
  {"fieldname": "status", "fieldtype": "Select", "label": "Status", "options": "Draft\\nApproved\\nArchived", "default": "Draft", "reqd": 1}
 ],
 "index_web_pages_for_search": 1, "is_submittable": 0, "links": [],
 "modified": "2025-12-12 12:00:00.000000", "modified_by": "Administrator", "module": "THTPL",
 "name": "Standard Operating Procedure", "owner": "Administrator",
 "permissions": [
  {"create": 1, "delete": 1, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "System Manager", "share": 1, "write": 1},
  {"create": 1, "delete": 0, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, "role": "Quality Manager", "share": 1, "write": 1},
  {"create": 0, "delete": 0, "email": 0, "export": 0, "print": 0, "read": 1, "report": 0, "role": "Manufacturing User", "share": 0, "write": 0}
 ],
 "quick_entry": 1, "read_only": 0, "sort_field": "creation", "sort_order": "DESC",
 "track_changes": 1, "track_seen": 0, "track_views": 0, "naming_series": "SOP-"
}
        """,
        "child_doctypes": []
    }
}


# Define reports to create
reports_to_create = {
    "grir_outstanding_report": {
        "json_content": """
        {
            "doctype": "Report",
            "name": "GRIR Outstanding Report",
            "ref_doctype": "Purchase Receipt",
            "report_type": "Query Report",
            "is_standard": "Yes",
            "module": "THTPL",
            "idx": 0,
            "json_fields": null,
            "prepared_report": 0,
            "query": null,
            "roles": [
                { "role": "Accounts Manager" },
                { "role": "Stock Manager" },
                { "role": "System Manager" }
            ]
        }
        """,
        "sql_content": """
        -- Example SQL for GRIR Outstanding Report (simplified, may need refinement for exact logic)
        -- This query identifies Purchase Receipts for which no corresponding Purchase Invoice has been created.
        SELECT
            pr.name AS "Purchase Receipt",
            pr.posting_date AS "Receipt Date",
            pr.supplier AS "Supplier",
            pr.grand_total AS "Receipt Total",
            (pr.grand_total - IFNULL(SUM(pin.grand_total), 0)) AS "Outstanding Amount"
        FROM
            `tabPurchase Receipt` pr
        LEFT JOIN
            `tabPurchase Invoice Item` pii ON pr.name = pii.purchase_receipt
        LEFT JOIN
            `tabPurchase Invoice` pin ON pii.parent = pin.name
        WHERE
            pr.docstatus = 1 AND pr.status != "Cancelled"
            AND pr.is_subcontracted = 0 -- Exclude subcontracting if not relevant
        GROUP BY
            pr.name
        HAVING
            "Outstanding Amount" > 0;

        -- You would typically need a more complex query or a Script Report
        -- to handle all GRIR scenarios, including invoices without receipts.
        """
    },
    "batch_expiry_report": {
        "json_content": """
        {
            "doctype": "Report",
            "name": "Batch Expiry Report",
            "ref_doctype": "Batch",
            "report_type": "Query Report",
            "is_standard": "Yes",
            "module": "THTPL",
            "idx": 0,
            "json_fields": null,
            "prepared_report": 0,
            "query": null,
            "roles": [
                { "role": "Stock Manager" },
                { "role": "Quality Manager" },
                { "role": "System Manager" }
            ]
        }
        """,
        "sql_content": """
        -- Example SQL for Batch Expiry Report
        SELECT
            b.name AS "Batch ID",
            b.item_code AS "Item Code:Link/Item",
            i.item_name AS "Item Name",
            b.expiry_date AS "Expiry Date:Date",
            b.batch_qty AS "Batch Quantity",
            sle.warehouse AS "Warehouse:Link/Warehouse"
        FROM
            `tabBatch` b
        JOIN
            `tabItem` i ON b.item_code = i.item_code
        LEFT JOIN
            `tabStock Ledger Entry` sle ON b.name = sle.batch_no AND b.item_code = sle.item_code
        WHERE
            b.expiry_date IS NOT NULL
            AND b.expiry_date <= CURDATE() + INTERVAL 30 DAY -- Expiring within 30 days or already expired
        GROUP BY
            b.name, sle.warehouse
        ORDER BY
            b.expiry_date ASC;
        """
    },
    "production_daily_log": {
        "json_content": """
        {
            "doctype": "Report",
            "name": "Production Daily Log",
            "ref_doctype": "Work Order",
            "report_type": "Script Report",
            "is_standard": "Yes",
            "module": "THTPL",
            "idx": 0,
            "json_fields": null,
            "prepared_report": 0,
            "query": null,
            "roles": [
                { "role": "Production Manager" },
                { "role": "System Manager" }
            ]
        }
        """,
        "py_content": """
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

    data = frappe.db.sql(f"""
    """, as_dict=1)
    return data
        """,
        "js_content": """
frappe.query_reports["Production Daily Log"] = {
    "filters": [
        {
            "fieldname":"from_date",
            "label": __("From Date"),
            "fieldtype": "Date",
            "reqd": 1,
            "default": frappe.datetime.add_months(frappe.datetime.get_today(), -1)
        },
        {
            "fieldname":"to_date",
            "label": __("To Date"),
            "fieldtype": "Date",
            "reqd": 1,
            "default": frappe.datetime.get_today()
        },
        {
            "fieldname":"item_code",
            "label": __("Item"),
            "fieldtype": "Link",
            "options": "Item"
        }
    ]
};
        """
    }
}


def create_dir_if_not_exists(path):
    """Creates a directory if it doesn't already exist."""
    os.makedirs(path, exist_ok=True)
    print(f"Ensured directory: {path}")

def create_file(path, content, overwrite=False):
    """Creates a file with the given content."""
    if os.path.exists(path) and not overwrite:
        print(f"Skipping existing file (overwrite=False): {path}")
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created file: {path}")

def main():
    app_root = os.path.join(BASE_PATH, APP_NAME, APP_NAME)
    
    # 1. Create main app folders
    create_dir_if_not_exists(os.path.join(app_root, "doctype"))
    create_dir_if_not_exists(os.path.join(app_root, "report"))
    create_dir_if_not_exists(os.path.join(app_root, "fixtures"))

    # 2. Create custom fields fixture file
    custom_fields_file_path = os.path.join(app_root, "fixtures", "custom_field.json")
    # Convert None to null for JSON output
    json_compatible_custom_fields = json.dumps(custom_fields_data, indent=2, ensure_ascii=False).replace('null', 'null')
    create_file(custom_fields_file_path, json_compatible_custom_fields, overwrite=True)

    # 3. Create DocType folders and JSON files
    for doctype_name, doctype_info in doctypes_to_create.items():
        snake_case_doctype_name = doctype_name.replace(" ", "_").lower()
        doctype_path = os.path.join(app_root, "doctype", snake_case_doctype_name)
        create_dir_if_not_exists(doctype_path)
        
        json_file_path = os.path.join(doctype_path, f"{snake_case_doctype_name}.json")
        # Ensure 'modified' and 'creation' dates are current
        doctype_json_content = doctype_info["json"].replace("THTPL", APP_NAME)
        doctype_dict = json.loads(doctype_json_content)
        current_time = datetime.now().isoformat(sep=' ', timespec='milliseconds')
        doctype_dict["creation"] = current_time
        doctype_dict["modified"] = current_time
        doctype_dict["module"] = APP_NAME
        create_file(json_file_path, json.dumps(doctype_dict, indent=1, ensure_ascii=False), overwrite=True)

        # Create boilerplate .py and .js files for DocType
        create_file(os.path.join(doctype_path, f"{snake_case_doctype_name}.py"),
                    f'# Copyright (c) 2025, {APP_NAME} and contributors\n# For license information, please see license.txt\n\n# import frappe\nfrom frappe.model.document import Document\n\nclass {doctype_name.replace(" ", "")}(Document):\n\tpass\n', overwrite=False)
        create_file(os.path.join(doctype_path, f"{snake_case_doctype_name}.js"),
                    f'// Copyright (c) 2025, {APP_NAME} and contributors\n// For license information, please see license.txt\n\nfrappe.ui.form.on("{doctype_name}", {{\n\trefresh: function(frm) {{\n\n\t}}\n}});', overwrite=False)

    # 4. Create Report folders and files
    for report_name, report_info in reports_to_create.items():
        report_path = os.path.join(app_root, "report", report_name)
        create_dir_if_not_exists(report_path)

        # Create report JSON
        create_file(os.path.join(report_path, f"{report_name}.json"),
                    json.dumps(json.loads(report_info["json_content"]), indent=4, ensure_ascii=False), overwrite=True)

        # Create report specific files
        if "sql_content" in report_info:
            create_file(os.path.join(report_path, f"{report_name}.sql"), report_info["sql_content"].strip(), overwrite=True)
        if "py_content" in report_info:
            create_file(os.path.join(report_path, f"{report_name}.py"), report_info["py_content"].strip(), overwrite=True)
        if "js_content" in report_info:
            create_file(os.path.join(report_path, f"{report_name}.js"), report_info["js_content"].strip(), overwrite=True)

    print("\nFrappe custom app structure and files created successfully for 'thtpl'!")
    print("Remember to run `bench migrate` and `bench clear-cache` after installing the app.")

if __name__ == "__main__":
    main()