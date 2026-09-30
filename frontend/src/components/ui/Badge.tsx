import { cn } from "@/lib/utils";

const tones = {
  green: "bg-green-100 text-green-700",
  red: "bg-red-100 text-red-700",
  gray: "bg-slate-100 text-slate-600",
};

export default function Badge({ tone = "gray", children }: { tone?: keyof typeof tones; children: React.ReactNode }) {
  return <span className={cn("rounded-full px-2 py-0.5 text-xs font-medium", tones[tone])}>{children}</span>;
}
