import { useQuery } from "@tanstack/react-query";
import { api } from "@/lib/api";
import type { CurrentStockRow } from "@/types/current-stock";

export function useCurrentStock(warehouseId?: number, lowOnly = false) {
  const params = new URLSearchParams();
  if (warehouseId) params.set("warehouse_id", String(warehouseId));
  if (lowOnly) params.set("low_only", "true");
  const qs = params.toString();
  return useQuery({
    queryKey: ["current-stock", warehouseId ?? null, lowOnly],
    queryFn: () => api<CurrentStockRow[]>(`/stock/current${qs ? `?${qs}` : ""}`),
  });
}
