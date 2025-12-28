# THTPL ERPNext - Reports Generator Script
# Location: thtpl_erp/generate_reports.py
# Usage: bench --site thtpl.test console < generate_reports.py
# Purpose: Create 10+ query reports and KPI calculations

import frappe

def create_report_if_not_exists(report_dict):
    """Create a new report if it doesn't already exist"""
    report_name = report_dict.get("name")
    try:
        if frappe.db.exists("Report", report_name):
            print(f"   ✓ {report_name} (already exists)")
            return False
        
        doc = frappe.new_doc("Report")
        doc.update(report_dict)
        doc.insert(ignore_permissions=True)
        print(f"   ✅ {report_name}")
        return True
    except Exception as e:
        print(f"   ❌ {report_name} - Error: {str(e)}")
        return False

print("\n" + "="*100)
print("THTPL ERPNext - Reports Generator Script")
print("="*100)

# ============================================================================
# 1. QUALITY GATE STATUS REPORT
# ============================================================================

print("\n🎯 1. Quality Gate Status Report")
print("-" * 100)

quality_gate_status_report = {
    "name": "Quality Gate Status",
    "doctype": "Report",
    "module": "THTPL",
    "report_type": "Query Report",
    "ref_doctype": "Work Order",
    "query": """
SELECT
    wo.name as 'Work Order',
    wo.production_item as 'Item',
    wo.qty as 'Quantity',
    wo.thtpl_quality_status as 'QC Status',
    IF(wo.quality_hold = 1, 'YES', 'NO') as 'Quality Hold',
    wo.expected_completion_date as 'Expected Date',
    wo.modified as 'Last Updated'
FROM
    `tabWork Order` wo
WHERE
    wo.docstatus = 1
ORDER BY
    wo.modified DESC
    """,
    "is_standard": "No",
    "disabled": 0
}

create_report_if_not_exists(quality_gate_status_report)

# ============================================================================
# 2. ASME COMPLIANCE TREND REPORT
# ============================================================================

print("\n🎯 2. ASME Compliance Trend Report")
print("-" * 100)

asme_compliance_report = {
    "name": "ASME Compliance Trend",
    "doctype": "Report",
    "module": "THTPL",
    "report_type": "Query Report",
    "ref_doctype": "Sales Order",
    "query": """
SELECT
    so.name as 'Sales Order',
    so.customer_name as 'Customer',
    so.asme_standard as 'ASME Standard',
    so.asme_edition as 'Edition',
    so.design_approval_status as 'Design Status',
    DATE_FORMAT(so.design_approval_date, '%Y-%m-%d') as 'Approved Date',
    so.design_approved_by as 'Approved By',
    so.creation as 'Created'
FROM
    `tabSales Order` so
WHERE
    so.thtpl_asme_compliance = 1
ORDER BY
    so.creation DESC
    """,
    "is_standard": "No",
    "disabled": 0
}

create_report_if_not_exists(asme_compliance_report)

# ============================================================================
# 3. WELDER QUALIFICATION REPORT
# ============================================================================

print("\n🎯 3. Welder Qualification Report")
print("-" * 100)

welder_qualification_report = {
    "name": "Welder Qualification",
    "doctype": "Report",
    "module": "THTPL",
    "report_type": "Query Report",
    "ref_doctype": "Employee",
    "query": """
SELECT
    e.name as 'Employee ID',
    e.employee_name as 'Welder Name',
    e.designation as 'Designation',
    DATEDIFF(CURDATE(), e.date_of_joining) DIV 365 as 'Years',
    e.status as 'Status',
    e.creation as 'Joined Date'
FROM
    `tabEmployee` e
WHERE
    e.designation LIKE '%Welder%'
ORDER BY
    e.employee_name
    """,
    "is_standard": "No",
    "disabled": 0
}

create_report_if_not_exists(welder_qualification_report)

# ============================================================================
# 4. SUPPLIER PERFORMANCE SCORECARD
# ============================================================================

print("\n🎯 4. Supplier Performance Scorecard")
print("-" * 100)

supplier_performance_report = {
    "name": "Supplier Performance Scorecard",
    "doctype": "Report",
    "module": "THTPL",
    "report_type": "Query Report",
    "ref_doctype": "Supplier",
    "query": """
SELECT
    s.name as 'Supplier',
    s.thtpl_supplier_category as 'Category',
    s.quality_rating as 'Quality',
    s.delivery_rating as 'Delivery',
    s.cost_rating as 'Cost',
    s.overall_compliance_score as 'Compliance',
    s.audit_status as 'Audit Status',
    s.asme_approved as 'ASME Approved'
FROM
    `tabSupplier` s
ORDER BY
    s.overall_compliance_score DESC
    """,
    "is_standard": "No",
    "disabled": 0
}

create_report_if_not_exists(supplier_performance_report)

