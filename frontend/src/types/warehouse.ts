export interface Warehouse {
  id: number;
  code: string;
  name: string;
  location: string | null;
  is_active: boolean;
  created_at: string;
}

export type WarehouseInput = Omit<Warehouse, "id" | "created_at">;
