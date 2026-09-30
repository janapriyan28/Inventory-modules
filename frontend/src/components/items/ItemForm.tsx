"use client";

import { useState } from "react";
import Button from "@/components/ui/Button";
import Input from "@/components/ui/Input";
import type { Item, ItemInput } from "@/types/item";

export default function ItemForm({
  initial,
  onSubmit,
  onCancel,
  submitting,
  error,
}: {
  initial?: Item;
  onSubmit: (data: ItemInput) => void;
  onCancel: () => void;
  submitting?: boolean;
  error?: string | null;
}) {
  const [productId, setProductId] = useState(initial?.product_id ?? "");
  const [name, setName] = useState(initial?.name ?? "");
  const [fabricType, setFabricType] = useState(initial?.fabric_type ?? "");
  const [priceInr, setPriceInr] = useState(initial?.price_inr ?? "0.00");
  const [unit, setUnit] = useState(initial?.unit ?? "pcs");
  const [reorder, setReorder] = useState(String(initial?.reorder_level ?? 0));
  const [active, setActive] = useState(initial?.is_active ?? true);

  return (
    <form
      className="space-y-3"
      onSubmit={(e) => {
        e.preventDefault();
        onSubmit({ product_id: productId.trim(), name: name.trim(), fabric_type: fabricType.trim(), price_inr: priceInr, unit: unit.trim() || "pcs", reorder_level: Number(reorder) || 0, is_active: active });
      }}
    >
      <Input label="Product ID" value={productId} onChange={(e) => setProductId(e.target.value)} required />
      <Input label="Product Name" value={name} onChange={(e) => setName(e.target.value)} required />
      <Input label="Fabric Type" value={fabricType} onChange={(e) => setFabricType(e.target.value)} required />
      <Input label="Price (INR)" type="number" min={0} step="0.01" value={priceInr} onChange={(e) => setPriceInr(e.target.value)} required />
      <div className="grid grid-cols-2 gap-3">
        <Input label="Unit" value={unit} onChange={(e) => setUnit(e.target.value)} />
        <Input label="Reorder level" type="number" min={0} value={reorder} onChange={(e) => setReorder(e.target.value)} />
      </div>
      <label className="flex items-center gap-2 text-sm">
        <input type="checkbox" checked={active} onChange={(e) => setActive(e.target.checked)} /> Active
      </label>
      {error && <p className="text-sm text-red-600">{error}</p>}
      <div className="flex justify-end gap-2 pt-2">
        <Button type="button" variant="secondary" onClick={onCancel}>Cancel</Button>
        <Button type="submit" disabled={submitting}>{submitting ? "Saving…" : "Save"}</Button>
      </div>
    </form>
  );
}
