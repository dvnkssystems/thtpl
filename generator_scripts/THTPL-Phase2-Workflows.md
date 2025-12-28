# THTPL ERPNext - Phase 2: Approval Workflows & Auto-Notifications

## Phase 2: Setup Approval Workflows for Design & Quality Gates

### Part A: Design Approval Workflow

#### Workflow 1: Design Input Approval Workflow

**Workflow States:**
```
Draft → Submitted → Under Review → Approved → Design Sent to BOM
   ↓                                    ↓
   └──────── Rejected ←──────────────┘
```

**Frappe Workflow Configuration:**

```json
{
  "doctype": "Workflow",
  "module": "THTPL",
  "name": "Design Input Approval Workflow",
  "workflow_name": "Design Input Approval",
  "document_type": "Design Input",
  "is_active": 1,
  "states": [
    {
      "state": "Draft",
      "doc_status": 0,
      "allow_on_submit": 0
    },
    {
      "state": "Submitted",
      "doc_status": 1,
      "allow_on_submit": 1
    },
    {
      "state": "Under Review",
      "doc_status": 1,
      "allow_on_submit": 1
    },
    {
      "state": "Approved",
      "doc_status": 1,
      "allow_on_submit": 1
    },
    {
      "state": "Rejected",
      "doc_status": 1,
      "allow_on_submit": 1
    },
    {
      "state": "Design Ready",
      "doc_status": 1,
      "allow_on_submit": 1
    }
  ],
  "transitions": [
    {
      "from_state": "Draft",
      "to_state": "Submitted",
      "action": "Submit",
      "allowed_roles": ["Design Engineer"]
    },
    {
      "from_state": "Submitted",
      "to_state": "Under Review",
      "action": "Send for Review",
      "allowed_roles": ["Design Engineer"],
      "condition": "eval:doc.design_drawings"
    },
    {
      "from_state": "Under Review",
      "to_state": "Approved",
      "action": "Approve",
      "allowed_roles": ["Design Manager"],
      "condition": "eval:doc.asme_compliance_verified"
    },
    {
      "from_state": "Under Review",
      "to_state": "Rejected",
      "action": "Reject",
      "allowed_roles": ["Design Manager"]
    },
    {
      "from_state": "Rejected",
      "to_state": "Submitted",
      "action": "Resubmit",
      "allowed_roles": ["Design Engineer"]
    },
    {
      "from_state": "Approved",
      "to_state": "Design Ready",
      "action": "Mark Ready for BOM",
      "allowed_roles": ["Design Manager"]
    }
  ]
}
```

#### Workflow 2: BOM Approval Workflow

```json
{
  "doctype": "Workflow",
  "name": "BOM Approval Workflow",
  "document_type": "BOM",
  "states": [
    {
      "state": "Draft",
      "doc_status": 0
    },
    {
      "state": "Pending Approval",
      "doc_status": 1
    },
    {
      "state": "Approved",
      "doc_status": 1
    },
    {
      "state": "Rejected",
      "doc_status": 1
    },
    {
      "state": "Released to Production",
      "doc_status": 1
    }
  ],
  "transitions": [
    {
      "from_state": "Draft",
      "to_state": "Pending Approval",
      "action": "Submit for Approval",
      "allowed_roles": ["Design Engineer"],
      "condition": "eval:doc.approved_drawing_reference"
    },
    {
      "from_state": "Pending Approval",
      "to_state": "Approved",
      "action": "Approve BOM",
      "allowed_roles": ["Design Manager"],
      "description": "BOM approved. Will trigger auto-creation of Work Order and Purchase Requisitions"
    },
    {
      "from_state": "Pending Approval",
      "to_state": "Rejected",
      "action": "Reject",
      "allowed_roles": ["Design Manager"]
    },
    {
      "from_state": "Rejected",
      "to_state": "Pending Approval",
      "action": "Resubmit",
      "allowed_roles": ["Design Engineer"]
    },
    {
      "from_state": "Approved",
      "to_state": "Released to Production",
      "action": "Release to Production",
      "allowed_roles": ["Design Manager", "Production Manager"]
    }
  ]
}
```

---

### Part B: Quality Gate Workflow

#### Workflow 3: Quality Inspection Approval Workflow

**Applies to:** Liquid Penetrant Test, Radiography Report, Pressure Test Report, etc.

