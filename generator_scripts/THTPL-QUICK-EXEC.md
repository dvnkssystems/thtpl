# THTPL ERPNext - Quick Execution Guide

## 🚀 One-Time Setup

This guide shows exactly what commands to run to set up the complete THTPL system.

---

## Prerequisites Check

```bash
# Verify Frappe is installed
which bench
# Should output: /usr/local/bin/bench

# Check Python version
python --version
# Should be: Python 3.7 or higher

# List all sites
bench list-apps
# Should show: frappe, erpnext, and others
```

---

## Step 1: Download All Scripts

Place these 4 files in your Frappe bench root directory:

```bash
# Navigate to your Frappe bench root
cd /path/to/frappe-bench

# List files (should see these 4 files)
ls -la THTPL*.py THTPL*.md
```

**Files needed:**
- ✅ THTPL-generate-doctypes.py
- ✅ THTPL-generate-doctypes-part2.py
- ✅ THTPL-generate-custom-fields.py
- ✅ THTPL-README.md
- ✅ THTPL-COMPLETE-SUMMARY.md

---

## Step 2: Start Frappe (Terminal 1)

```bash
cd /path/to/frappe-bench

# Start Frappe bench
bench start

# You should see output like:
# Starting Frappe server...
# Listen on: 127.0.0.1:8000
```

Keep this terminal running. **DO NOT CLOSE IT.**

---

## Step 3: Execute DocTypes Part 1 (Terminal 2)

Open a NEW terminal window and run:

```bash
cd /path/to/frappe-bench

# Execute Part 1 DocTypes
bench --site thtpl.test console < THTPL-generate-doctypes.py
```

**Expected output (takes ~2-3 minutes):**
```
════════════════════════════════════════════════════════════════════════════════
THTPL ERPNext - Complete DocTypes Generator Script
════════════════════════════════════════════════════════════════════════════════

🎯 1. Quality Control Plan (THTPL/QC/QCP)
   ✅ Quality Control Plan

🎯 2. QC Plan Gate (Child Table)
   ✅ QC Plan Gate

🎯 3. QC Testing Type (Child Table)
   ✅ QC Testing Type

... [continues for all 23 doctypes]

════════════════════════════════════════════════════════════════════════════════
✅ DOCTYPE CREATION COMPLETE
════════════════════════════════════════════════════════════════════════════════
```

**Verify it completed successfully:**
```bash
# Check for "DOCTYPE CREATION COMPLETE" message
# If you see ❌ errors, note them down
```

---

## Step 4: Execute DocTypes Part 2 (Terminal 2)

In the same terminal, run:

```bash
# Execute Part 2 DocTypes
bench --site thtpl.test console < THTPL-generate-doctypes-part2.py
```

**Expected output (takes ~2-3 minutes):**
```
════════════════════════════════════════════════════════════════════════════════
THTPL ERPNext - Additional DocTypes Generator (Part 2)
════════════════════════════════════════════════════════════════════════════════

🎯 DESIGN & DOCUMENTATION DOCTYPES

🎯 1. Design Input (THTPL/DAD/DI)
   ✅ Design Input

... [continues for Design, Production, Procurement, Quality modules]

════════════════════════════════════════════════════════════════════════════════
✅ ADDITIONAL DOCTYPES CREATION COMPLETE (PART 2)
════════════════════════════════════════════════════════════════════════════════
```

---

## Step 5: Execute Custom Fields (Terminal 2)

In the same terminal, run:

```bash
# Execute Custom Fields
bench --site thtpl.test console < THTPL-generate-custom-fields.py
```

**Expected output (takes ~3-5 minutes):**
```
════════════════════════════════════════════════════════════════════════════════
THTPL ERPNext - Custom Fields Generation Script
════════════════════════════════════════════════════════════════════════════════

🎯 PHASE 1: Sales Order Custom Fields (19 fields)
   ✅ order_acceptance_number
   ✅ thtpl_design_manager
   ✅ design_input_reference

🎯 PHASE 2: Item Custom Fields (13 fields)
   ✅ thtpl_asme_compliance

... [continues for all 158+ fields]

════════════════════════════════════════════════════════════════════════════════
✅ CUSTOM FIELDS GENERATION COMPLETE
════════════════════════════════════════════════════════════════════════════════
```

