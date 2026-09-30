"use client";

import Link from "next/link";
import PageHeader from "@/components/layout/PageHeader";
import LowStockAlert from "@/components/stock/LowStockAlert";
import { useCurrentStock } from "@/hooks/useCurrentStock";
import { useItems } from "@/hooks/useItems";
import { useWarehouses } from "@/hooks/useWarehouses";

function Card({ label, value, href, kind }: { label: string; value: number | string; href: string; kind: string }) {
  return (
    <Link href={href} className={`dashboard-metric dashboard-metric--${kind} group rounded-lg border border-slate-200 p-5`}>
      <span className="metric-kicker">{label}</span>
      <p className="mt-3 text-4xl font-semibold tracking-tight text-slate-800">{value}</p>
      <span className="metric-link mt-5 inline-flex items-center gap-2 text-xs font-semibold text-slate-500">
        Explore <span aria-hidden="true" className="metric-arrow">-&gt;</span>
      </span>
    </Link>
  );
}

export default function DashboardPage() {
  const { data: items = [] } = useItems();
  const { data: warehouses = [] } = useWarehouses();
  const { data: stock = [] } = useCurrentStock();
  const low = stock.filter((s) => s.is_low).length;

  return (
    <>
      <div className="dashboard-intro">
        <span className="dashboard-eyebrow">INVENTORY OVERVIEW</span>
        <PageHeader title="Dashboard" description="A clear view of items, storage, and stock health." />
      </div>
      <LowStockAlert rows={stock} />
      <div className="dashboard-metrics grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <Card kind="items" label="Items" value={items.length} href="/masters/items" />
        <Card kind="warehouses" label="Warehouses" value={warehouses.length} href="/masters/warehouses" />
        <Card kind="stock" label="Stock lines" value={stock.length} href="/stock/current" />
        <Card kind="low-stock" label="Low stock" value={low} href="/stock/current" />
      </div>
    </>
  );
}
