"use client";

import PageHeader from "@/components/layout/PageHeader";
import StockOutForm from "@/components/stock-out/StockOutForm";
import StockOutTable from "@/components/stock-out/StockOutTable";
import { useStockOut } from "@/hooks/useStockOut";

export default function StockOutPage() {
  const { data = [], isLoading } = useStockOut();
  return (
    <>
      <PageHeader title="Stock Out" description="Record goods issued from a warehouse" />
      <StockOutForm />
      {isLoading ? <p className="text-sm text-slate-500">Loading…</p> : <StockOutTable entries={data} />}
    </>
  );
}
