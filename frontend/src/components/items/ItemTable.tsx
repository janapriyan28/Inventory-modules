"use client";

import Badge from "@/components/ui/Badge";
import Button from "@/components/ui/Button";
import Table from "@/components/ui/Table";
import type { Item } from "@/types/item";

const priceFormatter = new Intl.NumberFormat("en-IN", {
  style: "currency",
  currency: "INR",
  minimumFractionDigits: 2,
  maximumFractionDigits: 2,
});

export default function ItemTable({
  items,
  onEdit,
  onDelete,
}: {
  items: Item[];
  onEdit: (item: Item) => void;
  onDelete: (item: Item) => void;
}) {
  return (
    <Table
      rows={items}
      empty="No items yet. Add your first item."
      columns={[
        { header: "Product ID", cell: (i) => <span className="font-mono">{i.product_id}</span> },
        { header: "Product Name", cell: (i) => i.name },
        { header: "Fabric Type", cell: (i) => i.fabric_type },
        { header: "Price (INR)", cell: (i) => priceFormatter.format(Number(i.price_inr)) },
        { header: "Unit", cell: (i) => i.unit },
        { header: "Reorder level", cell: (i) => i.reorder_level },
        { header: "Status", cell: (i) => <Badge tone={i.is_active ? "green" : "gray"}>{i.is_active ? "Active" : "Inactive"}</Badge> },
        {
          header: "",
          className: "text-right",
          cell: (i) => (
            <div className="flex justify-end gap-2">
              <Button variant="secondary" onClick={() => onEdit(i)}>Edit</Button>
              <Button variant="danger" onClick={() => onDelete(i)}>Delete</Button>
            </div>
          ),
        },
      ]}
    />
  );
}
