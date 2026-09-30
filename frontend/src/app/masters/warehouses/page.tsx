"use client";

import { useState } from "react";
import PageHeader from "@/components/layout/PageHeader";
import WarehouseForm from "@/components/warehouses/WarehouseForm";
import WarehouseTable from "@/components/warehouses/WarehouseTable";
import Button from "@/components/ui/Button";
import Modal from "@/components/ui/Modal";
import { useDeleteWarehouse, useSaveWarehouse, useWarehouses } from "@/hooks/useWarehouses";
import type { Warehouse } from "@/types/warehouse";

export default function WarehousesPage() {
  const { data: warehouses = [], isLoading, error } = useWarehouses();
  const save = useSaveWarehouse();
  const del = useDeleteWarehouse();
  const [editing, setEditing] = useState<Warehouse | undefined>();
  const [open, setOpen] = useState(false);
  const close = () => { setOpen(false); save.reset(); };

  return (
    <>
      <PageHeader
        title="Warehouses"
        description="Warehouse master"
        actions={<Button onClick={() => { setEditing(undefined); setOpen(true); }}>New warehouse</Button>}
      />
      {error && <p className="mb-3 text-sm text-red-600">{error.message}</p>}
      {del.error && <p className="mb-3 text-sm text-red-600">{del.error.message}</p>}
      {isLoading ? (
        <p className="text-sm text-slate-500">Loading…</p>
      ) : (
        <WarehouseTable
          warehouses={warehouses}
          onEdit={(w) => { setEditing(w); setOpen(true); }}
          onDelete={(w) => confirm(`Delete ${w.name}?`) && del.mutate(w.id)}
        />
      )}
      <Modal open={open} title={editing ? "Edit warehouse" : "New warehouse"} onClose={close}>
        <WarehouseForm
          key={editing?.id ?? "new"}
          initial={editing}
          submitting={save.isPending}
          error={save.error?.message}
          onCancel={close}
          onSubmit={(data) => save.mutate({ id: editing?.id, data }, { onSuccess: close })}
        />
      </Modal>
    </>
  );
}
