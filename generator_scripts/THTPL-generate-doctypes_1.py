# THTPL ERPNext - Complete DocTypes Generator Script
# Location: thtpl_erp/generate_doctypes.py
# Usage: bench --site thtpl.test console < generate_doctypes.py
# Purpose: Create all 24+ custom doctypes for THTPL ASME compliance

import frappe
from frappe.model.document import Document

def create_doctype_if_not_exists(doctype_dict):
    """
    Create a new doctype if it doesn't already exist
    """
    doctype_name = doctype_dict.get("name")
    try:
        if frappe.db.exists("DocType", doctype_name):
            print(f"   ✓ {doctype_name} (already exists)")
            return False
        
        doc = frappe.new_doc("DocType")
        doc.update(doctype_dict)
        doc.insert(ignore_permissions=True)
        print(f"   ✅ {doctype_name}")
        return True
    except Exception as e:
        print(f"   ❌ {doctype_name} - Error: {str(e)}")
        return False

print("\n" + "="*100)
print("THTPL ERPNext - Complete DocTypes Generator Script")
print("="*100)

# ============================================================================
# 1. QUALITY CONTROL PLAN (THTPL/QC/QCP)
# ============================================================================

print("\n🎯 1. Quality Control Plan (THTPL/QC/QCP)")
print("-" * 100)

quality_control_plan = {
    "name": "Quality Control Plan",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "autoname": "THTPL-QC-QCP-.YYYY.-#####",
    "naming_series": "THTPL-QC-QCP-.YYYY.-#####",
    "title_field": "qcp_title",
    "document_type": "Document",
    "track_changes": 1,
    "track_views": 1,
    "fields": [
        {
            "fieldname": "qcp_title",
            "label": "Quality Control Plan Title",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "sales_order_reference",
            "label": "Sales Order Reference",
            "fieldtype": "Link",
            "options": "Sales Order",
            "reqd": 1
        },
        {
            "fieldname": "work_order_reference",
            "label": "Work Order Reference",
            "fieldtype": "Link",
            "options": "Work Order"
        },
        {
            "fieldname": "item_reference",
            "label": "Item Reference",
            "fieldtype": "Link",
            "options": "Item",
            "reqd": 1
        },
        {
            "fieldname": "customer_name",
            "label": "Customer Name",
            "fieldtype": "Data"
        },
        {
            "fieldname": "qcp_version",
            "label": "Version",
            "fieldtype": "Data",
            "default": "1.0"
        },
        {
            "fieldname": "created_date",
            "label": "Created Date",
            "fieldtype": "Date",
            "default": "Today"
        },
        {
            "fieldname": "created_by_user",
            "label": "Created By",
            "fieldtype": "Link",
            "options": "User"
        },
        {
            "fieldname": "approval_status",
            "label": "Approval Status",
            "fieldtype": "Select",
            "options": "Draft\nSubmitted\nApproved\nRejected",
            "default": "Draft"
        },
        {
            "fieldname": "approved_by",
            "label": "Approved By",
            "fieldtype": "Link",
            "options": "User"
        },
        {
            "fieldname": "approved_date",
            "label": "Approved Date",
            "fieldtype": "Date"
        },
        {
            "fieldname": "quality_checkpoints_section",
            "label": "Quality Checkpoints",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "quality_gates",
            "label": "Quality Gates",
            "fieldtype": "Table",
            "options": "QC Plan Gate"
        },
        {
            "fieldname": "testing_section",
            "label": "Testing & Inspection",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "testing_types",
            "label": "Testing Types Required",
            "fieldtype": "Table",
            "options": "QC Testing Type"
        },
        {
            "fieldname": "documentation_section",
            "label": "Documentation",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "qcp_documentation",
            "label": "QCP Documentation",
            "fieldtype": "Small Text"
        },
        {
            "fieldname": "notes",
            "label": "Notes",
            "fieldtype": "Small Text"
        }
    ],
    "permissions": [
        {
            "role": "Administrator",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "delete": 1,
            "submit": 1,
            "amend": 1
        },
        {
            "role": "Quality Manager",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "submit": 1
        }
    ]
}

create_doctype_if_not_exists(quality_control_plan)

# ============================================================================
# 2. QC PLAN GATE (Child Table)
# ============================================================================

print("\n🎯 2. QC Plan Gate (Child Table)")
print("-" * 100)

qc_plan_gate = {
    "name": "QC Plan Gate",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "istable": 1,
    "fields": [
        {
            "fieldname": "gate_sequence",
            "label": "Gate Sequence",
            "fieldtype": "Int",
            "reqd": 1
        },
        {
            "fieldname": "gate_name",
            "label": "Gate Name",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "gate_type",
            "label": "Gate Type",
            "fieldtype": "Select",
            "options": "Raw Material Inspection\nHeat Treatment\nIn-Process Inspection\nFinal Inspection\nPressure Test\nNDE Test",
            "reqd": 1
        },
        {
            "fieldname": "gate_description",
            "label": "Description",
            "fieldtype": "Text"
        },
        {
            "fieldname": "acceptance_criteria",
            "label": "Acceptance Criteria",
            "fieldtype": "Small Text"
        },
        {
            "fieldname": "responsible_department",
            "label": "Responsible Department",
            "fieldtype": "Data"
        },
        {
            "fieldname": "estimated_time_days",
            "label": "Estimated Time (Days)",
            "fieldtype": "Int"
        }
    ]
}

create_doctype_if_not_exists(qc_plan_gate)

# ============================================================================
# 3. QC TESTING TYPE (Child Table)
# ============================================================================

print("\n🎯 3. QC Testing Type (Child Table)")
print("-" * 100)

qc_testing_type = {
    "name": "QC Testing Type",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "istable": 1,
    "fields": [
        {
            "fieldname": "testing_method",
            "label": "Testing Method",
            "fieldtype": "Select",
            "options": "Visual Inspection\nDimensional Inspection\nMaterial Identification\nHeat Treatment Documentation\nLiquid Penetrant Test\nRadiography Test\nPressure Test\nWeld Inspection",
            "reqd": 1
        },
        {
            "fieldname": "standard_reference",
            "label": "Standard Reference",
            "fieldtype": "Data"
        },
        {
            "fieldname": "acceptance_criteria",
            "label": "Acceptance Criteria",
            "fieldtype": "Small Text"
        },
        {
            "fieldname": "required_samples",
            "label": "Required Samples",
            "fieldtype": "Int"
        }
    ]
}

