import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { api } from "@/lib/api";
import type { StockIn, StockInInput } from "@/types/stock-in";

export function useStockIn() {
  return useQuery({ queryKey: ["stock-in"], queryFn: () => api<StockIn[]>("/stock-in") });
}

export function useCreateStockIn() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: (data: StockInInput) => api<StockIn>("/stock-in", { method: "POST", body: JSON.stringify(data) }),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ["stock-in"] });
      qc.invalidateQueries({ queryKey: ["current-stock"] });
    },
  });
}
