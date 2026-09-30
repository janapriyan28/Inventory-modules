import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { api } from "@/lib/api";
import type { StockOut, StockOutInput } from "@/types/stock-out";

export function useStockOut() {
  return useQuery({ queryKey: ["stock-out"], queryFn: () => api<StockOut[]>("/stock-out") });
}

export function useCreateStockOut() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: (data: StockOutInput) => api<StockOut>("/stock-out", { method: "POST", body: JSON.stringify(data) }),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ["stock-out"] });
      qc.invalidateQueries({ queryKey: ["current-stock"] });
    },
  });
}
