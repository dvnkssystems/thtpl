import frappe
import json



# ----------------------------------------------------------------------
# Chart
# ----------------------------------------------------------------------

def create_chart(title, chart_type, labels, values):
    try:
        existing = frappe.db.get_value(
            "Dashboard Chart",
            {"chart_name": title, "type": chart_type},
            "name"
        )

        if existing:
            print(f"✅ Chart exists: {title}")
            return existing

        chart = frappe.get_doc({
            "doctype": "Dashboard Chart",
            "chart_name": title,
            "type": chart_type,
            "data": json.dumps({
                "labels": labels,
                "datasets": [{"name": "Count", "values": values}]
            }),
            "is_standard": 0
        })

        chart.insert(ignore_permissions=True)
        print(f"✅ Chart created: {title}")
        return chart.name

    except Exception as e:
        print(f"❌{title} - {e}")
        return None

# ----------------------------------------------------------------------
# Dashboard (FIXED dashboard_charts)
# ----------------------------------------------------------------------

def create_dashboard(title, chart_refs):
    try:
        existing = frappe.db.get_value(
            "Dashboard",
            {"dashboard_name": title},
            "name"
        )

        if existing:
            print(f"✅ Dashboard exists: {title}")
            return existing

        dashboard = frappe.get_doc({
            "doctype": "Dashboard",
            "dashboard_name": title,
            "dashboard_charts": [
                {"chart": c, "width": "Half"}
                for c in chart_refs if c
            ],
            "is_standard": 0
        })

        dashboard.insert(ignore_permissions=True)
        print(f"✅ Dashboard created: {title}")
        return dashboard.name

    except Exception as e:
        print(f"❌{title} - {e}")
        return None

# ----------------------------------------------------------------------
# Workspace (VALID MODULES ONLY)
# ----------------------------------------------------------------------

def create_workspace(name, title, module, icon="chart"):
    try:
        if frappe.db.exists("Workspace", name):
            print(f"✅ Workspace exists: {title}")
            return name

        workspace = frappe.get_doc({
            "doctype": "Workspace",
            "name": name,
            "title": title,
            "label": title,
            "module": module,
            "icon": icon,
            "public": 1,
            "content": "[]",
            "is_standard": 0
        })

        workspace.insert(ignore_permissions=True)
        print(f"✅ Workspace created: {title}")
        return name

    except Exception as e:
        print(f"❌{title} - {e}")
        return None

# ----------------------------------------------------------------------
# RUN
# ----------------------------------------------------------------------

print("\n🎯 Creating Dashboards\n" + "-" * 80)

create_dashboard(
    "Executive ASME Compliance Overview",
    [create_chart(
        "ASME Compliance by Standard",
        "Donut",
        ["Section VIII Div 1", "Section VIII Div 2", "Section IV"],
        [35, 12, 8]
    )]
)

create_dashboard(
    "Quality Control Operations",
    [create_chart(
        "Current QC Workload",
        "Bar",
        ["Material ID", "Heat Treatment", "Pressure Test", "Weld Inspection"],
        [12, 8, 5, 6]
    )]
)

create_dashboard(
    "Production Status",
    [create_chart(
        "Active Work Orders by Status",
        "Donut",
        ["In Progress", "Ready for QC", "QC Hold", "Completed"],
        [28, 12, 3, 45]
    )]
)

create_dashboard(
    "Supplier Performance",
    [create_chart(
        "Supplier Compliance Scorecard (Top 10)",
        "Bar",
        ["Supplier A", "Supplier B", "Supplier C", "Supplier D", "Supplier E"],
        [4.8, 4.6, 4.4, 4.2, 4.0]
    )]
)

create_dashboard(
    "Welder & Resource Qualification",
    [create_chart(
        "Welder Qualification Status",
        "Donut",
        ["Active", "Expiring Soon", "Expired"],
        [38, 5, 2]
    )]
)

print("\n🎯 Creating Workspaces\n" + "-" * 80)

create_workspace("THTPL Quality Control", "THTPL Quality Control", "Quality Management")
create_workspace("THTPL Production", "THTPL Production", "Manufacturing")
create_workspace("THTPL Procurement", "THTPL Procurement", "Buying")
create_workspace("THTPL Design & Documentation", "THTPL Design & Documentation", "Manufacturing")
create_workspace("THTPL Executive", "THTPL Executive", "Projects")

frappe.db.commit()

print("\n🎉 Dashboards & Workspaces generation completed successfully!\n")
