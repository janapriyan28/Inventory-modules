"use client";

import { useState } from "react";
import Button from "@/components/ui/Button";
import { API_URL } from "@/lib/api";

export default function ExportCsvButton({ warehouseId, lowOnly }: { warehouseId?: number; lowOnly?: boolean }) {
  const [busy, setBusy] = useState(false);

  async function download() {
    setBusy(true);
    try {
      const params = new URLSearchParams();
      if (warehouseId) params.set("warehouse_id", String(warehouseId));
      if (lowOnly) params.set("low_only", "true");
      const res = await fetch(`${API_URL}/stock/current/export?${params}`);
      if (!res.ok) throw new Error("Export failed");
      const url = URL.createObjectURL(await res.blob());
      const a = document.createElement("a");
      a.href = url;
      a.download = "current_stock.csv";
      a.click();
      URL.revokeObjectURL(url);
    } finally {
      setBusy(false);
    }
  }

  return (
    <Button variant="secondary" onClick={download} disabled={busy}>
      {busy ? "Exporting…" : "Export CSV"}
    </Button>
  );
}
