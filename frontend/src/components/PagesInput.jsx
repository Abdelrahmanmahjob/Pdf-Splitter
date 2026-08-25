export default function PagesInput({
  value,

  setValue,
}) {
  return (
    <input
      type="number"
      min={1}
      value={value}
      onChange={(e) => setValue(Number(e.target.value))}
      className="

            w-full

            p-3

            rounded-xl

            bg-zinc-800

            border

            border-zinc-700

            "
    />
  )
}
