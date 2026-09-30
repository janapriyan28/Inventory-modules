"use client";

import { useState } from "react";
import Button from "@/components/ui/Button";
import Input from "@/components/ui/Input";
import Select from "@/components/ui/Select";
import { useItems } from "@/hooks/useItems";
import { useWarehouses } from "@/hooks/useWarehouses";
import { useCreateStockOut } from "@/hooks/useStockOut";

export default function StockOutForm() {
  const { data: items = [] } = useItems();
  const { data: warehouses = [] } = useWarehouses();
  const create = useCreateStockOut();
  const [itemId, setItemId] = useState("");
  const [warehouseId, setWarehouseId] = useState("");
  const [quantity, setQuantity] = useState("");
  const [reference, setReference] = useState("");
  const [remarks, setRemarks] = useState("");

  return (
    <form
      className="mb-6 grid gap-3 rounded-lg border border-slate-200 bg-white p-4 md:grid-cols-6"
      onSubmit={(e) => {
        e.preventDefault();
        create.mutate(
          {
            item_id: Number(itemId),
            warehouse_id: Number(warehouseId),
            quantity: Number(quantity),
            reference: reference.trim() || null,
            remarks: remarks.trim() || null,
          },
          {
            onSuccess: () => {
              setQuantity("");
              setReference("");
              setRemarks("");
            },
          }
        );
      }}
    >
      <Select label="Item" value={itemId} onChange={(e) => setItemId(e.target.value)} required>
        <option value="">Select item</option>
        {items.filter((i) => i.is_active).map((i) => (
          <option key={i.id} value={i.id}>{i.product_id} — {i.name}</option>
        ))}
      </Select>
      <Select label="Warehouse" value={warehouseId} onChange={(e) => setWarehouseId(e.target.value)} required>
        <option value="">Select warehouse</option>
        {warehouses.filter((w) => w.is_active).map((w) => (
          <option key={w.id} value={w.id}>{w.name}</option>
        ))}
      </Select>
      <Input label="Quantity" type="number" min={1} value={quantity} onChange={(e) => setQuantity(e.target.value)} required />
      <Input label="Reference" value={reference} onChange={(e) => setReference(e.target.value)} />
      <Input label="Remarks" value={remarks} onChange={(e) => setRemarks(e.target.value)} />
      <div className="flex items-end">
        <Button type="submit" disabled={create.isPending} className="w-full">
          {create.isPending ? "Saving…" : "Record stock out"}
        </Button>
      </div>
      {create.error && <p className="text-sm text-red-600 md:col-span-6">{create.error.message}</p>}
    </form>
  );
}