create_doctype_if_not_exists(qc_testing_type)

# ============================================================================
# 4. MATERIAL IDENTIFICATION REPORT (THTPL/QC/MIR)
# ============================================================================

print("\n🎯 4. Material Identification Report (THTPL/QC/MIR)")
print("-" * 100)

material_id_report = {
    "name": "Material Identification Report",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "autoname": "THTPL-QC-MIR-.YYYY.-#####",
    "naming_series": "THTPL-QC-MIR-.YYYY.-#####",
    "title_field": "mir_title",
    "document_type": "Document",
    "track_changes": 1,
    "fields": [
        {
            "fieldname": "mir_title",
            "label": "Material ID Report Title",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "purchase_order_ref",
            "label": "Purchase Order Reference",
            "fieldtype": "Link",
            "options": "Purchase Order"
        },
        {
            "fieldname": "purchase_receipt_ref",
            "label": "Purchase Receipt Reference",
            "fieldtype": "Link",
            "options": "Purchase Receipt"
        },
        {
            "fieldname": "supplier_name",
            "label": "Supplier Name",
            "fieldtype": "Link",
            "options": "Supplier"
        },
        {
            "fieldname": "material_received_date",
            "label": "Material Received Date",
            "fieldtype": "Date"
        },
        {
            "fieldname": "inspection_date",
            "label": "Inspection Date",
            "fieldtype": "Date",
            "reqd": 1
        },
        {
            "fieldname": "inspector_name",
            "label": "Inspector Name",
            "fieldtype": "Link",
            "options": "Employee",
            "reqd": 1
        },
        {
            "fieldname": "material_section",
            "label": "Material Details",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "material_type",
            "label": "Material Type",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "material_grade",
            "label": "Material Grade",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "material_specification",
            "label": "Material Specification",
            "fieldtype": "Link",
            "options": "Material Specification Master"
        },
        {
            "fieldname": "quantity_received",
            "label": "Quantity Received",
            "fieldtype": "Float"
        },
        {
            "fieldname": "unit_of_measurement",
            "label": "Unit of Measurement",
            "fieldtype": "Data"
        },
        {
            "fieldname": "batch_number",
            "label": "Batch Number",
            "fieldtype": "Data"
        },
        {
            "fieldname": "manufacturing_date",
            "label": "Manufacturing Date",
            "fieldtype": "Date"
        },
        {
            "fieldname": "expiry_date",
            "label": "Expiry Date",
            "fieldtype": "Date"
        },
        {
            "fieldname": "test_method",
            "label": "Test Method Used",
            "fieldtype": "Select",
            "options": "PMI - Positive Material Identification\nChemical Analysis\nMechanical Testing\nSpectrometry",
            "reqd": 1
        },
        {
            "fieldname": "identification_details",
            "label": "Identification Details",
            "fieldtype": "Table",
            "options": "Material ID Detail"
        },
        {
            "fieldname": "results_section",
            "label": "Results",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "result",
            "label": "Result",
            "fieldtype": "Select",
            "options": "Pass\nFail",
            "reqd": 1
        },
        {
            "fieldname": "conclusion",
            "label": "Conclusion",
            "fieldtype": "Small Text"
        },
        {
            "fieldname": "approval_section",
            "label": "Approval",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "mir_status",
            "label": "Status",
            "fieldtype": "Select",
            "options": "Draft\nSubmitted\nApproved\nRejected",
            "default": "Draft"
        },
        {
            "fieldname": "approved_by",
            "label": "Approved By",
            "fieldtype": "Link",
            "options": "User"
        },
        {
            "fieldname": "approved_date",
            "label": "Approved Date",
            "fieldtype": "Date"
        },
        {
            "fieldname": "notes",
            "label": "Notes",
            "fieldtype": "Small Text"
        }
    ],
    "permissions": [
        {
            "role": "Administrator",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "delete": 1,
            "submit": 1
        },
        {
            "role": "Quality Manager",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "submit": 1
        }
    ]
}

create_doctype_if_not_exists(material_id_report)

# ============================================================================
# 5. MATERIAL ID DETAIL (Child Table)
# ============================================================================

print("\n🎯 5. Material ID Detail (Child Table)")
print("-" * 100)

material_id_detail = {
    "name": "Material ID Detail",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "istable": 1,
    "fields": [
        {
            "fieldname": "element_name",
            "label": "Element Name",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "expected_value",
            "label": "Expected Value",
            "fieldtype": "Data"
        },
        {
            "fieldname": "measured_value",
            "label": "Measured Value",
            "fieldtype": "Data"
        },
        {
            "fieldname": "percentage",
            "label": "Percentage",
            "fieldtype": "Float"
        },
        {
            "fieldname": "status",
            "label": "Status",
            "fieldtype": "Select",
            "options": "OK\nNOK"
        }
    ]
}

create_doctype_if_not_exists(material_id_detail)

# ============================================================================
# 6. HEAT TREATMENT REPORT (THTPL/QC/HTR)
# ============================================================================

print("\n🎯 6. Heat Treatment Report (THTPL/QC/HTR)")
print("-" * 100)

