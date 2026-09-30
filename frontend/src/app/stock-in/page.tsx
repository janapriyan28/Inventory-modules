"use client";

import PageHeader from "@/components/layout/PageHeader";
import StockInForm from "@/components/stock-in/StockInForm";
import StockInTable from "@/components/stock-in/StockInTable";
import { useStockIn } from "@/hooks/useStockIn";

export default function StockInPage() {
  const { data = [], isLoading } = useStockIn();
  return (
    <>
      <PageHeader title="Stock In" description="Record goods received into a warehouse" />
      <StockInForm />
      {isLoading ? <p className="text-sm text-slate-500">Loading…</p> : <StockInTable entries={data} />}
    </>
  );
}