---

## Step 6: Database Migration (Terminal 2)

```bash
# Migrate database
bench migrate

# Clear cache
bench clear-cache

# Build assets
bench build --force

# Expected output:
# ✓ Executed 0 migrations
# Clearing cache
# Building assets...
```

---

## Step 7: Verification (Terminal 2)

```bash
# Open Frappe console
bench --site thtpl.test console

# In the console (frappe> prompt), run:
frappe> frappe.db.count("DocType", {"module": "THTPL"})
# Expected: Should be 46 or higher

frappe> len(frappe.db.get_list("Custom Field"))
# Expected: Should be 158 or higher

# Check a specific doctype
frappe> doc = frappe.get_doc("DocType", "Quality Control Plan")
frappe> print(f"Quality Control Plan has {len(doc.fields)} fields")

# Exit console
frappe> exit()
```

---

## Step 8: UI Verification

1. **Open browser**: http://localhost:8000
2. **Login**: Administrator / your-password
3. **Go to**: Setup > DocType
4. **Search**: "Quality Control Plan"
5. **Verify**: Should see THTPL-QC-QCP in the list

**Check custom fields:**
1. Go to: Selling > Sales Order
2. Create new or edit existing Sales Order
3. Scroll down to see THTPL fields like:
   - Order Acceptance Number
   - THTPL Design Manager
   - ASME Compliance
   - etc.

---

## ✅ Complete Checklist

Mark these as you complete them:

### Pre-Execution (5 min)
- [ ] All 4 THTPL files downloaded
- [ ] Files placed in frappe-bench root
- [ ] Frappe bench working (`bench --version`)
- [ ] Site exists (`bench list-sites`)

### Part 1 DocTypes Execution (3 min)
- [ ] Script started without errors
- [ ] "DOCTYPE CREATION COMPLETE" message appears
- [ ] No red ❌ errors in output

### Part 2 DocTypes Execution (3 min)
- [ ] Script started without errors
- [ ] "ADDITIONAL DOCTYPES CREATION COMPLETE" message appears
- [ ] No red ❌ errors in output

### Custom Fields Execution (5 min)
- [ ] Script started without errors
- [ ] "CUSTOM FIELDS GENERATION COMPLETE" message appears
- [ ] No red ❌ errors in output

### Database Migration (2 min)
- [ ] `bench migrate` completed successfully
- [ ] `bench clear-cache` completed
- [ ] `bench build --force` completed

### Verification (5 min)
- [ ] DocType count > 46
- [ ] Custom Field count > 158
- [ ] "Quality Control Plan" doctype exists
- [ ] Sales Order shows new THTPL fields in UI

### Success! 🎉
- [ ] All steps completed
- [ ] No errors encountered
- [ ] System ready for workflow setup

---

## ⏱️ Total Execution Time

| Step | Duration |
|------|----------|
| Step 1: Download | 1 min |
| Step 2: Start Frappe | 1 min |
| Step 3: Part 1 DocTypes | 3 min |
| Step 4: Part 2 DocTypes | 3 min |
| Step 5: Custom Fields | 5 min |
| Step 6: Database Migration | 2 min |
| Step 7: Verification | 5 min |
| **TOTAL** | **~20 minutes** |

---

## 🆘 If Something Goes Wrong

### Issue 1: Command not found

```bash
# Error: bench: command not found

# Solution: Add to PATH
export PATH="/usr/local/bin:$PATH"

# Verify
which bench
```

### Issue 2: Site not found

```bash
# Error: Site not found: thtpl.test

# Solution: Check site name
bench list-sites

# Create if missing
bench new-site thtpl.test
```

### Issue 3: ERPNext not installed

```bash
# Error: Module erpnext not found

# Solution: Install ERPNext
bench --site thtpl.test install-app erpnext
bench migrate
```

### Issue 4: Custom field already exists

```bash
# This is OK - script will skip it
# Output: ✓ field_name (already exists)

# Just continue to next script
```

### Issue 5: Database locked

```bash
# Error: Database is locked

# Solution: Restart Frappe in Terminal 1
# Press Ctrl+C to stop
# Then run: bench start
```

---

## 🔍 Detailed Verification

### Verify DocTypes Created