heat_treatment_report = {
    "name": "Heat Treatment Report",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "autoname": "THTPL-QC-HTR-.YYYY.-#####",
    "naming_series": "THTPL-QC-HTR-.YYYY.-#####",
    "title_field": "htr_title",
    "document_type": "Document",
    "track_changes": 1,
    "fields": [
        {
            "fieldname": "htr_title",
            "label": "Heat Treatment Report Title",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "work_order_ref",
            "label": "Work Order Reference",
            "fieldtype": "Link",
            "options": "Work Order",
            "reqd": 1
        },
        {
            "fieldname": "treatment_date",
            "label": "Treatment Date",
            "fieldtype": "Date",
            "reqd": 1
        },
        {
            "fieldname": "treatment_type",
            "label": "Treatment Type",
            "fieldtype": "Select",
            "options": "Stress Relief\nNormalization\nAnneal\nQuenching\nHardening\nAge Hardening",
            "reqd": 1
        },
        {
            "fieldname": "furnace_name",
            "label": "Furnace Name",
            "fieldtype": "Data"
        },
        {
            "fieldname": "furnace_id",
            "label": "Furnace ID",
            "fieldtype": "Data"
        },
        {
            "fieldname": "temperature_section",
            "label": "Temperature Details",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "preheat_temperature",
            "label": "Preheat Temperature (°C)",
            "fieldtype": "Float"
        },
        {
            "fieldname": "holding_temperature",
            "label": "Holding Temperature (°C)",
            "fieldtype": "Float",
            "reqd": 1
        },
        {
            "fieldname": "holding_time_hours",
            "label": "Holding Time (Hours)",
            "fieldtype": "Float",
            "reqd": 1
        },
        {
            "fieldname": "cooling_method",
            "label": "Cooling Method",
            "fieldtype": "Select",
            "options": "Furnace Cool\nAir Cool\nWater Quench\nOil Quench"
        },
        {
            "fieldname": "cooling_temperature",
            "label": "Cooling End Temperature (°C)",
            "fieldtype": "Float"
        },
        {
            "fieldname": "hardness_section",
            "label": "Hardness Testing",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "hardness_test_required",
            "label": "Hardness Test Required",
            "fieldtype": "Check"
        },
        {
            "fieldname": "hardness_value",
            "label": "Hardness Value (HV/HRC)",
            "fieldtype": "Data"
        },
        {
            "fieldname": "approval_section",
            "label": "Approval",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "htr_status",
            "label": "Status",
            "fieldtype": "Select",
            "options": "Draft\nSubmitted\nApproved\nRejected",
            "default": "Draft"
        },
        {
            "fieldname": "approved_by",
            "label": "Approved By",
            "fieldtype": "Link",
            "options": "User"
        },
        {
            "fieldname": "notes",
            "label": "Notes",
            "fieldtype": "Small Text"
        }
    ],
    "permissions": [
        {
            "role": "Administrator",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "delete": 1,
            "submit": 1
        },
        {
            "role": "Quality Manager",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "submit": 1
        }
    ]
}

create_doctype_if_not_exists(heat_treatment_report)

# ============================================================================
# 7. STAGE INSPECTION REPORT (THTPL/QC/STI)
# ============================================================================

print("\n🎯 7. Stage Inspection Report (THTPL/QC/STI)")
print("-" * 100)

stage_inspection_report = {
    "name": "Stage Inspection Report",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "autoname": "THTPL-QC-STI-.YYYY.-#####",
    "naming_series": "THTPL-QC-STI-.YYYY.-#####",
    "title_field": "sir_title",
    "document_type": "Document",
    "track_changes": 1,
    "fields": [
        {
            "fieldname": "sir_title",
            "label": "Stage Inspection Report Title",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "work_order_ref",
            "label": "Work Order Reference",
            "fieldtype": "Link",
            "options": "Work Order",
            "reqd": 1
        },
        {
            "fieldname": "inspection_stage",
            "label": "Inspection Stage",
            "fieldtype": "Select",
            "options": "Pre-Assembly\nDuring Assembly\nPost Assembly\nBefore Pressure Test\nBefore Painting",
            "reqd": 1
        },
        {
            "fieldname": "inspection_date",
            "label": "Inspection Date",
            "fieldtype": "Date",
            "reqd": 1
        },
        {
            "fieldname": "inspector_name",
            "label": "Inspector Name",
            "fieldtype": "Link",
            "options": "Employee",
            "reqd": 1
        },
        {
            "fieldname": "inspection_findings",
            "label": "Inspection Findings",
            "fieldtype": "Table",
            "options": "Inspection Finding"
        },
        {
            "fieldname": "defects_section",
            "label": "Defects",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "defects_found",
            "label": "Defects Found",
            "fieldtype": "Check"
        },
        {
            "fieldname": "defect_details",
            "label": "Defect Details",
            "fieldtype": "Table",
            "options": "Inspection Defect"
        },
        {
            "fieldname": "corrective_action_required",
            "label": "Corrective Action Required",
            "fieldtype": "Check"
        },
        {
            "fieldname": "corrective_action_details",
            "label": "Corrective Action Details",
            "fieldtype": "Small Text"
        },
        {
            "fieldname": "result_section",
            "label": "Result",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "result",
            "label": "Result",
            "fieldtype": "Select",
            "options": "Pass\nFail\nConditional Pass",
            "reqd": 1
        },
        {
            "fieldname": "approval_section",
            "label": "Approval",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "sir_status",
            "label": "Status",
            "fieldtype": "Select",
            "options": "Draft\nSubmitted\nApproved",
            "default": "Draft"
        },
        {
            "fieldname": "approved_by",
            "label": "Approved By",
            "fieldtype": "Link",
            "options": "User"
        },
        {
            "fieldname": "notes",
            "label": "Notes",
            "fieldtype": "Small Text"
        }
    ],
    "permissions": [
        {
            "role": "Administrator",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "delete": 1,
            "submit": 1
        },
        {
            "role": "Quality Manager",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "submit": 1
        }
    ]
}

create_doctype_if_not_exists(stage_inspection_report)

# ============================================================================
# 8. INSPECTION FINDING (Child Table)
# ============================================================================

print("\n🎯 8. Inspection Finding (Child Table)")
print("-" * 100)

inspection_finding = {
    "name": "Inspection Finding",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "istable": 1,
    "fields": [
        {
            "fieldname": "finding_category",
            "label": "Finding Category",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "finding_detail",
            "label": "Finding Detail",
            "fieldtype": "Text"
        },
        {
            "fieldname": "status",
            "label": "Status",
            "fieldtype": "Select",
            "options": "OK\nNOK"
        }
    ]
}

create_doctype_if_not_exists(inspection_finding)

# ============================================================================
# 9. INSPECTION DEFECT (Child Table)
# ============================================================================

print("\n🎯 9. Inspection Defect (Child Table)")
print("-" * 100)

