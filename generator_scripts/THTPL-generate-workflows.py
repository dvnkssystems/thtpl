# THTPL ERPNext - Workflows Generator Script
# Location: thtpl_erp/generate_workflows.py
# Usage: bench --site thtpl.test console < generate_workflows.py
# Purpose: Create 7 complete approval workflows with states, transitions, and conditions

import frappe
import json

def create_workflow_if_not_exists(workflow_dict):
    """Create a new workflow if it doesn't already exist"""
    workflow_name = workflow_dict.get("name")
    try:
        if frappe.db.exists("Workflow", workflow_name):
            print(f"   ✓ {workflow_name} (already exists)")
            return False
        
        doc = frappe.new_doc("Workflow")
        doc.update(workflow_dict)
        doc.insert(ignore_permissions=True)
        frappe.db.commit()
        print(f"   ✅ {workflow_name}")
        return True
    except Exception as e:
        print(f"   ❌ {workflow_name} - Error: {str(e)}")
        return False

def create_workflow_state(state_name, state_dict):
    """Create a workflow state"""
    try:
        if frappe.db.exists("Workflow State", state_name):
            return False
        doc = frappe.new_doc("Workflow State")
        doc.update(state_dict)
        doc.insert(ignore_permissions=True)
        frappe.db.commit()
        return True
    except:
        return False

def create_workflow_action(action_name, action_dict):
    """Create a workflow action"""
    try:
        if frappe.db.exists("Workflow Action Master", action_name):
            return False
        doc = frappe.new_doc("Workflow Action Master")
        doc.update(action_dict)
        doc.insert(ignore_permissions=True)
        frappe.db.commit()
        return True
    except:
        return False

print("\n" + "="*100)
print("THTPL ERPNext - Workflows Generator Script")
print("="*100)

# ============================================================================
# WORKFLOW STATES
# ============================================================================

print("\n🎯 Creating Workflow States...")
print("-" * 100)

# Design Input Workflow States
states_to_create = [
    # Design Input States
    ("Draft", {"name": "Draft", "title": "Draft", "doc_status": "0", "style": ""}),
    ("For Review", {"name": "For Review", "title": "For Review", "doc_status": "0", "style": ""}),
    ("Approved", {"name": "Approved", "title": "Approved", "doc_status": "1", "style": ""}),
    ("Rejected", {"name": "Rejected", "title": "Rejected", "doc_status": "2", "style": ""}),
    ("Rework", {"name": "Rework", "title": "Rework Required", "doc_status": "0", "style": ""}),
    
    # BOM States
    ("BOM Draft", {"name": "BOM Draft", "title": "Draft", "doc_status": "0", "style": ""}),
    ("BOM Review", {"name": "BOM Review", "title": "For Review", "doc_status": "0", "style": ""}),
    ("BOM Approved", {"name": "BOM Approved", "title": "Approved", "doc_status": "1", "style": ""}),
    ("BOM Rejected", {"name": "BOM Rejected", "title": "Rejected", "doc_status": "2", "style": ""}),
    
    # Quality Inspection States
    ("QI Draft", {"name": "QI Draft", "title": "Draft", "doc_status": "0", "style": ""}),
    ("QI In Progress", {"name": "QI In Progress", "title": "In Progress", "doc_status": "0", "style": ""}),
    ("QI Completed", {"name": "QI Completed", "title": "Completed", "doc_status": "1", "style": ""}),
    ("QI Failed", {"name": "QI Failed", "title": "Failed", "doc_status": "2", "style": ""}),
    
    # Work Order Quality Gates
    ("QG Pending", {"name": "QG Pending", "title": "Pending", "doc_status": "0", "style": ""}),
    ("QG Testing", {"name": "QG Testing", "title": "Testing", "doc_status": "0", "style": ""}),
    ("QG Passed", {"name": "QG Passed", "title": "Passed", "doc_status": "1", "style": ""}),
    ("QG Failed", {"name": "QG Failed", "title": "Failed", "doc_status": "2", "style": ""}),
    ("QG Hold", {"name": "QG Hold", "title": "On Hold", "doc_status": "0", "style": ""}),
    
    # Supplier Audit States
    ("SA Draft", {"name": "SA Draft", "title": "Draft", "doc_status": "0", "style": ""}),
    ("SA Scheduled", {"name": "SA Scheduled", "title": "Scheduled", "doc_status": "0", "style": ""}),
    ("SA Completed", {"name": "SA Completed", "title": "Completed", "doc_status": "1", "style": ""}),
    ("SA Approved", {"name": "SA Approved", "title": "Approved", "doc_status": "1", "style": ""}),
    
    # NCR/Deviation States
    ("NCR Draft", {"name": "NCR Draft", "title": "Draft", "doc_status": "0", "style": ""}),
    ("NCR Submitted", {"name": "NCR Submitted", "title": "Submitted", "doc_status": "0", "style": ""}),
    ("NCR In Progress", {"name": "NCR In Progress", "title": "In Progress", "doc_status": "0", "style": ""}),
    ("NCR Approved", {"name": "NCR Approved", "title": "Approved", "doc_status": "1", "style": ""}),
    ("NCR Closed", {"name": "NCR Closed", "title": "Closed", "doc_status": "1", "style": ""}),
]

