"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { cn } from "@/lib/utils";

const links = [
  { href: "/", label: "Dashboard" },
  { href: "/masters/items", label: "Items" },
  { href: "/masters/warehouses", label: "Warehouses" },
  { href: "/stock-in", label: "Stock In" },
  { href: "/stock-out", label: "Stock Out" },
  { href: "/stock/current", label: "Current Stock" },
];

export default function Sidebar() {
  const pathname = usePathname();
  return (
    <aside className="app-sidebar hidden w-56 shrink-0 border-r border-slate-200 md:block">
      <div className="sidebar-brand px-5 py-5">
        <span className="sidebar-mark" aria-hidden="true">I</span>
        <span>
          <span className="block text-base font-bold text-slate-800">Inventory ERP</span>
          <span className="mt-0.5 block text-[10px] font-semibold uppercase tracking-[0.16em] text-slate-500">Stock operations</span>
        </span>
      </div>
      <nav className="space-y-1 px-3">
        {links.map((l) => {
          const active = l.href === "/" ? pathname === "/" : pathname.startsWith(l.href);
          return (
            <Link
              key={l.href}
              href={l.href}
              className={cn(
                "sidebar-link block rounded-md px-3 py-2.5 text-sm font-medium",
                active ? "is-active bg-teal-50 text-teal-800" : "text-slate-600 hover:bg-white/70"
              )}
            >
              {l.label}
            </Link>
          );
        })}
      </nav>
    </aside>
  );
}