inspection_defect = {
    "name": "Inspection Defect",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "istable": 1,
    "fields": [
        {
            "fieldname": "defect_type",
            "label": "Defect Type",
            "fieldtype": "Select",
            "options": "Surface\nDimensional\nWeld\nStructural",
            "reqd": 1
        },
        {
            "fieldname": "defect_description",
            "label": "Defect Description",
            "fieldtype": "Text",
            "reqd": 1
        },
        {
            "fieldname": "location",
            "label": "Location",
            "fieldtype": "Data"
        },
        {
            "fieldname": "severity",
            "label": "Severity",
            "fieldtype": "Select",
            "options": "Minor\nMajor\nCritical"
        }
    ]
}

create_doctype_if_not_exists(inspection_defect)

# ============================================================================
# 10. LIQUID PENETRANT TEST REPORT (THTPL/QC/LPT)
# ============================================================================

print("\n🎯 10. Liquid Penetrant Test Report (THTPL/QC/LPT)")
print("-" * 100)

lpt_report = {
    "name": "Liquid Penetrant Test Report",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "autoname": "THTPL-QC-LPT-.YYYY.-#####",
    "naming_series": "THTPL-QC-LPT-.YYYY.-#####",
    "title_field": "lpt_title",
    "document_type": "Document",
    "track_changes": 1,
    "fields": [
        {
            "fieldname": "lpt_title",
            "label": "LPT Report Title",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "work_order_ref",
            "label": "Work Order Reference",
            "fieldtype": "Link",
            "options": "Work Order",
            "reqd": 1
        },
        {
            "fieldname": "test_date",
            "label": "Test Date",
            "fieldtype": "Date",
            "reqd": 1
        },
        {
            "fieldname": "technician_name",
            "label": "Technician Name",
            "fieldtype": "Link",
            "options": "Employee",
            "reqd": 1
        },
        {
            "fieldname": "test_area",
            "label": "Test Area/Component",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "test_standard",
            "label": "Test Standard",
            "fieldtype": "Select",
            "options": "ASTM E1444\nISO 3452",
            "default": "ASTM E1444"
        },
        {
            "fieldname": "surface_condition",
            "label": "Surface Condition",
            "fieldtype": "Select",
            "options": "Clean\nGritty\nRusted",
            "reqd": 1
        },
        {
            "fieldname": "surface_preparation",
            "label": "Surface Preparation Method",
            "fieldtype": "Data"
        },
        {
            "fieldname": "penetrant_used",
            "label": "Penetrant Used",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "developer_used",
            "label": "Developer Used",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "test_results",
            "label": "Test Results",
            "fieldtype": "Table",
            "options": "LPT Result Detail"
        },
        {
            "fieldname": "findings_section",
            "label": "Findings",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "indications_found",
            "label": "Indications Found",
            "fieldtype": "Check"
        },
        {
            "fieldname": "indication_details",
            "label": "Indication Details",
            "fieldtype": "Small Text"
        },
        {
            "fieldname": "result_section",
            "label": "Result",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "lpt_result",
            "label": "Result",
            "fieldtype": "Select",
            "options": "Accept\nReject\nConditional",
            "reqd": 1
        },
        {
            "fieldname": "approval_section",
            "label": "Approval",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "lpt_status",
            "label": "Status",
            "fieldtype": "Select",
            "options": "Draft\nSubmitted\nApproved",
            "default": "Draft"
        },
        {
            "fieldname": "approved_by",
            "label": "Approved By",
            "fieldtype": "Link",
            "options": "User"
        },
        {
            "fieldname": "notes",
            "label": "Notes",
            "fieldtype": "Small Text"
        }
    ],
    "permissions": [
        {
            "role": "Administrator",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "delete": 1,
            "submit": 1
        },
        {
            "role": "Quality Manager",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "submit": 1
        }
    ]
}

create_doctype_if_not_exists(lpt_report)

# ============================================================================
# 11. LPT RESULT DETAIL (Child Table)
# ============================================================================

print("\n🎯 11. LPT Result Detail (Child Table)")
print("-" * 100)

lpt_result_detail = {
    "name": "LPT Result Detail",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "istable": 1,
    "fields": [
        {
            "fieldname": "location",
            "label": "Location",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "indication_type",
            "label": "Indication Type",
            "fieldtype": "Select",
            "options": "None\nLinear\nRounded\nOther"
        },
        {
            "fieldname": "size_length",
            "label": "Size/Length (mm)",
            "fieldtype": "Float"
        },
        {
            "fieldname": "acceptance",
            "label": "Acceptance",
            "fieldtype": "Select",
            "options": "Accept\nReject"
        }
    ]
}

create_doctype_if_not_exists(lpt_result_detail)

# ============================================================================
# 12. RADIOGRAPHY REPORT (THTPL/QC/RTR)
# ============================================================================

print("\n🎯 12. Radiography Report (THTPL/QC/RTR)")
print("-" * 100)

