import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { api } from "@/lib/api";
import type { Item, ItemInput } from "@/types/item";

const KEY = ["items"];

export function useItems() {
  return useQuery({ queryKey: KEY, queryFn: () => api<Item[]>("/items") });
}

export function useSaveItem() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: ({ id, data }: { id?: number; data: Partial<ItemInput> }) =>
      id
        ? api<Item>(`/items/${id}`, { method: "PATCH", body: JSON.stringify(data) })
        : api<Item>("/items", { method: "POST", body: JSON.stringify(data) }),
    onSuccess: () => qc.invalidateQueries({ queryKey: KEY }),
  });
}

export function useDeleteItem() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: (id: number) => api<void>(`/items/${id}`, { method: "DELETE" }),
    onSuccess: () => qc.invalidateQueries({ queryKey: KEY }),
  });
}