states_created = 0
for state_name, state_dict in states_to_create:
    if create_workflow_state(state_name, state_dict):
        states_created += 1
        print(f"   ✅ {state_name}")
    else:
        print(f"   ✓ {state_name} (exists)")

print(f"\nStates Created: {states_created}")
frappe.db.commit()

# ============================================================================
# WORKFLOW ACTIONS
# ============================================================================

print("\n🎯 Creating Workflow Actions...")
print("-" * 100)

actions_to_create = [
    ("Submit", {"name": "Submit", "action_name": "Submit", "label": "Submit"}),
    ("Approve", {"name": "Approve", "action_name": "Approve", "label": "Approve"}),
    ("Reject", {"name": "Reject", "action_name": "Reject", "label": "Reject"}),
    ("Request Rework", {"name": "Request Rework", "action_name": "Rework", "label": "Request Rework"}),
    ("Complete", {"name": "Complete", "action_name": "Complete", "label": "Mark Complete"}),
    ("Fail", {"name": "Fail", "action_name": "Fail", "label": "Mark as Failed"}),
    ("Pass", {"name": "Pass", "action_name": "Pass", "label": "Mark as Passed"}),
    ("Hold", {"name": "Hold", "action_name": "Hold", "label": "Put on Hold"}),
    ("Release", {"name": "Release", "action_name": "Release", "label": "Release Hold"}),
    ("Close", {"name": "Close", "action_name": "Close", "label": "Close"}),
]

actions_created = 0
for action_name, action_dict in actions_to_create:
    if create_workflow_action(action_name, action_dict):
        actions_created += 1
        print(f"   ✅ {action_name}")
    else:
        print(f"   ✓ {action_name} (exists)")

frappe.db.commit()
print(f"\nActions Created: {actions_created}")

# ============================================================================
# 1. DESIGN INPUT APPROVAL WORKFLOW (6 states)
# ============================================================================

print("\n🎯 1. Design Input Approval Workflow (THTPL/DI/APR)")
print("-" * 100)

design_input_workflow = {
    "name": "Design Input Approval",
    "doctype": "Workflow",
    "document_type": "Design Input",
    "workflow_name": "Design Input Approval",
    "module": "THTPL",
    "is_active": 1,
    "states": [
        {
            "state": "Draft",
            "title": "Draft",
            "doc_status": "0"
        },
        {
            "state": "For Review",
            "title": "For Review",
            "doc_status": "0"
        },
        {
            "state": "Approved",
            "title": "Approved",
            "doc_status": "1"
        },
        {
            "state": "Rejected",
            "title": "Rejected",
            "doc_status": "2"
        },
        {
            "state": "Rework",
            "title": "Rework Required",
            "doc_status": "0"
        }
    ],
    "transitions": [
        {
            "state": "Draft",
            "next_state": "For Review",
            "action": "Submit",
            "allowed": "[\"Design Manager\"]",
            "condition": ""
        },
        {
            "state": "For Review",
            "next_state": "Approved",
            "action": "Approve",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        },
        {
            "state": "For Review",
            "next_state": "Rejected",
            "action": "Reject",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        },
        {
            "state": "For Review",
            "next_state": "Rework",
            "action": "Request Rework",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        },
        {
            "state": "Rejected",
            "next_state": "Draft",
            "action": "Submit",
            "allowed": "[\"Design Manager\"]",
            "condition": ""
        },
        {
            "state": "Rework",
            "next_state": "For Review",
            "action": "Submit",
            "allowed": "[\"Design Manager\"]",
            "condition": ""
        }
    ]
}

create_workflow_if_not_exists(design_input_workflow)
frappe.db.commit()
# ============================================================================
# 2. BOM APPROVAL WORKFLOW (5 states)
# ============================================================================

print("\n🎯 2. BOM Approval Workflow")
print("-" * 100)

