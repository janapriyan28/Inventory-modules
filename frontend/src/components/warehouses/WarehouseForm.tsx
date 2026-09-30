"use client";

import { useState } from "react";
import Button from "@/components/ui/Button";
import Input from "@/components/ui/Input";
import type { Warehouse, WarehouseInput } from "@/types/warehouse";

export default function WarehouseForm({
  initial,
  onSubmit,
  onCancel,
  submitting,
  error,
}: {
  initial?: Warehouse;
  onSubmit: (data: WarehouseInput) => void;
  onCancel: () => void;
  submitting?: boolean;
  error?: string | null;
}) {
  const [code, setCode] = useState(initial?.code ?? "");
  const [name, setName] = useState(initial?.name ?? "");
  const [location, setLocation] = useState(initial?.location ?? "");
  const [active, setActive] = useState(initial?.is_active ?? true);

  return (
    <form
      className="space-y-3"
      onSubmit={(e) => {
        e.preventDefault();
        onSubmit({ code: code.trim(), name: name.trim(), location: location.trim() || null, is_active: active });
      }}
    >
      <Input label="Code" value={code} onChange={(e) => setCode(e.target.value)} required />
      <Input label="Name" value={name} onChange={(e) => setName(e.target.value)} required />
      <Input label="Location" value={location} onChange={(e) => setLocation(e.target.value)} />
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
