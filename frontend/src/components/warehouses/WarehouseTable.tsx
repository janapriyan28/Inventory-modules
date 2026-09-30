"use client";

import Badge from "@/components/ui/Badge";
import Button from "@/components/ui/Button";
import Table from "@/components/ui/Table";
import type { Warehouse } from "@/types/warehouse";

export default function WarehouseTable({
  warehouses,
  onEdit,
  onDelete,
}: {
  warehouses: Warehouse[];
  onEdit: (w: Warehouse) => void;
  onDelete: (w: Warehouse) => void;
}) {
  return (
    <Table
      rows={warehouses}
      empty="No warehouses yet. Add your first warehouse."
      columns={[
        { header: "Code", cell: (w) => <span className="font-mono">{w.code}</span> },
        { header: "Name", cell: (w) => w.name },
        { header: "Location", cell: (w) => w.location ?? "—" },
        { header: "Status", cell: (w) => <Badge tone={w.is_active ? "green" : "gray"}>{w.is_active ? "Active" : "Inactive"}</Badge> },
        {
          header: "",
          className: "text-right",
          cell: (w) => (
            <div className="flex justify-end gap-2">
              <Button variant="secondary" onClick={() => onEdit(w)}>Edit</Button>
              <Button variant="danger" onClick={() => onDelete(w)}>Delete</Button>
            </div>
          ),
        },
      ]}
    />
  );
}