```bash
bench --site thtpl.test console

# Count all THTPL doctypes
frappe> all_thtpl_docs = frappe.db.get_list(
...     "DocType", 
...     {"module": "THTPL"}, 
...     as_list=False
... )
frappe> print(f"Total THTPL DocTypes: {len(all_thtpl_docs)}")

# List them
frappe> for doc in all_thtpl_docs:
...     print(f"  - {doc.name}")

frappe> exit()
```

### Verify Custom Fields Created

```bash
bench --site thtpl.test console

# Count custom fields on Sales Order
frappe> so_fields = frappe.db.get_list(
...     "Custom Field", 
...     {"dt": "Sales Order"}, 
...     as_list=False
... )
frappe> print(f"Sales Order custom fields: {len(so_fields)}")

# List them
frappe> for field in so_fields:
...     print(f"  - {field.fieldname} ({field.fieldtype})")

frappe> exit()
```

### Test DocType Functionality

```bash
bench --site thtpl.test console

# Try creating a Quality Control Plan
frappe> qcp = frappe.new_doc("Quality Control Plan")
frappe> qcp.qcp_title = "Test QCP"
frappe> qcp.sales_order_reference = "SO-..." # (if exists)
frappe> print(qcp)

frappe> exit()
```

---

## 📚 Next Phase

After successful execution, you're ready for:

1. **Workflows** (Phase 2)
   - Design Input Approval
   - BOM Approval
   - Quality Inspection Approval
   - Work Order Quality Gates
   - Supplier Audit Approval
   - NCR/Deviation Workflow
   - Quality Gate Validation

2. **Email Alerts** (Phase 2)
   - Design Input Rejection
   - BOM Approved notification
   - Quality Gate Failed alerts
   - Pressure Test results
   - Calibration due reminders
   - Welder expiry warnings
   - NCR/Deviation creation

3. **Dashboards** (Phase 4)
   - Executive ASME Compliance
   - Quality Control Operations
   - Production Status
   - Supplier Performance
   - Welder Qualification

4. **Reports** (Phase 4)
   - Quality Gate Status
   - ASME Compliance Trends
   - Welder Qualification
   - Supplier Performance

---

## 📞 Quick Help

### Getting Current Status

```bash
# Check system information
frappe> frappe.db.count("DocType", {"module": "THTPL"})

# Check specific doctype
frappe> frappe.get_doc("DocType", "Quality Control Plan")

# Check field
frappe> frappe.get_doc("Custom Field", 
...     {"dt": "Sales Order", "fieldname": "order_acceptance_number"}
... )
```

### Common Queries

```bash
# List all THTPL child tables
frappe> frappe.db.get_list(
...     "DocType", 
...     {"module": "THTPL", "istable": 1}
... )

# Find custom fields on specific doctype
frappe> frappe.db.get_list(
...     "Custom Field",
...     {"dt": "Work Order"},
...     ["fieldname", "fieldtype", "label"]
... )

# Check field on specific doctype
frappe> frappe.db.get_value(
...     "Custom Field",
...     {"dt": "Item", "fieldname": "design_pressure_value"}
... )
```

---

## 🎯 Success Indicators

You'll know it's working when:

✅ All scripts run without error  
✅ No red ❌ marks in output  
✅ Database migration completes  
✅ `frappe.db.count()` returns 46+  
✅ Custom fields visible in UI  
✅ Can create new Quality Control Plans  
✅ Sales Order shows THTPL fields  
✅ No JavaScript errors in browser  

---

## 🚀 Ready to Go!

You're now ready to:

1. ✅ Create Quality Control Plans
2. ✅ Generate Material ID Reports
3. ✅ Track Heat Treatment
4. ✅ Perform Stage Inspections
5. ✅ Create Pressure Test Reports
6. ✅ Manage Welder Qualifications
7. ✅ Track Instrument Calibration
8. ✅ Manage Supplier Audits
9. ✅ Generate Production Reports
10. ✅ Track Deviations & NCRs

---

## 📋 Keep This Handy

Save this document as reference for:
- Initial setup troubleshooting
- Verification steps
- Common commands
- Next phase planning

---

**Time to execute: ~20 minutes**  
**Status: Ready to start**  
**Questions? Check THTPL-README.md**

🎉 **Let's build THTPL ASME Compliance System!** 🎉
