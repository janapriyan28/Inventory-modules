"use client";

import Modal from "@/components/ui/Modal";
import { useSaveItem } from "@/hooks/useItems";
import type { Item } from "@/types/item";
import ItemForm from "./ItemForm";

export default function ItemModal({ open, item, onClose }: { open: boolean; item?: Item; onClose: () => void }) {
  const save = useSaveItem();
  if (!open) return null;
  return (
    <Modal open={open} title={item ? "Edit item" : "New item"} onClose={onClose}>
      <ItemForm
        initial={item}
        submitting={save.isPending}
        error={save.error?.message}
        onCancel={onClose}
        onSubmit={(data) => save.mutate({ id: item?.id, data }, { onSuccess: onClose })}
      />
    </Modal>
  );
}