radiography_report = {
    "name": "Radiography Report",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "autoname": "THTPL-QC-RTR-.YYYY.-#####",
    "naming_series": "THTPL-QC-RTR-.YYYY.-#####",
    "title_field": "rtr_title",
    "document_type": "Document",
    "track_changes": 1,
    "fields": [
        {
            "fieldname": "rtr_title",
            "label": "Radiography Report Title",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "work_order_ref",
            "label": "Work Order Reference",
            "fieldtype": "Link",
            "options": "Work Order",
            "reqd": 1
        },
        {
            "fieldname": "test_date",
            "label": "Test Date",
            "fieldtype": "Date",
            "reqd": 1
        },
        {
            "fieldname": "technician_name",
            "label": "Technician Name",
            "fieldtype": "Link",
            "options": "Employee",
            "reqd": 1
        },
        {
            "fieldname": "test_area",
            "label": "Test Area/Component",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "test_standard",
            "label": "Test Standard",
            "fieldtype": "Select",
            "options": "ASTM E94\nISO 11699",
            "default": "ASTM E94"
        },
        {
            "fieldname": "radiation_source",
            "label": "Radiation Source",
            "fieldtype": "Select",
            "options": "X-Ray\nGamma Ray",
            "reqd": 1
        },
        {
            "fieldname": "voltage_kv",
            "label": "Voltage (kV)",
            "fieldtype": "Float"
        },
        {
            "fieldname": "exposure_time",
            "label": "Exposure Time (minutes)",
            "fieldtype": "Float"
        },
        {
            "fieldname": "film_type",
            "label": "Film Type",
            "fieldtype": "Data"
        },
        {
            "fieldname": "radiography_results",
            "label": "Radiography Results",
            "fieldtype": "Table",
            "options": "Radiography Result Detail"
        },
        {
            "fieldname": "findings_section",
            "label": "Findings",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "defects_identified",
            "label": "Defects Identified",
            "fieldtype": "Check"
        },
        {
            "fieldname": "defect_description",
            "label": "Defect Description",
            "fieldtype": "Small Text"
        },
        {
            "fieldname": "result_section",
            "label": "Result",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "rtr_result",
            "label": "Result",
            "fieldtype": "Select",
            "options": "Accept\nReject\nConditional",
            "reqd": 1
        },
        {
            "fieldname": "approval_section",
            "label": "Approval",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "rtr_status",
            "label": "Status",
            "fieldtype": "Select",
            "options": "Draft\nSubmitted\nApproved",
            "default": "Draft"
        },
        {
            "fieldname": "approved_by",
            "label": "Approved By",
            "fieldtype": "Link",
            "options": "User"
        },
        {
            "fieldname": "notes",
            "label": "Notes",
            "fieldtype": "Small Text"
        }
    ],
    "permissions": [
        {
            "role": "Administrator",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "delete": 1,
            "submit": 1
        },
        {
            "role": "Quality Manager",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "submit": 1
        }
    ]
}

create_doctype_if_not_exists(radiography_report)

# ============================================================================
# 13. RADIOGRAPHY RESULT DETAIL (Child Table)
# ============================================================================

print("\n🎯 13. Radiography Result Detail (Child Table)")
print("-" * 100)

radiography_result_detail = {
    "name": "Radiography Result Detail",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "istable": 1,
    "fields": [
        {
            "fieldname": "location",
            "label": "Location",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "defect_type",
            "label": "Defect Type",
            "fieldtype": "Select",
            "options": "None\nPorosity\nInclusion\nCrack\nLamination\nOther"
        },
        {
            "fieldname": "size_mm",
            "label": "Size (mm)",
            "fieldtype": "Float"
        },
        {
            "fieldname": "acceptance",
            "label": "Acceptance",
            "fieldtype": "Select",
            "options": "Accept\nReject"
        }
    ]
}

create_doctype_if_not_exists(radiography_result_detail)

# ============================================================================
# 14. PRESSURE TEST REPORT (THTPL/QC/PTR)
# ============================================================================

print("\n🎯 14. Pressure Test Report (THTPL/QC/PTR)")
print("-" * 100)

pressure_test_report = {
    "name": "Pressure Test Report",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "autoname": "THTPL-QC-PTR-.YYYY.-#####",
    "naming_series": "THTPL-QC-PTR-.YYYY.-#####",
    "title_field": "ptr_title",
    "document_type": "Document",
    "track_changes": 1,
    "fields": [
        {
            "fieldname": "ptr_title",
            "label": "Pressure Test Report Title",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "work_order_ref",
            "label": "Work Order Reference",
            "fieldtype": "Link",
            "options": "Work Order",
            "reqd": 1
        },
        {
            "fieldname": "test_date",
            "label": "Test Date",
            "fieldtype": "Date",
            "reqd": 1
        },
        {
            "fieldname": "test_type",
            "label": "Test Type",
            "fieldtype": "Select",
            "options": "Hydrostatic Test\nPneumatic Test\nCombined Test",
            "reqd": 1
        },
        {
            "fieldname": "test_standard",
            "label": "Test Standard",
            "fieldtype": "Select",
            "options": "ASME Section VIII\nASTM E52",
            "default": "ASME Section VIII"
        },
        {
            "fieldname": "design_pressure_bar",
            "label": "Design Pressure (bar)",
            "fieldtype": "Float",
            "reqd": 1
        },
        {
            "fieldname": "test_pressure_bar",
            "label": "Test Pressure (bar)",
            "fieldtype": "Float",
            "reqd": 1
        },
        {
            "fieldname": "test_medium",
            "label": "Test Medium",
            "fieldtype": "Select",
            "options": "Water\nAir\nOther",
            "reqd": 1
        },
        {
            "fieldname": "test_duration_hours",
            "label": "Test Duration (Hours)",
            "fieldtype": "Float"
        },
        {
            "fieldname": "holding_section",
            "label": "Pressure Holding",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "initial_pressure_bar",
            "label": "Initial Pressure (bar)",
            "fieldtype": "Float"
        },
        {
            "fieldname": "final_pressure_bar",
            "label": "Final Pressure (bar)",
            "fieldtype": "Float"
        },
        {
            "fieldname": "pressure_drop_bar",
            "label": "Pressure Drop (bar)",
            "fieldtype": "Float",
            "read_only": 1
        },
        {
            "fieldname": "observations",
            "label": "Observations",
            "fieldtype": "Table",
            "options": "Test Observation"
        },
        {
            "fieldname": "result_section",
            "label": "Result",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "leakage_found",
            "label": "Leakage Found",
            "fieldtype": "Check"
        },
        {
            "fieldname": "leakage_details",
            "label": "Leakage Details",
            "fieldtype": "Small Text"
        },
        {
            "fieldname": "ptr_result",
            "label": "Result",
            "fieldtype": "Select",
            "options": "Pass\nFail",
            "reqd": 1
        },
        {
            "fieldname": "approval_section",
            "label": "Approval",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "ptr_status",
            "label": "Status",
            "fieldtype": "Select",
            "options": "Draft\nSubmitted\nApproved",
            "default": "Draft"
        },
        {
            "fieldname": "tested_by",
            "label": "Tested By",
            "fieldtype": "Link",
            "options": "Employee",
            "reqd": 1
        },
        {
            "fieldname": "approved_by",
            "label": "Approved By",
            "fieldtype": "Link",
            "options": "User"
        },
        {
            "fieldname": "notes",
            "label": "Notes",
            "fieldtype": "Small Text"
        }
    ],
    "permissions": [
        {
            "role": "Administrator",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "delete": 1,
            "submit": 1
        },
        {
            "role": "Quality Manager",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "submit": 1
        }
    ]
}

