"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const links = [
  { href: "/", label: "Dashboard" },
  { href: "/masters/items", label: "Items" },
  { href: "/masters/warehouses", label: "Warehouses" },
  { href: "/stock-in", label: "Stock In" },
  { href: "/stock-out", label: "Stock Out" },
  { href: "/stock/current", label: "Current Stock" },
];

export default function Header() {
  const pathname = usePathname();

  return (
    <header className="app-header sticky top-0 z-20 flex flex-col border-b border-slate-200 px-4 py-3 sm:px-6 md:items-end">
      <div className="flex w-full items-center justify-between md:justify-end">
        <Link href="/" className="font-bold text-teal-800 md:hidden">
          Inventory ERP
        </Link>
        <span className="text-xs font-medium text-slate-500 sm:text-sm">Warehouse &amp; Stock Management</span>
      </div>
      <nav aria-label="Main navigation" className="mobile-nav mt-3 flex w-full gap-1 overflow-x-auto pb-1 md:hidden">
        {links.map((link) => {
          const active = link.href === "/" ? pathname === "/" : pathname.startsWith(link.href);
          return (
            <Link
              key={link.href}
              href={link.href}
              aria-current={active ? "page" : undefined}
              className={`mobile-nav-link shrink-0 rounded-full px-3 py-2 text-xs font-semibold ${active ? "is-active" : ""}`}
            >
              {link.label}
            </Link>
          );
        })}
      </nav>
    </header>
  );
}