```json
{
  "doctype": "Workflow",
  "name": "QC Inspection Result Workflow",
  "document_type": "Liquid Penetrant Test Report",
  "states": [
    {
      "state": "Draft",
      "doc_status": 0
    },
    {
      "state": "Test Completed",
      "doc_status": 0
    },
    {
      "state": "Under Review",
      "doc_status": 1
    },
    {
      "state": "Accepted",
      "doc_status": 1
    },
    {
      "state": "Rejected",
      "doc_status": 1
    },
    {
      "state": "Retest Required",
      "doc_status": 1
    }
  ],
  "transitions": [
    {
      "from_state": "Draft",
      "to_state": "Test Completed",
      "action": "Complete Test",
      "allowed_roles": ["QC Inspector"],
      "condition": "eval:doc.tested_by and doc.test_date"
    },
    {
      "from_state": "Test Completed",
      "to_state": "Under Review",
      "action": "Submit for Review",
      "allowed_roles": ["QC Inspector"]
    },
    {
      "from_state": "Under Review",
      "to_state": "Accepted",
      "action": "Accept Result",
      "allowed_roles": ["QC Manager"],
      "condition": "eval:doc.overall_result == 'Accepted'"
    },
    {
      "from_state": "Under Review",
      "to_state": "Rejected",
      "action": "Reject Result",
      "allowed_roles": ["QC Manager"]
    },
    {
      "from_state": "Under Review",
      "to_state": "Retest Required",
      "action": "Request Retest",
      "allowed_roles": ["QC Manager"]
    },
    {
      "from_state": "Rejected",
      "to_state": "Draft",
      "action": "Return to Draft",
      "allowed_roles": ["QC Inspector"]
    }
  ]
}
```

---

### Part C: Work Order Quality Gates Workflow

```python
# hooks.py - Define workflow for Quality Gates

doc_events = {
    "Work Order": {
        "before_submit": "thtpl_erp.work_order.before_submit_work_order",
        "on_update": "thtpl_erp.work_order.update_quality_gates"
    },
    "Quality Control Plan": {
        "on_submit": "thtpl_erp.quality.create_quality_gates"
    }
}

# thtpl_erp/work_order.py

import frappe
from frappe.utils import getdate

def before_submit_work_order(doc, method):
    """Create Quality Control Plan and initialize quality gates"""
    if doc.asme_compliance_section:
        # Auto-create QCP
        qcp = frappe.new_doc("Quality Control Plan")
        qcp.sales_order_link = doc.sales_order_link
        qcp.item_code = doc.item_code
        qcp.work_order_link = doc.name
        qcp.asme_standard = doc.asme_standard
        qcp.asme_edition = doc.asme_edition
        qcp.insert()
        
        doc.quality_control_plan_link = qcp.name
        frappe.msgprint(f"Quality Control Plan {qcp.name} created automatically")


def update_quality_gates(doc, method):
    """Update quality gates based on inspection reports"""
    if doc.quality_gates_status:
        total_gates = len(doc.quality_gates_status)
        passed_gates = len([g for g in doc.quality_gates_status if g.status == "Passed"])
        
        # Update overall quality status
        if passed_gates == total_gates:
            doc.quality_status = "Accepted"
        elif passed_gates > 0:
            doc.quality_status = "In Progress"
        else:
            doc.quality_status = "Pending"
```

---

## Phase 3: Configure Auto-Notifications & Email Alerts

### Part A: Email Alert Configurations

#### Alert 1: Design Input Rejection Notification

```json
{
  "doctype": "Email Alert",
  "name": "Design Input Rejection Alert",
  "document_type": "Design Input",
  "trigger": "on_change",
  "is_enabled": 1,
  "send_to": "{doc.design_engineer.user_id}",
  "subject": "Design Input Rejected: {doc.name}",
  "message": """
  <h3>Design Input Rejected</h3>
  <p>Your Design Input <b>{doc.name}</b> for Sales Order <b>{doc.sales_order_link}</b> has been rejected by {doc.rejected_by}.</p>
  
  <p><strong>Rejection Reason:</strong></p>
  <p>{doc.rejection_reason}</p>
  
  <p>Please review the feedback and resubmit the design input for approval.</p>
  """,
  "condition": "doc.workflow_state == 'Rejected'",
  "recipients": [
    {"field_type": "email", "field_value": "design_engineer"}
  ]
}
```

#### Alert 2: BOM Approved - Auto Create Work Order

```json
{
  "doctype": "Email Alert",
  "name": "BOM Approved Alert",
  "document_type": "BOM",
  "trigger": "on_change",
  "is_enabled": 1,
  "send_to": "{doc.design_approved_by}",
  "subject": "BOM Approved & Released: {doc.name}",
  "message": """
  <h3>Bill of Materials Approved</h3>
  <p>BOM <b>{doc.name}</b> has been approved.</p>
  
  <p><strong>Next Steps:</strong></p>
  <ul>
    <li>✓ Work Order has been auto-created</li>
    <li>✓ Document Transmittal sent to Purchase, Production, and QC</li>
    <li>✓ Material Requisitions generated</li>
  </ul>
  
  <p>Production can now proceed with manufacturing.</p>
  """,
  "condition": "doc.workflow_state == 'Released to Production'",
  "recipients": [
    {"recipient_type": "Role", "recipient": "Production Manager"}
  ]
}
```

