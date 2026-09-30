import type { CurrentStockRow } from "@/types/current-stock";

export default function LowStockAlert({ rows }: { rows: CurrentStockRow[] }) {
  const low = rows.filter((r) => r.is_low);
  if (low.length === 0) return null;
  return (
    <div className="mb-4 rounded-lg border border-red-200 bg-red-50 p-4 text-sm text-red-800">
      <p className="font-semibold">
        {low.length} item{low.length > 1 ? "s are" : " is"} at or below reorder level
      </p>
      <ul className="mt-1 list-inside list-disc">
        {low.slice(0, 5).map((r) => (
          <li key={`${r.item_id}-${r.warehouse_id}`}>
            {r.item_name} @ {r.warehouse_name}: {r.quantity} {r.unit} (reorder at {r.reorder_level})
          </li>
        ))}
        {low.length > 5 && <li>…and {low.length - 5} more</li>}
      </ul>
    </div>
  );
}
