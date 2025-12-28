# THTPL ERPNext - Complete DocType Generation Script
# This script generates all 24+ custom doctypes for THTPL

## Installation Instructions

### Step 1: Copy this entire structure to your Frappe app

```
thtpl_erp/
├── doctype/
│   ├── quality_control_plan/
│   │   ├── quality_control_plan.json
│   │   ├── quality_control_plan.py
│   │   └── __init__.py
│   ├── material_identification_report/
│   ├── heat_treatment_report/
│   ├── ... (all 24+ doctypes)
│   └── __init__.py
├── generate_doctypes.py  (Main script)
└── README.md
```

### Step 2: Run the generation script

```bash
cd /path/to/frappe-bench
bench --site thtpl.test console < thtpl_erp/generate_doctypes.py
```

### Step 3: Or run bench migrate

```bash
bench migrate thtpl.test
```

---

## How to Use This Approach

### Option A: Auto-Generate Using Python Script

The `generate_doctypes.py` file (provided separately) will:
1. Read all doctype JSON files
2. Create them in the database
3. Create child tables
4. Add custom fields to standard doctypes
5. Generate workflow configurations

### Option B: Manual DocType Creation (If needed)

If you prefer to manually create doctypes:
1. Use Frappe UI: Setup → Customize Form → New Doctype
2. Copy the JSON from each doctype file
3. Use "Duplicate" to create child tables

### Option C: Use Bench Commands

```bash
# Individual doctype creation
bench make-doctype quality_control_plan
bench make-doctype material_identification_report
... (repeat for all)
```

---

## File Organization

All doctype definitions are provided in separate files below, organized by category:

**QC Module (11 Doctypes):**
- quality_control_plan.json
- material_identification_report.json
- heat_treatment_report.json
- stage_inspection_report.json
- liquid_penetrant_test_report.json
- radiography_report.json
- pressure_test_report.json
- weld_summary.json
- painting_inspection_report.json
- instrument_calibration_list.json
- out_of_calibration_form.json

**Design Module (2 Doctypes):**
- design_input.json
- document_transmittal.json

**Production Module (2 Doctypes):**
- daily_production_report.json
- production_transmittal.json

**Procurement Module (2 Doctypes):**
- supplier_performance_report.json
- supplier_audit.json

**Master Data (2 Doctypes):**
- material_specification_master.json
- deviation_change_note.json

**Support Tables:**
- qcp_inspection_activity.json
- mir_material_item.json
- lpt_testing_detail.json
- transmittal_recipient.json
- design_parameter.json
- design_revision.json

---

## Next: See individual files below for JSON definitions
