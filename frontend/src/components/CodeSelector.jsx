export default function CodeSelector({
  value,

  setValue,
}) {
  return (
    <div className="flex gap-6">
      {["Auto", "B", "C"].map((item) => (
        <label key={item} className="flex gap-2">
          <input
            type="radio"
            checked={value === item}
            onChange={() => setValue(item)}
          />

          {item}
        </label>
      ))}
    </div>
  )
}