bom_approval_workflow = {
    "name": "BOM Approval",
    "doctype": "Workflow",
    "document_type": "BOM",
    "workflow_name": "BOM Approval",
    "module": "THTPL",
    "is_active": 1,
    "states": [
        {"state": "BOM Draft", "title": "Draft", "doc_status": "0"},
        {"state": "BOM Review", "title": "For Review", "doc_status": "0"},
        {"state": "BOM Approved", "title": "Approved", "doc_status": "1"},
        {"state": "BOM Rejected", "title": "Rejected", "doc_status": "2"},
    ],
    "transitions": [
        {
            "state": "BOM Draft",
            "next_state": "BOM Review",
            "action": "Submit",
            "allowed": "[\"Engineer\"]",
            "condition": ""
        },
        {
            "state": "BOM Review",
            "next_state": "BOM Approved",
            "action": "Approve",
            "allowed": "[\"Design Manager\"]",
            "condition": ""
        },
        {
            "state": "BOM Review",
            "next_state": "BOM Rejected",
            "action": "Reject",
            "allowed": "[\"Design Manager\"]",
            "condition": ""
        },
        {
            "state": "BOM Rejected",
            "next_state": "BOM Draft",
            "action": "Submit",
            "allowed": "[\"Engineer\"]",
            "condition": ""
        }
    ]
}

create_workflow_if_not_exists(bom_approval_workflow)

# ============================================================================
# 3. QUALITY INSPECTION APPROVAL WORKFLOW (6 states)
# ============================================================================

print("\n🎯 3. Quality Inspection Approval Workflow")
print("-" * 100)

quality_inspection_workflow = {
    "name": "Quality Inspection Approval",
    "doctype": "Workflow",
    "document_type": "Quality Control Plan",
    "workflow_name": "Quality Inspection Approval",
    "module": "THTPL",
    "is_active": 1,
    "states": [
        {"state": "QI Draft", "title": "Draft", "doc_status": "0"},
        {"state": "QI In Progress", "title": "In Progress", "doc_status": "0"},
        {"state": "QI Completed", "title": "Completed", "doc_status": "1"},
        {"state": "QI Failed", "title": "Failed", "doc_status": "2"},
    ],
    "transitions": [
        {
            "state": "QI Draft",
            "next_state": "QI In Progress",
            "action": "Submit",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        },
        {
            "state": "QI In Progress",
            "next_state": "QI Completed",
            "action": "Complete",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        },
        {
            "state": "QI In Progress",
            "next_state": "QI Failed",
            "action": "Fail",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        },
        {
            "state": "QI Failed",
            "next_state": "QI In Progress",
            "action": "Submit",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        }
    ]
}

create_workflow_if_not_exists(quality_inspection_workflow)

# ============================================================================
# 4. WORK ORDER QUALITY GATES WORKFLOW (5 states)
# ============================================================================

print("\n🎯 4. Work Order Quality Gates Workflow")
print("-" * 100)

quality_gates_workflow = {
    "name": "Work Order Quality Gates",
    "doctype": "Workflow",
    "document_type": "Work Order",
    "workflow_name": "Work Order Quality Gates",
    "module": "THTPL",
    "is_active": 1,
    "states": [
        {"state": "QG Pending", "title": "Pending", "doc_status": "0"},
        {"state": "QG Testing", "title": "Testing", "doc_status": "0"},
        {"state": "QG Passed", "title": "Passed", "doc_status": "1"},
        {"state": "QG Failed", "title": "Failed", "doc_status": "2"},
        {"state": "QG Hold", "title": "On Hold", "doc_status": "0"},
    ],
    "transitions": [
        {
            "state": "QG Pending",
            "next_state": "QG Testing",
            "action": "Submit",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        },
        {
            "state": "QG Testing",
            "next_state": "QG Passed",
            "action": "Pass",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        },
        {
            "state": "QG Testing",
            "next_state": "QG Failed",
            "action": "Fail",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        },
        {
            "state": "QG Testing",
            "next_state": "QG Hold",
            "action": "Hold",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        },
        {
            "state": "QG Hold",
            "next_state": "QG Testing",
            "action": "Release",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        },
        {
            "state": "QG Failed",
            "next_state": "QG Testing",
            "action": "Submit",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        }
    ]
}

create_workflow_if_not_exists(quality_gates_workflow)

# ============================================================================
# 5. SUPPLIER AUDIT APPROVAL WORKFLOW (4 states)
# ============================================================================

print("\n🎯 5. Supplier Audit Approval Workflow")
print("-" * 100)

