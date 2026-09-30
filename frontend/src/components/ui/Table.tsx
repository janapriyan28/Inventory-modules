import EmptyState from "./EmptyState";

export interface Column<T> {
  header: string;
  cell: (row: T) => React.ReactNode;
  className?: string;
}

export default function Table<T extends object>({
  columns,
  rows,
  empty = "No records yet.",
  rowKey,
}: {
  columns: Column<T>[];
  rows: T[];
  empty?: string;
  rowKey?: (row: T) => string | number;
}) {
  if (rows.length === 0) return <EmptyState message={empty} />;
  return (
    <div className="overflow-x-auto rounded-lg border border-slate-200 bg-white">
      <table className="min-w-full divide-y divide-slate-200 text-sm">
        <thead className="bg-slate-50">
          <tr>
            {columns.map((c) => (
              <th key={c.header} className="px-4 py-3 text-left font-semibold text-slate-600">
                {c.header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="divide-y divide-slate-100">
          {rows.map((row, i) => (
            <tr
              key={rowKey ? rowKey(row) : ("id" in row && (typeof row.id === "string" || typeof row.id === "number") ? row.id : i)}
              className="hover:bg-slate-50"
            >
              {columns.map((c) => (
                <td key={c.header} className={`px-4 py-3 ${c.className ?? ""}`}>
                  {c.cell(row)}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
