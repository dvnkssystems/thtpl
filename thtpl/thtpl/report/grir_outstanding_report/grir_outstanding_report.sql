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