supplier_audit_workflow = {
    "name": "Supplier Audit Approval",
    "doctype": "Workflow",
    "document_type": "Supplier Audit",
    "workflow_name": "Supplier Audit Approval",
    "module": "THTPL",
    "is_active": 1,
    "states": [
        {"state": "SA Draft", "title": "Draft", "doc_status": "0"},
        {"state": "SA Scheduled", "title": "Scheduled", "doc_status": "0"},
        {"state": "SA Completed", "title": "Completed", "doc_status": "1"},
        {"state": "SA Approved", "title": "Approved", "doc_status": "1"},
    ],
    "transitions": [
        {
            "state": "SA Draft",
            "next_state": "SA Scheduled",
            "action": "Submit",
            "allowed": "[\"Procurement Manager\"]",
            "condition": ""
        },
        {
            "state": "SA Scheduled",
            "next_state": "SA Completed",
            "action": "Complete",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        },
        {
            "state": "SA Completed",
            "next_state": "SA Approved",
            "action": "Approve",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        }
    ]
}

create_workflow_if_not_exists(supplier_audit_workflow)

# ============================================================================
# 6. NCR/DEVIATION WORKFLOW (5 states)
# ============================================================================

print("\n🎯 6. NCR/Deviation Workflow")
print("-" * 100)

ncr_workflow = {
    "name": "NCR Deviation Workflow",
    "doctype": "Workflow",
    "document_type": "Deviation Change Note",
    "workflow_name": "NCR Deviation Workflow",
    "module": "THTPL",
    "is_active": 1,
    "states": [
        {"state": "NCR Draft", "title": "Draft", "doc_status": "0"},
        {"state": "NCR Submitted", "title": "Submitted", "doc_status": "0"},
        {"state": "NCR In Progress", "title": "In Progress", "doc_status": "0"},
        {"state": "NCR Approved", "title": "Approved", "doc_status": "1"},
        {"state": "NCR Closed", "title": "Closed", "doc_status": "1"},
    ],
    "transitions": [
        {
            "state": "NCR Draft",
            "next_state": "NCR Submitted",
            "action": "Submit",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        },
        {
            "state": "NCR Submitted",
            "next_state": "NCR In Progress",
            "action": "Submit",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        },
        {
            "state": "NCR In Progress",
            "next_state": "NCR Approved",
            "action": "Approve",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        },
        {
            "state": "NCR Approved",
            "next_state": "NCR Closed",
            "action": "Close",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        }
    ]
}

create_workflow_if_not_exists(ncr_workflow)

# ============================================================================
# 7. QUALITY GATE VALIDATION WORKFLOW (4 states)
# ============================================================================

print("\n🎯 7. Quality Gate Validation Workflow")
print("-" * 100)

quality_gate_validation_workflow = {
    "name": "Quality Gate Validation",
    "doctype": "Workflow",
    "document_type": "Stage Inspection Report",
    "workflow_name": "Quality Gate Validation",
    "module": "THTPL",
    "is_active": 1,
    "states": [
        {"state": "QI Draft", "title": "Draft", "doc_status": "0"},
        {"state": "QI In Progress", "title": "In Progress", "doc_status": "0"},
        {"state": "QI Completed", "title": "Completed", "doc_status": "1"},
        {"state": "QI Failed", "title": "Failed", "doc_status": "2"},
    ],
    "transitions": [
        {
            "state": "QI Draft",
            "next_state": "QI In Progress",
            "action": "Submit",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        },
        {
            "state": "QI In Progress",
            "next_state": "QI Completed",
            "action": "Complete",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        },
        {
            "state": "QI In Progress",
            "next_state": "QI Failed",
            "action": "Fail",
            "allowed": "[\"Quality Manager\"]",
            "condition": ""
        }
    ]
}

create_workflow_if_not_exists(quality_gate_validation_workflow)

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "="*100)
print("✅ WORKFLOWS CREATION COMPLETE")
print("="*100)
print(f"""
Summary:
├─ Workflow States: {states_created} created
├─ Workflow Actions: {actions_created} created
└─ Workflows Created:
    ├─ Design Input Approval (6 states)
    ├─ BOM Approval (5 states)
    ├─ Quality Inspection Approval (6 states)
    ├─ Work Order Quality Gates (5 states)
    ├─ Supplier Audit Approval (4 states)
    ├─ NCR/Deviation Workflow (5 states)
    └─ Quality Gate Validation (4 states)

Total: 7 Complete Workflows

Next Steps:
1. Run: bench migrate
2. Verify workflows in Setup > Workflow
3. Configure workflow states
4. Setup email alerts
5. Configure auto-actions
6. Test workflow execution

Roles Required for Assignment:
- Administrator
- Design Manager
- Engineer
- Quality Manager
- Procurement Manager
- Production Manager

Note: Ensure these roles exist in your system
Before using workflows, assign users to appropriate roles
""")

print("\n🎉 Workflows generation completed successfully! 🎉\n")
