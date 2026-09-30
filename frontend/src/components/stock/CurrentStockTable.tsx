"use client";

import Badge from "@/components/ui/Badge";
import Table from "@/components/ui/Table";
import type { CurrentStockRow } from "@/types/current-stock";

export default function CurrentStockTable({ rows }: { rows: CurrentStockRow[] }) {
  return (
    <Table
      rows={rows}
      rowKey={(r) => `${r.item_id}-${r.warehouse_id}`}
      empty="No stock on hand yet. Record a stock-in first."
      columns={[
        { header: "Product ID", cell: (r) => <span className="font-mono">{r.product_id}</span> },
        { header: "Product Name", cell: (r) => r.item_name },
        { header: "Warehouse", cell: (r) => r.warehouse_name },
        { header: "Quantity", cell: (r) => `${r.quantity} ${r.unit}`, className: "font-medium" },
        { header: "Reorder level", cell: (r) => r.reorder_level },
        { header: "Status", cell: (r) => <Badge tone={r.is_low ? "red" : "green"}>{r.is_low ? "Low stock" : "OK"}</Badge> },
      ]}
    />
  );
}
