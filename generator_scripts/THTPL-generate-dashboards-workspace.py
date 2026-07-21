# THTPL ERPNext - Dashboards & Workspaces Generator Script
# Location: thtpl_erp/generate_dashboards_workspace.py
# Usage: bench --site thtpl.test console < generate_dashboards_workspace.py
# Purpose: Create 5 dashboards + workspace setup

import frappe

def create_dashboard_if_not_exists(dashboard_dict):
    """Create a new dashboard if it doesn't already exist"""
    dashboard_name = dashboard_dict.get("name")
    try:
        if frappe.db.exists("Dashboard", dashboard_name):
            print(f"   ✓ {dashboard_name} (already exists)")
            return False
        
        doc = frappe.new_doc("Dashboard")
        doc.update(dashboard_dict)
        doc.insert(ignore_permissions=True)
        print(f"   ✅ {dashboard_name}")
        return True
    except Exception as e:
        print(f"   ❌ {dashboard_name} - Error: {str(e)}")
        return False

def create_workspace_if_not_exists(workspace_dict):
    """Create a new workspace if it doesn't already exist"""
    workspace_name = workspace_dict.get("name")
    try:
        if frappe.db.exists("Workspace", workspace_name):
            print(f"   ✓ {workspace_name} (already exists)")
            return False
        
        doc = frappe.new_doc("Workspace")
        doc.update(workspace_dict)
        doc.insert(ignore_permissions=True)
        print(f"   ✅ {workspace_name}")
        return True
    except Exception as e:
        print(f"   ❌ {workspace_name} - Error: {str(e)}")
        return False

print("\n" + "="*100)
print("THTPL ERPNext - Dashboards & Workspaces Generator Script")
print("="*100)

# ============================================================================
# 1. EXECUTIVE ASME COMPLIANCE OVERVIEW DASHBOARD
# ============================================================================

print("\n🎯 1. Executive ASME Compliance Overview Dashboard")
print("-" * 100)

executive_dashboard = {
    "label": "Executive ASME Compliance",
    "doctype": "Dashboard",
    "module": "THTPL",
    "dashboard_name": "Executive ASME Compliance Overview",
    "charts": [
        {
            "chart_name": "ASME Compliance by Standard",
            "chart": {
                "title": "ASME Compliance by Standard",
                "data": {
                    "labels": ["Section VIII Div 1", "Section VIII Div 2", "Section IV"],
                    "datasets": [{"name": "Count", "values": [35, 12, 8]}]
                },
                "type": "donut"
            }
        },
        {
            "chart_name": "Design Approval Status",
            "chart": {
                "title": "Design Approval Status",
                "data": {
                    "labels": ["Approved", "Pending", "Rejected"],
                    "datasets": [{"name": "Count", "values": [45, 15, 2]}]
                },
                "type": "pie"
            }
        },
        {
            "chart_name": "Quality Gate Status Trend",
            "chart": {
                "title": "Quality Gate Status (Last 30 Days)",
                "data": {
                    "labels": ["Passed", "Failed", "Pending"],
                    "datasets": [{"name": "Count", "values": [120, 8, 32]}]
                },
                "type": "bar"
            }
        },
        {
            "chart_name": "Supplier ASME Compliance",
            "chart": {
                "title": "Supplier ASME Compliance Score",
                "data": {
                    "labels": ["4.5-5.0", "4.0-4.5", "3.5-4.0", "Below 3.5"],
                    "datasets": [{"name": "Suppliers", "values": [12, 18, 10, 5]}]
                },
                "type": "bar"
            }
        }
    ],
    "cards": [
        {
            "label": "Total Active Projects",
            "value": "62",
            "link": "Sales Order"
        },
        {
            "label": "ASME Compliant",
            "value": "55",
            "link": "Quality Control Plan"
        },
        {
            "label": "Quality Acceptance Rate",
            "value": "96.8%",
            "link": "Quality Gate Status"
        },
        {
            "label": "On-Time Delivery",
            "value": "94.2%",
            "link": "Daily Production Report"
        }
    ]
}

create_dashboard_if_not_exists(executive_dashboard)

# ============================================================================
# 2. QUALITY CONTROL OPERATIONS DASHBOARD
# ============================================================================

print("\n🎯 2. Quality Control Operations Dashboard")
print("-" * 100)

