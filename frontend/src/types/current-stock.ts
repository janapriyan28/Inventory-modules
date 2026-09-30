export interface CurrentStockRow {
  item_id: number;
  product_id: string;
  item_name: string;
  unit: string;
  warehouse_id: number;
  warehouse_name: string;
  quantity: number;
  reorder_level: number;
  is_low: boolean;
}