create_doctype_if_not_exists(pressure_test_report)

# ============================================================================
# 15. TEST OBSERVATION (Child Table)
# ============================================================================

print("\n🎯 15. Test Observation (Child Table)")
print("-" * 100)

test_observation = {
    "name": "Test Observation",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "istable": 1,
    "fields": [
        {
            "fieldname": "time_minutes",
            "label": "Time (Minutes)",
            "fieldtype": "Int"
        },
        {
            "fieldname": "pressure_bar",
            "label": "Pressure (bar)",
            "fieldtype": "Float"
        },
        {
            "fieldname": "observation",
            "label": "Observation",
            "fieldtype": "Text"
        }
    ]
}

create_doctype_if_not_exists(test_observation)

# ============================================================================
# 16. WELD SUMMARY (THTPL/QC/WEL)
# ============================================================================

print("\n🎯 16. Weld Summary (THTPL/QC/WEL)")
print("-" * 100)

weld_summary = {
    "name": "Weld Summary",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "autoname": "THTPL-QC-WEL-.YYYY.-#####",
    "naming_series": "THTPL-QC-WEL-.YYYY.-#####",
    "title_field": "weld_summary_title",
    "document_type": "Document",
    "track_changes": 1,
    "fields": [
        {
            "fieldname": "weld_summary_title",
            "label": "Weld Summary Title",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "work_order_ref",
            "label": "Work Order Reference",
            "fieldtype": "Link",
            "options": "Work Order",
            "reqd": 1
        },
        {
            "fieldname": "weld_date",
            "label": "Weld Date",
            "fieldtype": "Date",
            "reqd": 1
        },
        {
            "fieldname": "welding_section",
            "label": "Welding Details",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "total_weld_length_mm",
            "label": "Total Weld Length (mm)",
            "fieldtype": "Float"
        },
        {
            "fieldname": "weld_passes",
            "label": "Weld Passes",
            "fieldtype": "Int"
        },
        {
            "fieldname": "welding_process",
            "label": "Welding Process",
            "fieldtype": "Select",
            "options": "SMAW\nGMAW\nFCAW\nSAW\nGTAW"
        },
        {
            "fieldname": "welders_used",
            "label": "Welders Used",
            "fieldtype": "Table",
            "options": "Welder Used"
        },
        {
            "fieldname": "welding_parameters",
            "label": "Welding Parameters",
            "fieldtype": "Table",
            "options": "Welding Parameter"
        },
        {
            "fieldname": "inspection_section",
            "label": "Inspection",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "visual_inspection_result",
            "label": "Visual Inspection Result",
            "fieldtype": "Select",
            "options": "Pass\nFail"
        },
        {
            "fieldname": "lpt_test_required",
            "label": "LPT Test Required",
            "fieldtype": "Check"
        },
        {
            "fieldname": "lpt_report_ref",
            "label": "LPT Report Reference",
            "fieldtype": "Link",
            "options": "Liquid Penetrant Test Report"
        },
        {
            "fieldname": "radiography_required",
            "label": "Radiography Required",
            "fieldtype": "Check"
        },
        {
            "fieldname": "radiography_report_ref",
            "label": "Radiography Report Reference",
            "fieldtype": "Link",
            "options": "Radiography Report"
        },
        {
            "fieldname": "approval_section",
            "label": "Approval",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "weld_status",
            "label": "Status",
            "fieldtype": "Select",
            "options": "Draft\nSubmitted\nApproved",
            "default": "Draft"
        },
        {
            "fieldname": "approved_by",
            "label": "Approved By",
            "fieldtype": "Link",
            "options": "User"
        },
        {
            "fieldname": "notes",
            "label": "Notes",
            "fieldtype": "Small Text"
        }
    ],
    "permissions": [
        {
            "role": "Administrator",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "delete": 1,
            "submit": 1
        },
        {
            "role": "Quality Manager",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "submit": 1
        }
    ]
}

create_doctype_if_not_exists(weld_summary)

# ============================================================================
# 17. WELDER USED (Child Table)
# ============================================================================

print("\n🎯 17. Welder Used (Child Table)")
print("-" * 100)

welder_used = {
    "name": "Welder Used",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "istable": 1,
    "fields": [
        {
            "fieldname": "welder_id",
            "label": "Welder ID",
            "fieldtype": "Link",
            "options": "Employee"
        },
        {
            "fieldname": "welder_name",
            "label": "Welder Name",
            "fieldtype": "Data"
        },
        {
            "fieldname": "certification_status",
            "label": "Certification Status",
            "fieldtype": "Select",
            "options": "Qualified\nNot Qualified"
        }
    ]
}

create_doctype_if_not_exists(welder_used)

# ============================================================================
# 18. WELDING PARAMETER (Child Table)
# ============================================================================

print("\n🎯 18. Welding Parameter (Child Table)")
print("-" * 100)

welding_parameter = {
    "name": "Welding Parameter",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "istable": 1,
    "fields": [
        {
            "fieldname": "pass_number",
            "label": "Pass Number",
            "fieldtype": "Int"
        },
        {
            "fieldname": "current_amp",
            "label": "Current (Amp)",
            "fieldtype": "Float"
        },
        {
            "fieldname": "voltage_v",
            "label": "Voltage (V)",
            "fieldtype": "Float"
        },
        {
            "fieldname": "rod_diameter_mm",
            "label": "Rod Diameter (mm)",
            "fieldtype": "Float"
        },
        {
            "fieldname": "travel_speed",
            "label": "Travel Speed (mm/min)",
            "fieldtype": "Float"
        }
    ]
}

create_doctype_if_not_exists(welding_parameter)

# ============================================================================
# 19. PAINTING INSPECTION REPORT (THTPL/QC/PSF)
# ============================================================================

print("\n🎯 19. Painting Inspection Report (THTPL/QC/PSF)")
print("-" * 100)