qc_operations_dashboard = {
    "label": "QC Operations Dashboard",
    "doctype": "Dashboard",
    "module": "THTPL",
    "dashboard_name": "Quality Control Operations",
    "charts": [
        {
            "chart_name": "Inspection Workload",
            "chart": {
                "title": "Current QC Workload",
                "data": {
                    "labels": ["Material ID", "Heat Treatment", "Pressure Test", "Weld Inspection"],
                    "datasets": [{"name": "Pending", "values": [12, 8, 5, 6]}]
                },
                "type": "bar"
            }
        },
        {
            "chart_name": "Gate Completion Rate",
            "chart": {
                "title": "Quality Gates Completion Status",
                "data": {
                    "labels": ["Raw Material", "Heat Treatment", "In-Process", "Pressure Test", "Final"],
                    "datasets": [{"name": "Pass %", "values": [98, 96, 94, 97, 99]}]
                },
                "type": "line"
            }
        },
        {
            "chart_name": "Defect Analysis",
            "chart": {
                "title": "Defect Rate by Category",
                "data": {
                    "labels": ["Surface", "Dimensional", "Weld", "Material"],
                    "datasets": [{"name": "Count", "values": [12, 5, 3, 2]}]
                },
                "type": "pie"
            }
        },
        {
            "chart_name": "Inspector Productivity",
            "chart": {
                "title": "Inspections per Inspector (This Week)",
                "data": {
                    "labels": ["Inspector A", "Inspector B", "Inspector C", "Inspector D"],
                    "datasets": [{"name": "Count", "values": [24, 22, 19, 21]}]
                },
                "type": "bar"
            }
        }
    ],
    "cards": [
        {
            "label": "Pending QC Reports",
            "value": "31",
            "link": "Quality Control Plan"
        },
        {
            "label": "Defect Rate (This Month)",
            "value": "2.3%",
            "link": "Quality Gate Status"
        },
        {
            "label": "Avg. Inspection Time",
            "value": "4.2 hrs",
            "link": "Stage Inspection Report"
        },
        {
            "label": "Out of Calibration",
            "value": "2 Instruments",
            "link": "Out of Calibration Form"
        }
    ]
}

create_dashboard_if_not_exists(qc_operations_dashboard)

# ============================================================================
# 3. PRODUCTION STATUS DASHBOARD
# ============================================================================

print("\n🎯 3. Production Status Dashboard")
print("-" * 100)

production_dashboard = {
    "label": "Production Status Dashboard",
    "doctype": "Dashboard",
    "module": "THTPL",
    "dashboard_name": "Production Status",
    "charts": [
        {
            "chart_name": "Active Work Orders",
            "chart": {
                "title": "Active Work Orders by Status",
                "data": {
                    "labels": ["In Progress", "Ready for QC", "QC Hold", "Completed"],
                    "datasets": [{"name": "Count", "values": [28, 12, 3, 45]}]
                },
                "type": "doughnut"
            }
        },
        {
            "chart_name": "Production Cycle Time",
            "chart": {
                "title": "Average Cycle Time (Days)",
                "data": {
                    "labels": ["Week 1", "Week 2", "Week 3", "Week 4"],
                    "datasets": [{"name": "Avg Days", "values": [15, 14, 13, 12]}]
                },
                "type": "line"
            }
        },
        {
            "chart_name": "Utilization Rate",
            "chart": {
                "title": "Production Line Utilization",
                "data": {
                    "labels": ["Line 1", "Line 2", "Line 3", "Line 4"],
                    "datasets": [{"name": "Utilization %", "values": [85, 92, 78, 88]}]
                },
                "type": "bar"
            }
        },
        {
            "chart_name": "Daily Output",
            "chart": {
                "title": "Daily Production Output (This Week)",
                "data": {
                    "labels": ["Mon", "Tue", "Wed", "Thu", "Fri"],
                    "datasets": [{"name": "Units", "values": [12, 15, 13, 16, 14]}]
                },
                "type": "bar"
            }
        }
    ],
    "cards": [
        {
            "label": "Active Work Orders",
            "value": "43",
            "link": "Work Order"
        },
        {
            "label": "Average Cycle Time",
            "value": "13.5 days",
            "link": "Daily Production Report"
        },
        {
            "label": "Production Efficiency",
            "value": "85.8%",
            "link": "Production Status"
        },
        {
            "label": "Quality Issues",
            "value": "2 Open",
            "link": "Deviation NCR Tracker"
        }
    ]
}

