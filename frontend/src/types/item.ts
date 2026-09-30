export interface Item {
  id: number;
  product_id: string;
  name: string;
  fabric_type: string;
  price_inr: string;
  unit: string;
  reorder_level: number;
  is_active: boolean;
  created_at: string;
}

export type ItemInput = Omit<Item, "id" | "created_at">;
