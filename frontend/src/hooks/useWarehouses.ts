import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { api } from "@/lib/api";
import type { Warehouse, WarehouseInput } from "@/types/warehouse";

const KEY = ["warehouses"];

export function useWarehouses() {
  return useQuery({ queryKey: KEY, queryFn: () => api<Warehouse[]>("/warehouses") });
}

export function useSaveWarehouse() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: ({ id, data }: { id?: number; data: Partial<WarehouseInput> }) =>
      id
        ? api<Warehouse>(`/warehouses/${id}`, { method: "PATCH", body: JSON.stringify(data) })
        : api<Warehouse>("/warehouses", { method: "POST", body: JSON.stringify(data) }),
    onSuccess: () => qc.invalidateQueries({ queryKey: KEY }),
  });
}

export function useDeleteWarehouse() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: (id: number) => api<void>(`/warehouses/${id}`, { method: "DELETE" }),
    onSuccess: () => qc.invalidateQueries({ queryKey: KEY }),
  });
}