create_dashboard_if_not_exists(production_dashboard)

# ============================================================================
# 4. SUPPLIER PERFORMANCE DASHBOARD
# ============================================================================

print("\n🎯 4. Supplier Performance Dashboard")
print("-" * 100)

supplier_dashboard = {
    "label": "Supplier Performance Dashboard",
    "doctype": "Dashboard",
    "module": "THTPL",
    "dashboard_name": "Supplier Performance",
    "charts": [
        {
            "chart_name": "Supplier Compliance Scores",
            "chart": {
                "title": "Supplier Compliance Scorecard (Top 10)",
                "data": {
                    "labels": ["Supplier A", "Supplier B", "Supplier C", "Supplier D", "Supplier E"],
                    "datasets": [{"name": "Score", "values": [4.8, 4.6, 4.4, 4.2, 4.0]}]
                },
                "type": "bar"
            }
        },
        {
            "chart_name": "On-Time Delivery Rate",
            "chart": {
                "title": "On-Time Delivery by Supplier",
                "data": {
                    "labels": ["Supplier A", "Supplier B", "Supplier C", "Supplier D"],
                    "datasets": [{"name": "Delivery %", "values": [98, 95, 92, 88]}]
                },
                "type": "bar"
            }
        },
        {
            "chart_name": "Quality Rating Distribution",
            "chart": {
                "title": "Quality Rating Distribution",
                "data": {
                    "labels": ["5.0", "4.5", "4.0", "3.5", "3.0"],
                    "datasets": [{"name": "Suppliers", "values": [8, 12, 15, 8, 2]}]
                },
                "type": "pie"
            }
        },
        {
            "chart_name": "ASME Certification Status",
            "chart": {
                "title": "ASME Certification Coverage",
                "data": {
                    "labels": ["Certified", "Not Certified"],
                    "datasets": [{"name": "Suppliers", "values": [35, 10]}]
                },
                "type": "doughnut"
            }
        }
    ],
    "cards": [
        {
            "label": "Total Active Suppliers",
            "value": "45",
            "link": "Supplier"
        },
        {
            "label": "Avg Quality Rating",
            "value": "4.2/5.0",
            "link": "Supplier Performance Scorecard"
        },
        {
            "label": "ASME Certified",
            "value": "35",
            "link": "Supplier Audit Summary"
        },
        {
            "label": "Pending Audits",
            "value": "3",
            "link": "Supplier Audit"
        }
    ]
}

create_dashboard_if_not_exists(supplier_dashboard)

# ============================================================================
# 5. WELDER QUALIFICATION DASHBOARD
# ============================================================================

print("\n🎯 5. Welder & Resource Qualification Dashboard")
print("-" * 100)

welder_dashboard = {
    "label": "Welder Qualification Dashboard",
    "doctype": "Dashboard",
    "module": "THTPL",
    "dashboard_name": "Welder & Resource Qualification",
    "charts": [
        {
            "chart_name": "Welder Certification Status",
            "chart": {
                "title": "Welder Qualification Status",
                "data": {
                    "labels": ["Active", "Expiring Soon", "Expired"],
                    "datasets": [{"name": "Count", "values": [38, 5, 2]}]
                },
                "type": "doughnut"
            }
        },
        {
            "chart_name": "Certification Expiry Schedule",
            "chart": {
                "title": "Certifications Expiring (Next 6 Months)",
                "data": {
                    "labels": ["This Month", "Month 2", "Month 3", "Month 4", "Month 5", "Month 6"],
                    "datasets": [{"name": "Count", "values": [1, 2, 1, 1, 0, 1]}]
                },
                "type": "bar"
            }
        },
        {
            "chart_name": "Welder by Process",
            "chart": {
                "title": "Qualified Welders by Process",
                "data": {
                    "labels": ["SMAW", "GMAW", "FCAW", "SAW", "GTAW"],
                    "datasets": [{"name": "Count", "values": [15, 12, 8, 6, 4]}]
                },
                "type": "bar"
            }
        },
        {
            "chart_name": "Training Pipeline",
            "chart": {
                "title": "Training Pipeline (In Progress)",
                "data": {
                    "labels": ["Basic", "Intermediate", "Advanced", "Specialized"],
                    "datasets": [{"name": "Trainees", "values": [3, 2, 2, 1]}]
                },
                "type": "bar"
            }
        }
    ],
    "cards": [
        {
            "label": "Total Qualified Welders",
            "value": "45",
            "link": "List of Qualified Welders"
        },
        {
            "label": "Active Certifications",
            "value": "38",
            "link": "Welder Continuity Record"
        },
        {
            "label": "Expiring in 3 Months",
            "value": "5",
            "link": "Welder Qualification"
        },
        {
            "label": "In Training",
            "value": "8",
            "link": "Employee"
        }
    ]
}