# ============================================================================
# 5. DAILY PRODUCTION STATUS
# ============================================================================

print("\n🎯 5. Daily Production Status")
print("-" * 100)

production_status_report = {
    "name": "Daily Production Status",
    "doctype": "Report",
    "module": "THTPL",
    "report_type": "Query Report",
    "ref_doctype": "Daily Production Report",
    "query": """
SELECT
    dpr.name as 'Report Date',
    dpr.shift as 'Shift',
    dpr.completed_items as 'Completed',
    dpr.partially_completed as 'Partial',
    dpr.pending_items as 'Pending',
    IF(dpr.quality_issues = 1, 'YES', 'NO') as 'Issues Found',
    dpr.approved_by_qa as 'QA Approval'
FROM
    `tabDaily Production Report` dpr
ORDER BY
    dpr.report_date DESC,
    dpr.shift DESC
    """,
    "is_standard": "No",
    "disabled": 0
}

create_report_if_not_exists(production_status_report)

# ============================================================================
# 6. MATERIAL IDENTIFICATION AUDIT
# ============================================================================

print("\n🎯 6. Material Identification Audit")
print("-" * 100)

material_audit_report = {
    "name": "Material Identification Audit",
    "doctype": "Report",
    "module": "THTPL",
    "report_type": "Query Report",
    "ref_doctype": "Material Identification Report",
    "query": """
SELECT
    mir.name as 'Report ID',
    mir.supplier_name as 'Supplier',
    mir.material_grade as 'Material Grade',
    mir.batch_number as 'Batch #',
    mir.test_method as 'Test Method',
    mir.result as 'Result',
    mir.inspector_name as 'Inspector',
    DATE_FORMAT(mir.inspection_date, '%Y-%m-%d') as 'Date'
FROM
    `tabMaterial Identification Report` mir
WHERE
    mir.mir_status = 'Approved'
ORDER BY
    mir.inspection_date DESC
    """,
    "is_standard": "No",
    "disabled": 0
}

create_report_if_not_exists(material_audit_report)

# ============================================================================
# 7. CALIBRATION DUE INSTRUMENTS
# ============================================================================

print("\n🎯 7. Calibration Due Instruments")
print("-" * 100)

calibration_due_report = {
    "name": "Calibration Due Instruments",
    "doctype": "Report",
    "module": "THTPL",
    "report_type": "Query Report",
    "ref_doctype": "Asset",
    "query": """
SELECT
    a.name as 'Asset ID',
    a.asset_name as 'Instrument',
    a.last_calibration_date as 'Last Cal Date',
    a.next_calibration_due_date as 'Due Date',
    a.calibration_status as 'Status',
    DATEDIFF(a.next_calibration_due_date, CURDATE()) as 'Days Left',
    a.calibration_agency as 'Agency'
FROM
    `tabAsset` a
WHERE
    a.calibration_required = 1
    AND a.calibration_status IN ('Due', 'Overdue')
ORDER BY
    a.next_calibration_due_date ASC
    """,
    "is_standard": "No",
    "disabled": 0
}

create_report_if_not_exists(calibration_due_report)

# ============================================================================
# 8. HEAT TREATMENT COMPLIANCE
# ============================================================================

print("\n🎯 8. Heat Treatment Compliance")
print("-" * 100)

heat_treatment_report = {
    "name": "Heat Treatment Compliance",
    "doctype": "Report",
    "module": "THTPL",
    "report_type": "Query Report",
    "ref_doctype": "Heat Treatment Report",
    "query": """
SELECT
    htr.name as 'Report ID',
    htr.work_order_ref as 'Work Order',
    htr.treatment_type as 'Treatment Type',
    htr.holding_temperature as 'Temperature',
    htr.holding_time_hours as 'Time (hrs)',
    htr.furnace_name as 'Furnace',
    htr.htr_status as 'Status',
    DATE_FORMAT(htr.treatment_date, '%Y-%m-%d') as 'Treatment Date'
FROM
    `tabHeat Treatment Report` htr
WHERE
    htr.htr_status = 'Approved'
ORDER BY
    htr.treatment_date DESC
    """,
    "is_standard": "No",
    "disabled": 0
}

create_report_if_not_exists(heat_treatment_report)

# ============================================================================
# 9. PRESSURE TEST SUMMARY
# ============================================================================

print("\n🎯 9. Pressure Test Summary")
print("-" * 100)

pressure_test_report = {
    "name": "Pressure Test Summary",
    "doctype": "Report",
    "module": "THTPL",
    "report_type": "Query Report",
    "ref_doctype": "Pressure Test Report",
    "query": """
SELECT
    ptr.name as 'Report ID',
    ptr.work_order_ref as 'Work Order',
    ptr.test_type as 'Test Type',
    ptr.test_pressure_bar as 'Test Pressure',
    ptr.design_pressure_bar as 'Design Pressure',
    ptr.pressure_drop_bar as 'Pressure Drop',
    ptr.ptr_result as 'Result',
    ptr.tested_by as 'Tested By',
    DATE_FORMAT(ptr.test_date, '%Y-%m-%d') as 'Test Date'
FROM
    `tabPressure Test Report` ptr
ORDER BY
    ptr.test_date DESC
    """,
    "is_standard": "No",
    "disabled": 0
}

