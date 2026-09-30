"use client";

import Table from "@/components/ui/Table";
import { formatDate } from "@/lib/utils";
import type { StockIn } from "@/types/stock-in";

export default function StockInTable({ entries }: { entries: StockIn[] }) {
  return (
    <Table
      rows={entries}
      empty="No stock in entries yet."
      columns={[
        { header: "Date", cell: (e) => formatDate(e.created_at) },
        { header: "Item", cell: (e) => <>{e.item_name} <span className="font-mono text-xs text-slate-400">{e.item_product_id}</span></> },
        { header: "Warehouse", cell: (e) => e.warehouse_name },
        { header: "Quantity", cell: (e) => e.quantity, className: "font-medium" },
        { header: "Reference", cell: (e) => e.reference ?? "—" },
        { header: "Remarks", cell: (e) => e.remarks ?? "—" },
      ]}
    />
  );
}