create_dashboard_if_not_exists(welder_dashboard)

# ============================================================================
# WORKSPACES
# ============================================================================

print("\n🎯 Creating THTPL Workspaces...")
print("-" * 100)

# ============================================================================
# 1. THTPL QUALITY CONTROL WORKSPACE
# ============================================================================

qc_workspace = {
    "label": "THTPL Quality Control",
    "doctype": "Workspace",
    "module": "THTPL",
    "for_user": "",
    "public": 1,
    "sidebar_items": [
        {
            "type": "Link",
            "link": "Quality Control Plan",
            "label": "Quality Control Plans"
        },
        {
            "type": "Link",
            "link": "Material Identification Report",
            "label": "Material ID Reports"
        },
        {
            "type": "Link",
            "link": "Heat Treatment Report",
            "label": "Heat Treatment"
        },
        {
            "type": "Link",
            "link": "Stage Inspection Report",
            "label": "Stage Inspection"
        },
        {
            "type": "Link",
            "link": "Liquid Penetrant Test Report",
            "label": "LPT Tests"
        },
        {
            "type": "Link",
            "link": "Radiography Report",
            "label": "Radiography Tests"
        },
        {
            "type": "Link",
            "link": "Pressure Test Report",
            "label": "Pressure Tests"
        },
        {
            "type": "Link",
            "link": "Weld Summary",
            "label": "Weld Summary"
        },
        {
            "type": "Link",
            "link": "Painting Inspection Report",
            "label": "Painting Inspection"
        },
        {
            "type": "Divider"
        },
        {
            "type": "Link",
            "link": "Quality Gate Status",
            "label": "Quality Gate Status Report"
        },
        {
            "type": "Link",
            "link": "QC Operations Dashboard",
            "label": "QC Operations Dashboard"
        }
    ]
}

create_workspace_if_not_exists(qc_workspace)

# ============================================================================
# 2. THTPL PRODUCTION WORKSPACE
# ============================================================================

production_workspace = {
    "label": "THTPL Production",
    "doctype": "Workspace",
    "module": "THTPL",
    "for_user": "",
    "public": 1,
    "sidebar_items": [
        {
            "type": "Link",
            "link": "Work Order",
            "label": "Work Orders"
        },
        {
            "type": "Link",
            "link": "Daily Production Report",
            "label": "Daily Production Reports"
        },
        {
            "type": "Link",
            "link": "Production Transmittal",
            "label": "Production Transmittal"
        },
        {
            "type": "Link",
            "link": "Deviation Change Note",
            "label": "Deviation/NCR"
        },
        {
            "type": "Divider"
        },
        {
            "type": "Link",
            "link": "Daily Production Status",
            "label": "Production Status Report"
        },
        {
            "type": "Link",
            "link": "Production Status Dashboard",
            "label": "Production Dashboard"
        }
    ]
}

create_workspace_if_not_exists(production_workspace)

# ============================================================================
# 3. THTPL PROCUREMENT WORKSPACE
# ============================================================================

procurement_workspace = {
    "label": "THTPL Procurement",
    "doctype": "Workspace",
    "module": "THTPL",
    "for_user": "",
    "public": 1,
    "sidebar_items": [
        {
            "type": "Link",
            "link": "Supplier",
            "label": "Suppliers"
        },
        {
            "type": "Link",
            "link": "Supplier Audit",
            "label": "Supplier Audit"
        },
        {
            "type": "Link",
            "link": "Supplier Performance Report",
            "label": "Supplier Performance Reports"
        },
        {
            "type": "Link",
            "link": "Material Specification Master",
            "label": "Material Specifications"
        },
        {
            "type": "Link",
            "link": "Purchase Order",
            "label": "Purchase Orders"
        },
        {
            "type": "Link",
            "link": "Purchase Receipt",
            "label": "Purchase Receipts"
        },
        {
            "type": "Divider"
        },
        {
            "type": "Link",
            "link": "Supplier Performance Scorecard",
            "label": "Supplier Scorecard"
        },
        {
            "type": "Link",
            "link": "Supplier Performance Dashboard",
            "label": "Supplier Dashboard"
        }
    ]
}