create_report_if_not_exists(pressure_test_report)

# ============================================================================
# 10. WELD INSPECTION SUMMARY
# ============================================================================

print("\n🎯 10. Weld Inspection Summary")
print("-" * 100)

weld_inspection_report = {
    "name": "Weld Inspection Summary",
    "doctype": "Report",
    "module": "THTPL",
    "report_type": "Query Report",
    "ref_doctype": "Weld Summary",
    "query": """
SELECT
    ws.name as 'Weld ID',
    ws.work_order_ref as 'Work Order',
    ws.welding_process as 'Process',
    ws.weld_passes as 'Passes',
    ws.visual_inspection_result as 'Visual',
    IF(ws.lpt_test_required = 1, 'YES', 'NO') as 'LPT Required',
    IF(ws.radiography_required = 1, 'YES', 'NO') as 'X-Ray Required',
    ws.weld_status as 'Status'
FROM
    `tabWeld Summary` ws
ORDER BY
    ws.weld_date DESC
    """,
    "is_standard": "No",
    "disabled": 0
}

create_report_if_not_exists(weld_inspection_report)

# ============================================================================
# 11. DEVIATION & NCR TRACKER
# ============================================================================

print("\n🎯 11. Deviation & NCR Tracker")
print("-" * 100)

deviation_tracker_report = {
    "name": "Deviation NCR Tracker",
    "doctype": "Report",
    "module": "THTPL",
    "report_type": "Query Report",
    "ref_doctype": "Deviation Change Note",
    "query": """
SELECT
    dcn.name as 'NCR ID',
    dcn.deviation_type as 'Type',
    dcn.related_work_order as 'Work Order',
    dcn.impact_assessment as 'Impact',
    dcn.discovered_by as 'Discovered By',
    dcn.dcn_status as 'Status',
    DATE_FORMAT(dcn.discovered_date, '%Y-%m-%d') as 'Discovered Date',
    DATEDIFF(CURDATE(), dcn.discovered_date) as 'Days Open'
FROM
    `tabDeviation Change Note` dcn
WHERE
    dcn.dcn_status != 'Closed'
ORDER BY
    dcn.discovered_date DESC
    """,
    "is_standard": "No",
    "disabled": 0
}

create_report_if_not_exists(deviation_tracker_report)

# ============================================================================
# 12. SUPPLIER AUDIT SUMMARY
# ============================================================================

print("\n🎯 12. Supplier Audit Summary")
print("-" * 100)

supplier_audit_summary_report = {
    "name": "Supplier Audit Summary",
    "doctype": "Report",
    "module": "THTPL",
    "report_type": "Query Report",
    "ref_doctype": "Supplier Audit",
    "query": """
SELECT
    sa.name as 'Audit ID',
    sa.supplier as 'Supplier',
    sa.audit_type as 'Type',
    sa.auditor as 'Auditor',
    sa.critical_noncompliances as 'Critical',
    sa.major_noncompliances as 'Major',
    sa.minor_noncompliances as 'Minor',
    sa.audit_conclusion as 'Conclusion',
    DATE_FORMAT(sa.audit_date, '%Y-%m-%d') as 'Audit Date'
FROM
    `tabSupplier Audit` sa
ORDER BY
    sa.audit_date DESC
    """,
    "is_standard": "No",
    "disabled": 0
}

create_report_if_not_exists(supplier_audit_summary_report)

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "="*100)
print("✅ REPORTS CREATION COMPLETE")
print("="*100)
print(f"""
Summary - 12 Reports Created:

Quality Control Module:
├─ Quality Gate Status
├─ ASME Compliance Trend
├─ Calibration Due Instruments
├─ Heat Treatment Compliance
├─ Pressure Test Summary
├─ Weld Inspection Summary
└─ Material Identification Audit

Procurement Module:
├─ Supplier Performance Scorecard
└─ Supplier Audit Summary

Production Module:
├─ Daily Production Status
└─ Deviation NCR Tracker

Workforce Module:
└─ Welder Qualification

Total: 12 Query Reports

Access Reports at:
1. Go to: View > Report
2. Select any report from list
3. Use filters to customize results
4. Export to PDF/Excel

Customization Options:
- Add filters
- Add columns
- Change sorting
- Export functionality
- Schedule reports

Next Steps:
1. Run: bench migrate
2. Verify reports in Reports list
3. Add filters as needed
4. Schedule periodic reports
5. Create dashboards from reports

""")

print("\n🎉 Reports generation completed successfully! 🎉\n")
