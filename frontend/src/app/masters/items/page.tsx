"use client";

import { useState } from "react";
import PageHeader from "@/components/layout/PageHeader";
import ItemModal from "@/components/items/ItemModal";
import ItemTable from "@/components/items/ItemTable";
import Button from "@/components/ui/Button";
import { useDeleteItem, useItems } from "@/hooks/useItems";
import type { Item } from "@/types/item";

export default function ItemsPage() {
  const { data: items = [], isLoading, error } = useItems();
  const del = useDeleteItem();
  const [editing, setEditing] = useState<Item | undefined>();
  const [open, setOpen] = useState(false);

  return (
    <>
      <PageHeader
        title="Items"
        description="Item master"
        actions={<Button onClick={() => { setEditing(undefined); setOpen(true); }}>New item</Button>}
      />
      {error && <p className="mb-3 text-sm text-red-600">{error.message}</p>}
      {del.error && <p className="mb-3 text-sm text-red-600">{del.error.message}</p>}
      {isLoading ? (
        <p className="text-sm text-slate-500">Loading…</p>
      ) : (
        <ItemTable
          items={items}
          onEdit={(i) => { setEditing(i); setOpen(true); }}
          onDelete={(i) => confirm(`Delete ${i.name}?`) && del.mutate(i.id)}
        />
      )}
      <ItemModal key={editing?.id ?? "new"} open={open} item={editing} onClose={() => setOpen(false)} />
    </>
  );
}