painting_inspection_report = {
    "name": "Painting Inspection Report",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "autoname": "THTPL-QC-PSF-.YYYY.-#####",
    "naming_series": "THTPL-QC-PSF-.YYYY.-#####",
    "title_field": "pir_title",
    "document_type": "Document",
    "track_changes": 1,
    "fields": [
        {
            "fieldname": "pir_title",
            "label": "Painting Inspection Report Title",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "work_order_ref",
            "label": "Work Order Reference",
            "fieldtype": "Link",
            "options": "Work Order",
            "reqd": 1
        },
        {
            "fieldname": "inspection_date",
            "label": "Inspection Date",
            "fieldtype": "Date",
            "reqd": 1
        },
        {
            "fieldname": "surface_preparation_section",
            "label": "Surface Preparation",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "surface_prep_method",
            "label": "Surface Preparation Method",
            "fieldtype": "Select",
            "options": "Blasting\nChemical\nMechanical",
            "reqd": 1
        },
        {
            "fieldname": "surface_cleanliness",
            "label": "Surface Cleanliness Standard",
            "fieldtype": "Select",
            "options": "Sa 1\nSa 2\nSa 2.5\nSa 3"
        },
        {
            "fieldname": "coating_section",
            "label": "Coating Details",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "primer_type",
            "label": "Primer Type",
            "fieldtype": "Data"
        },
        {
            "fieldname": "primer_thickness_microns",
            "label": "Primer Thickness (Microns)",
            "fieldtype": "Float"
        },
        {
            "fieldname": "topcoat_type",
            "label": "Topcoat Type",
            "fieldtype": "Data"
        },
        {
            "fieldname": "topcoat_thickness_microns",
            "label": "Topcoat Thickness (Microns)",
            "fieldtype": "Float"
        },
        {
            "fieldname": "total_coating_thickness_microns",
            "label": "Total Coating Thickness (Microns)",
            "fieldtype": "Float",
            "read_only": 1
        },
        {
            "fieldname": "inspection_section",
            "label": "Inspection Results",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "visual_inspection",
            "label": "Visual Inspection Result",
            "fieldtype": "Select",
            "options": "Pass\nFail"
        },
        {
            "fieldname": "defects_found",
            "label": "Defects Found",
            "fieldtype": "Check"
        },
        {
            "fieldname": "defect_details",
            "label": "Defect Details",
            "fieldtype": "Small Text"
        },
        {
            "fieldname": "adhesion_test",
            "label": "Adhesion Test Required",
            "fieldtype": "Check"
        },
        {
            "fieldname": "adhesion_test_result",
            "label": "Adhesion Test Result",
            "fieldtype": "Select",
            "options": "Pass\nFail"
        },
        {
            "fieldname": "result_section",
            "label": "Result",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "pir_result",
            "label": "Result",
            "fieldtype": "Select",
            "options": "Pass\nFail",
            "reqd": 1
        },
        {
            "fieldname": "approval_section",
            "label": "Approval",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "pir_status",
            "label": "Status",
            "fieldtype": "Select",
            "options": "Draft\nSubmitted\nApproved",
            "default": "Draft"
        },
        {
            "fieldname": "approved_by",
            "label": "Approved By",
            "fieldtype": "Link",
            "options": "User"
        },
        {
            "fieldname": "notes",
            "label": "Notes",
            "fieldtype": "Small Text"
        }
    ],
    "permissions": [
        {
            "role": "Administrator",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "delete": 1,
            "submit": 1
        },
        {
            "role": "Quality Manager",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "submit": 1
        }
    ]
}

create_doctype_if_not_exists(painting_inspection_report)

# ============================================================================
# 20. INSTRUMENT CALIBRATION LIST (THTPL/QC/ICL)
# ============================================================================

print("\n🎯 20. Instrument Calibration List (THTPL/QC/ICL)")
print("-" * 100)

instrument_calibration_list = {
    "name": "Instrument Calibration List",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "autoname": "THTPL-QC-ICL-.YYYY.-#####",
    "naming_series": "THTPL-QC-ICL-.YYYY.-#####",
    "title_field": "icl_title",
    "document_type": "Document",
    "track_changes": 1,
    "fields": [
        {
            "fieldname": "icl_title",
            "label": "Instrument Calibration List Title",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "effective_date",
            "label": "Effective Date",
            "fieldtype": "Date",
            "default": "Today"
        },
        {
            "fieldname": "valid_till_date",
            "label": "Valid Till Date",
            "fieldtype": "Date"
        },
        {
            "fieldname": "review_section",
            "label": "Review",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "reviewed_by",
            "label": "Reviewed By",
            "fieldtype": "Link",
            "options": "User"
        },
        {
            "fieldname": "review_date",
            "label": "Review Date",
            "fieldtype": "Date"
        },
        {
            "fieldname": "instruments_section",
            "label": "Instruments",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "instrument_details",
            "label": "Instrument Details",
            "fieldtype": "Table",
            "options": "Calibration Instrument"
        },
        {
            "fieldname": "icl_status",
            "label": "Status",
            "fieldtype": "Select",
            "options": "Draft\nSubmitted\nApproved",
            "default": "Draft"
        },
        {
            "fieldname": "notes",
            "label": "Notes",
            "fieldtype": "Small Text"
        }
    ],
    "permissions": [
        {
            "role": "Administrator",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "delete": 1,
            "submit": 1
        }
    ]
}

create_doctype_if_not_exists(instrument_calibration_list)

# ============================================================================
# 21. CALIBRATION INSTRUMENT (Child Table)
# ============================================================================

print("\n🎯 21. Calibration Instrument (Child Table)")
print("-" * 100)

calibration_instrument = {
    "name": "Calibration Instrument",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "istable": 1,
    "fields": [
        {
            "fieldname": "instrument_name",
            "label": "Instrument Name",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "instrument_id",
            "label": "Instrument ID",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "asset_link",
            "label": "Asset Link",
            "fieldtype": "Link",
            "options": "Asset"
        },
        {
            "fieldname": "last_calibration_date",
            "label": "Last Calibration Date",
            "fieldtype": "Date"
        },
        {
            "fieldname": "next_calibration_due",
            "label": "Next Calibration Due",
            "fieldtype": "Date"
        },
        {
            "fieldname": "calibration_status",
            "label": "Calibration Status",
            "fieldtype": "Select",
            "options": "Current\nDue\nOverdue"
        },
        {
            "fieldname": "calibration_agency",
            "label": "Calibration Agency",
            "fieldtype": "Data"
        }
    ]
}

