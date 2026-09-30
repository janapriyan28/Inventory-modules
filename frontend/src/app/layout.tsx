import type { Metadata } from "next";
import "./globals.css";
import Header from "@/components/layout/Header";
import Sidebar from "@/components/layout/Sidebar";
import QueryProvider from "@/providers/QueryProvider";

export const metadata: Metadata = {
  title: "Inventory ERP",
  description: "Items, warehouses, stock in/out and current stock",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <QueryProvider>
          <div className="flex min-h-screen">
            <Sidebar />
            <div className="flex min-w-0 flex-1 flex-col">
              <Header />
              <main className="flex-1 p-6">{children}</main>
            </div>
          </div>
        </QueryProvider>
      </body>
    </html>
  );
}