#### Alert 3: Quality Gate Failed - Critical Alert

```json
{
  "doctype": "Email Alert",
  "name": "Quality Gate Failed Alert",
  "document_type": "Liquid Penetrant Test Report",
  "trigger": "on_change",
  "is_enabled": 1,
  "priority": "High",
  "subject": "ALERT: Quality Gate Failed - {doc.work_order_link}",
  "message": """
  <h3 style="color:red;">⚠️ QUALITY GATE FAILED ⚠️</h3>
  <p>Liquid Penetrant Test for Work Order <b>{doc.work_order_link}</b> has <strong>FAILED</strong>.</p>
  
  <p><strong>Test Details:</strong></p>
  <ul>
    <li>Result: {doc.overall_result}</li>
    <li>Tested By: {doc.tested_by}</li>
    <li>Test Date: {doc.test_date}</li>
  </ul>
  
  <p><strong>Indications Found:</strong></p>
  <p>{doc.indications_description}</p>
  
  <p><strong>Immediate Action Required:</strong></p>
  <ol>
    <li>Production to halt further work on this WO</li>
    <li>QC Manager to review and decide: Rework vs Deviation</li>
    <li>Create Deviation Change Note if applicable</li>
  </ol>
  """,
  "condition": "doc.overall_result == 'Rejected'",
  "recipients": [
    {"recipient_type": "Role", "recipient": "QC Manager"},
    {"recipient_type": "Role", "recipient": "Production Manager"}
  ]
}
```

#### Alert 4: Pressure Test Passed - Release for Dispatch

```json
{
  "doctype": "Email Alert",
  "name": "Pressure Test Passed Alert",
  "document_type": "Pressure Test Report",
  "trigger": "on_change",
  "is_enabled": 1,
  "subject": "Pressure Test PASSED: {doc.work_order_link} Ready for Dispatch",
  "message": """
  <h3 style="color:green;">✓ Pressure Test PASSED</h3>
  <p>Pressure/Hydrostatic Test for Work Order <b>{doc.work_order_link}</b> has been <strong>PASSED</strong>.</p>
  
  <p><strong>Test Parameters:</strong></p>
  <ul>
    <li>Test Type: {doc.test_type}</li>
    <li>Design Pressure: {doc.design_pressure} kg/cm²</li>
    <li>Test Pressure: {doc.test_pressure} kg/cm²</li>
    <li>Holding Time: {doc.holding_time} hours</li>
  </ul>
  
  <p><strong>Status:</strong> ✓ All Quality Gates Completed</p>
  
  <p><strong>Next Steps:</strong></p>
  <ul>
    <li>Proceed to Surface Preparation & Painting</li>
    <li>After painting → Final Inspection Release</li>
    <li>Then → Ready for Delivery</li>
  </ul>
  """,
  "condition": "doc.overall_result == 'Accepted'",
  "recipients": [
    {"recipient_type": "Role", "recipient": "QC Manager"},
    {"recipient_type": "Role", "recipient": "Production Manager"}
  ]
}
```

#### Alert 5: Calibration Due - Preventive Alert

```json
{
  "doctype": "Email Alert",
  "name": "Instrument Calibration Due Alert",
  "document_type": "Asset",
  "trigger": "daily",
  "is_enabled": 1,
  "subject": "REMINDER: Instrument Calibration Due - {doc.name}",
  "message": """
  <h3>Instrument Calibration Reminder</h3>
  <p>Equipment <b>{doc.name}</b> calibration is due within 7 days.</p>
  
  <p><strong>Equipment Details:</strong></p>
  <ul>
    <li>Last Calibration: {doc.last_calibration_date}</li>
    <li>Next Due Date: {doc.next_calibration_due_date}</li>
    <li>Calibration Status: {doc.calibration_status}</li>
  </ul>
  
  <p>Please schedule calibration immediately to avoid production delays.</p>
  """,
  "condition": "frappe.utils.getdate(doc.next_calibration_due_date) <= frappe.utils.add_days(frappe.utils.today(), 7)",
  "recipients": [
    {"recipient_type": "Role", "recipient": "QC Manager"}
  ]
}
```

---

### Part B: Automated Workflow Actions

