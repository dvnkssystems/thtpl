import frappe
import json

def create_chart_if_not_exists(chart_name, doctype, chart_type="Group By", group_by="status", filters=None):
    if frappe.db.exists("Dashboard Chart", chart_name):
        print(f"   ✓ {chart_name} (exists)")
        return chart_name
    
    try:
        chart = frappe.new_doc("Dashboard Chart")
        chart.chart_name = chart_name
        chart.document_type = doctype
        chart.chart_type = chart_type # "Group By" is best for Status/Category charts
        chart.group_by = group_by
        chart.aggregate_function = "Count"
        chart.timeseries = 0
        chart.width = "Half"
        
        # Even if timeseries is 0, Frappe v15 validation sometimes checks this
        # if the chart_type is Count/Sum/etc. instead of "Group By"
        chart.based_on = "creation" 
        
        chart.filters_json = json.dumps(filters or {})
        chart.insert(ignore_permissions=True)
        print(f"   ✅ {chart_name}")
        return chart.name
    except Exception as e:
        print(f"   ❌ {chart_name} - {str(e)}")
        return None

def create_dashboard_if_not_exists(dashboard_name, chart_names):
    # Filter out None values from failed charts
    valid_charts = [c for c in chart_names if c]
    if not valid_charts:
        print(f"   ⚠️ Skipping {dashboard_name} - No valid charts")
        return

    if frappe.db.exists("Dashboard", dashboard_name):
        doc = frappe.get_doc("Dashboard", dashboard_name)
        doc.charts = []
        print(f"   ✓ {dashboard_name} (updating)")
    else:
        doc = frappe.new_doc("Dashboard")
        doc.dashboard_name = dashboard_name
        print(f"   ✅ {dashboard_name}")

    for name in valid_charts:
        doc.append("charts", {"chart": name, "width": "Half"})
    
    doc.save(ignore_permissions=True)

def create_workspace_if_not_exists(title, icon, label, links=None, shortcuts=None, charts=None):
    if frappe.db.exists("Workspace", title):
        doc = frappe.get_doc("Workspace", title)
        doc.links = []
        doc.shortcuts = []
        doc.charts = []
        print(f"   ✓ {title} (updating)")
    else:
        doc = frappe.new_doc("Workspace")
        doc.title = title
        doc.icon = icon
        doc.label = label
        doc.public = 1
        doc.module = "THTPL"
        print(f"   ✅ {title}")

    if links:
        for link in links:
            doc.append("links", {
                "link_to": link.get("name"),
                "link_type": link.get("type", "DocType"),
                "label": link.get("label", link.get("name")),
                "type": "Link",
                "onboard": 0
            })

    if shortcuts:
        for sc in shortcuts:
            doc.append("shortcuts", {
                "label": sc.get("label"),
                "link_to": sc.get("name"),
                "type": "DocType",
                "stats_filter": sc.get("filter")
            })

    if charts:
        valid_charts = [c for c in charts if c]
        for chart in valid_charts:
            doc.append("charts", {"chart": chart, "width": "Half"})

    doc.save(ignore_permissions=True)

def run():
    print("\n" + "="*80)
    print("THTPL ERPNext - Dashboards & Workspaces Generator v3")
    print("="*80)

    # 1. Create Dashboard Charts
    print("\n🎯 Creating Dashboard Charts...")
    c1 = create_chart_if_not_exists("ASME Compliance Items", "Item", group_by="asme_standard", filters={"asme_compliance_required": 1})
    c2 = create_chart_if_not_exists("QC Inspection Status", "Quality Inspection", group_by="status")
    c3 = create_chart_if_not_exists("Work Order Progress", "Work Order", group_by="status")
    c4 = create_chart_if_not_exists("Supplier Audit Pipeline", "Supplier Audit", group_by="status")
    c5 = create_chart_if_not_exists("Skills Inventory", "Employee Skill Map", group_by="skill")

    # 2. Create Dashboards
    print("\n🎯 Creating Dashboards...")
    create_dashboard_if_not_exists("THTPL Executive Dashboard", [c1, c3])
    create_dashboard_if_not_exists("THTPL Quality Dashboard", [c2, c4])

    # 3. Create Workspaces
    print("\n🎯 Creating Workspaces...")
    
    create_workspace_if_not_exists(
        "Quality Control", "check", "Quality Control",
        links=[
            {"name": "Quality Inspection", "label": "Inspections"},
            {"name": "Material Identification Report", "label": "Material ID Docs"}
        ],
        shortcuts=[
            {"label": "Draft Inspections", "name": "Quality Inspection", "filter": '{"status": "Draft"}'}
        ],
        charts=[c2]
    )

    create_workspace_if_not_exists(
        "Production", "package", "Production",
        links=[{"name": "Work Order", "label": "Work Orders"}],
        charts=[c3]
    )

    print("\n" + "="*80)
    print("✅ Configuration complete. Please check the Workspaces module.")
    print("="*80)

if __name__ == "__main__":
    run()