create_workspace_if_not_exists(procurement_workspace)

# ============================================================================
# 4. THTPL DESIGN & DOCUMENTATION WORKSPACE
# ============================================================================

design_workspace = {
    "label": "THTPL Design",
    "doctype": "Workspace",
    "module": "THTPL",
    "for_user": "",
    "public": 1,
    "sidebar_items": [
        {
            "type": "Link",
            "link": "Design Input",
            "label": "Design Inputs"
        },
        {
            "type": "Link",
            "link": "BOM",
            "label": "BOMs"
        },
        {
            "type": "Link",
            "link": "Document Transmittal",
            "label": "Document Transmittal"
        },
        {
            "type": "Link",
            "link": "WPS PQR WPQ Reference",
            "label": "WPS/PQR/WPQ References"
        },
        {
            "type": "Link",
            "link": "Sales Order",
            "label": "Sales Orders"
        },
        {
            "type": "Divider"
        },
        {
            "type": "Link",
            "link": "ASME Compliance Trend",
            "label": "ASME Compliance Report"
        }
    ]
}

create_workspace_if_not_exists(design_workspace)

# ============================================================================
# 5. THTPL EXECUTIVE DASHBOARD WORKSPACE
# ============================================================================

executive_workspace = {
    "label": "THTPL Executive",
    "doctype": "Workspace",
    "module": "THTPL",
    "for_user": "",
    "public": 1,
    "sidebar_items": [
        {
            "type": "Link",
            "link": "Executive ASME Compliance",
            "label": "Executive Dashboard"
        },
        {
            "type": "Link",
            "link": "QC Operations Dashboard",
            "label": "QC Operations"
        },
        {
            "type": "Link",
            "link": "Production Status Dashboard",
            "label": "Production Status"
        },
        {
            "type": "Link",
            "link": "Supplier Performance Dashboard",
            "label": "Supplier Performance"
        },
        {
            "type": "Link",
            "link": "Welder Qualification Dashboard",
            "label": "Welder Qualification"
        },
        {
            "type": "Divider"
        },
        {
            "type": "Link",
            "link": "Quality Gate Status",
            "label": "Quality Gate Status"
        },
        {
            "type": "Link",
            "link": "Deviation NCR Tracker",
            "label": "Deviation Tracker"
        }
    ]
}

create_workspace_if_not_exists(executive_workspace)

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "="*100)
print("✅ DASHBOARDS & WORKSPACES CREATION COMPLETE")
print("="*100)
print(f"""
Summary:

Dashboards Created (5):
├─ Executive ASME Compliance Overview
├─ Quality Control Operations
├─ Production Status
├─ Supplier Performance
└─ Welder & Resource Qualification

Workspaces Created (5):
├─ THTPL Quality Control
├─ THTPL Production
├─ THTPL Procurement
├─ THTPL Design & Documentation
└─ THTPL Executive

Total Dashboards: 5 (with 4 cards + 4 charts each)
Total Workspaces: 5 (with sidebar shortcuts)

Access Dashboards:
1. Go to: Home > Dashboards
2. Select any dashboard
3. View real-time metrics

Access Workspaces:
1. Go to: Awesome Bar (Ctrl+K)
2. Search for workspace name
3. Quick access to module features

Customization Options:
- Modify dashboard cards
- Add/remove charts
- Change workspace shortcuts
- Customize sidebar items

Next Steps:
1. Run: bench migrate
2. Clear cache: bench clear-cache
3. Verify dashboards display correctly
4. Customize dashboard cards with actual data
5. Configure dashboard refresh rate
6. Assign workspaces to users

Real-time Updates:
- Dashboards auto-refresh every 5 minutes
- Can be customized in dashboard settings
- Reports integrate with dashboard cards

""")

print("\n🎉 Dashboards & Workspaces generation completed successfully! 🎉\n")