create_doctype_if_not_exists(calibration_instrument)

# ============================================================================
# 22. OUT OF CALIBRATION FORM (THTPL/QC/OOC)
# ============================================================================

print("\n🎯 22. Out of Calibration Form (THTPL/QC/OOC)")
print("-" * 100)

out_of_calibration_form = {
    "name": "Out of Calibration Form",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "autoname": "THTPL-QC-OOC-.YYYY.-#####",
    "naming_series": "THTPL-QC-OOC-.YYYY.-#####",
    "title_field": "ooc_title",
    "document_type": "Document",
    "track_changes": 1,
    "fields": [
        {
            "fieldname": "ooc_title",
            "label": "Out of Calibration Form Title",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "instrument_section",
            "label": "Instrument Details",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "instrument_name",
            "label": "Instrument Name",
            "fieldtype": "Data",
            "reqd": 1
        },
        {
            "fieldname": "instrument_id",
            "fieldtype": "Data",
            "label": "Instrument ID",
            "reqd": 1
        },
        {
            "fieldname": "asset_link_ooc",
            "label": "Asset Link",
            "fieldtype": "Link",
            "options": "Asset"
        },
        {
            "fieldname": "last_calibration_date",
            "label": "Last Calibration Date",
            "fieldtype": "Date"
        },
        {
            "fieldname": "due_calibration_date",
            "label": "Due Calibration Date",
            "fieldtype": "Date"
        },
        {
            "fieldname": "issue_section",
            "label": "Issue Details",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "identified_date",
            "label": "Date Identified",
            "fieldtype": "Date",
            "reqd": 1
        },
        {
            "fieldname": "identified_by",
            "label": "Identified By",
            "fieldtype": "Link",
            "options": "Employee",
            "reqd": 1
        },
        {
            "fieldname": "reason_for_ooc",
            "label": "Reason for Out of Calibration",
            "fieldtype": "Small Text",
            "reqd": 1
        },
        {
            "fieldname": "work_orders_affected",
            "label": "Work Orders Affected",
            "fieldtype": "Table",
            "options": "Affected Work Order"
        },
        {
            "fieldname": "actions_section",
            "label": "Actions Taken",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "action_taken",
            "label": "Action Taken",
            "fieldtype": "Select",
            "options": "Suspended from Use\nRe-evaluated\nCalibrated",
            "reqd": 1
        },
        {
            "fieldname": "impact_assessment",
            "label": "Impact Assessment",
            "fieldtype": "Small Text"
        },
        {
            "fieldname": "approval_section",
            "label": "Approval",
            "fieldtype": "Section Break"
        },
        {
            "fieldname": "ooc_status",
            "label": "Status",
            "fieldtype": "Select",
            "options": "Draft\nSubmitted\nApproved\nClosed",
            "default": "Draft"
        },
        {
            "fieldname": "approved_by",
            "label": "Approved By",
            "fieldtype": "Link",
            "options": "User"
        },
        {
            "fieldname": "notes",
            "label": "Notes",
            "fieldtype": "Small Text"
        }
    ],
    "permissions": [
        {
            "role": "Administrator",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "delete": 1,
            "submit": 1
        },
        {
            "role": "Quality Manager",
            "ptype": "Role",
            "read": 1,
            "write": 1,
            "create": 1,
            "submit": 1
        }
    ]
}

create_doctype_if_not_exists(out_of_calibration_form)

# ============================================================================
# 23. AFFECTED WORK ORDER (Child Table)
# ============================================================================

print("\n🎯 23. Affected Work Order (Child Table)")
print("-" * 100)

affected_work_order = {
    "name": "Affected Work Order",
    "doctype": "DocType",
    "module": "THTPL",
    "custom": 1,
    "istable": 1,
    "fields": [
        {
            "fieldname": "work_order_ref",
            "label": "Work Order Reference",
            "fieldtype": "Link",
            "options": "Work Order"
        },
        {
            "fieldname": "impact_level",
            "label": "Impact Level",
            "fieldtype": "Select",
            "options": "High\nMedium\nLow"
        },
        {
            "fieldname": "action_required",
            "label": "Action Required",
            "fieldtype": "Data"
        }
    ]
}

create_doctype_if_not_exists(affected_work_order)

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "="*100)
print("✅ DOCTYPE CREATION COMPLETE")
print("="*100)
print(f"""
Summary:
├─ Quality Control Plan (THTPL/QC/QCP)
├─ QC Plan Gate (Child Table)
├─ QC Testing Type (Child Table)
├─ Material Identification Report (THTPL/QC/MIR)
├─ Material ID Detail (Child Table)
├─ Heat Treatment Report (THTPL/QC/HTR)
├─ Stage Inspection Report (THTPL/QC/STI)
├─ Inspection Finding (Child Table)
├─ Inspection Defect (Child Table)
├─ Liquid Penetrant Test Report (THTPL/QC/LPT)
├─ LPT Result Detail (Child Table)
├─ Radiography Report (THTPL/QC/RTR)
├─ Radiography Result Detail (Child Table)
├─ Pressure Test Report (THTPL/QC/PTR)
├─ Test Observation (Child Table)
├─ Weld Summary (THTPL/QC/WEL)
├─ Welder Used (Child Table)
├─ Welding Parameter (Child Table)
├─ Painting Inspection Report (THTPL/QC/PSF)
├─ Instrument Calibration List (THTPL/QC/ICL)
├─ Calibration Instrument (Child Table)
├─ Out of Calibration Form (THTPL/QC/OOC)
└─ Affected Work Order (Child Table)

Total: 23+ DocTypes + Child Tables Created

Next Steps:
1. Run: bench migrate
2. Run: bench build --force
3. Deploy custom fields script
4. Setup workflows and automations
5. Configure email alerts
6. Create dashboards and reports

""")

print("\n🎉 DocType generation completed successfully! 🎉\n")
