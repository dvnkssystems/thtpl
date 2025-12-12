-- Example SQL for Batch Expiry Report
        SELECT
            b.name AS "Batch ID",
            b.item_code AS "Item Code:Link/Item",
            i.item_name AS "Item Name",
            b.expiry_date AS "Expiry Date:Date",
            b.batch_qty AS "Batch Quantity",
            sle.warehouse AS "Warehouse:Link/Warehouse"
        FROM
            `tabBatch` b
        JOIN
            `tabItem` i ON b.item_code = i.item_code
        LEFT JOIN
            `tabStock Ledger Entry` sle ON b.name = sle.batch_no AND b.item_code = sle.item_code
        WHERE
            b.expiry_date IS NOT NULL
            AND b.expiry_date <= CURDATE() + INTERVAL 30 DAY -- Expiring within 30 days or already expired
        GROUP BY
            b.name, sle.warehouse
        ORDER BY
            b.expiry_date ASC;