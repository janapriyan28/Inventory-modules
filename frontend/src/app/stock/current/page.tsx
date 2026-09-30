"use client";

import { useState } from "react";
import PageHeader from "@/components/layout/PageHeader";
import CurrentStockTable from "@/components/stock/CurrentStockTable";
import ExportCsvButton from "@/components/stock/ExportCsvButton";
import LowStockAlert from "@/components/stock/LowStockAlert";
import Select from "@/components/ui/Select";
import { useCurrentStock } from "@/hooks/useCurrentStock";
import { useWarehouses } from "@/hooks/useWarehouses";

export default function CurrentStockPage() {
  const [warehouseId, setWarehouseId] = useState<number | undefined>();
  const [lowOnly, setLowOnly] = useState(false);
  const { data: warehouses = [] } = useWarehouses();
  const { data = [], isLoading, error } = useCurrentStock(warehouseId, lowOnly);

  return (
    <>
      <PageHeader
        title="Current Stock"
        description="Stock on hand per item and warehouse"
        actions={<ExportCsvButton warehouseId={warehouseId} lowOnly={lowOnly} />}
      />
      <LowStockAlert rows={data} />
      <div className="mb-4 flex flex-wrap items-end gap-4">
        <div className="w-56">
          <Select
            label="Warehouse"
            value={warehouseId ?? ""}
            onChange={(e) => setWarehouseId(e.target.value ? Number(e.target.value) : undefined)}
          >
            <option value="">All warehouses</option>
            {warehouses.map((w) => (
              <option key={w.id} value={w.id}>{w.name}</option>
            ))}
          </Select>
        </div>
        <label className="flex items-center gap-2 pb-2 text-sm">
          <input type="checkbox" checked={lowOnly} onChange={(e) => setLowOnly(e.target.checked)} /> Low stock only
        </label>
      </div>
      {error && <p className="mb-3 text-sm text-red-600">{error.message}</p>}
      {isLoading ? <p className="text-sm text-slate-500">Loading…</p> : <CurrentStockTable rows={data} />}
    </>
  );
}
