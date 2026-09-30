export interface StockOut {
  id: number;
  item_id: number;
  item_product_id: string;
  item_name: string;
  warehouse_id: number;
  warehouse_name: string;
  quantity: number;
  reference: string | null;
  remarks: string | null;
  created_at: string;
}

export interface StockOutInput {
  item_id: number;
  warehouse_id: number;
  quantity: number;
  reference?: string | null;
  remarks?: string | null;
}