```python
# hooks.py - Server-side automation

doc_events = {
    "BOM": {
        "on_submit": [
            "thtpl_erp.bom.create_work_order",
            "thtpl_erp.bom.generate_transmittal",
            "thtpl_erp.bom.create_material_requisitions"
        ]
    },
    "Work Order": {
        "on_submit": "thtpl_erp.work_order.create_quality_control_plan"
    },
    "Quality Control Plan": {
        "on_submit": "thtpl_erp.quality.initialize_quality_gates"
    },
    "Liquid Penetrant Test Report": {
        "on_submit": "thtpl_erp.quality.update_work_order_gate_status"
    },
    "Radiography Report": {
        "on_submit": "thtpl_erp.quality.update_work_order_gate_status"
    },
    "Pressure Test Report": {
        "on_submit": "thtpl_erp.quality.check_final_gate"
    }
}

# thtpl_erp/bom.py

def create_work_order(doc, method):
    """Auto-create Work Order when BOM is approved"""
    if doc.workflow_state == "Released to Production":
        wo = frappe.new_doc("Work Order")
        wo.sales_order_link = doc.sales_order_reference
        wo.item_code = doc.item_code
        wo.bom_no = doc.name
        wo.insert(ignore_permissions=True)
        frappe.msgprint(f"Work Order {wo.name} created automatically")


def generate_transmittal(doc, method):
    """Generate transmittals to PUR, PRD, QC"""
    departments = ["Purchase", "Production", "Quality Control"]
    
    for dept in departments:
        transmittal = frappe.new_doc("Document Transmittal")
        transmittal.document_type = "BOM"
        transmittal.document_title = f"BOM - {doc.item_code}"
        transmittal.document_reference_link = doc.name
        transmittal.from_department = "Design & Development"
        transmittal.to_departments = [{"recipient_department": dept}]
        transmittal.status_type = "Information"
        transmittal.insert(ignore_permissions=True)


def create_material_requisitions(doc, method):
    """Auto-create Material Requisitions from BOM"""
    mr = frappe.new_doc("Material Request")
    mr.material_request_type = "Purchase"
    mr.set_warehouse = "Raw Material - THTPL"
    
    for item in doc.items:
        mr.append('items', {
            'item_code': item.item_code,
            'qty': item.qty,
            'uom': item.uom
        })
    
    mr.insert(ignore_permissions=True)
    frappe.msgprint(f"Material Request {mr.name} created")


# thtpl_erp/quality.py

def update_work_order_gate_status(doc, method):
    """Update Work Order quality gate status when inspection completes"""
    work_order = frappe.get_doc("Work Order", doc.work_order_link)
    
    for gate in work_order.quality_gates_status:
        if gate.gate_name == doc.doctype and gate.status == "Pending":
            gate.status = "Passed" if doc.overall_result == "Accepted" else "Failed"
            gate.inspection_date = frappe.utils.today()
            gate.inspected_by = doc.tested_by or doc.inspected_by
            gate.report_reference = doc.name
    
    work_order.save(ignore_permissions=True)


def check_final_gate(doc, method):
    """Check if all quality gates passed - if yes, trigger final release"""
    work_order = frappe.get_doc("Work Order", doc.work_order_link)
    
    all_passed = all(g.status == "Passed" for g in work_order.quality_gates_status)
    any_failed = any(g.status == "Failed" for g in work_order.quality_gates_status)
    
    if all_passed:
        work_order.quality_status = "Accepted"
        work_order.save(ignore_permissions=True)
        
        # Send notification
        frappe.sendmail(
            recipients=frappe.db.get_value('Employee', {
                'designation': 'QC Manager'
            }, 'user_id'),
            subject=f"All Quality Gates Passed - {work_order.name}",
            message=f"Work Order {work_order.name} is ready for final inspection and dispatch."
        )
    
    elif any_failed:
        work_order.quality_status = "Rejected"
        work_order.save(ignore_permissions=True)
```

---

## Summary: Email Alerts & Auto-Workflows

| Alert | Trigger | Recipients | Action |
|-------|---------|------------|--------|
| Design Rejected | Workflow state = Rejected | Design Engineer | Resubmit design |
| BOM Approved | WF state = Released | Production Mgr | Create WO, Transmittal |
| Quality Gate Failed | Test result = Rejected | QC Mgr, Prod Mgr | Halt production, NCR |
| Pressure Test Passed | Test result = Accepted | QC Mgr, Prod Mgr | Proceed to painting |
| Calibration Due | Within 7 days | QC Manager | Schedule calibration |
| NCR Created | New Deviation | QC Mgr, Engineering | Review & approve |

---

**Document Version:** 1.0  
**Last Updated:** December 19, 2025  
**Status:** Workflow & Notification Specs Ready  
**Next Phase:** ASME Compliance Dashboards
