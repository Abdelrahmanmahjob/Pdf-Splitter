const rotations = ["Auto", -270, -180, -90, 0, 90, 180, 270]

export default function RotationSelect({
  value,

  setValue,
}) {
  return (
    <select
      value={value}
      onChange={(e) => setValue(e.target.value)}
      className="

            w-full

            p-3

            rounded-xl

            bg-zinc-800

            border

            border-zinc-700

            "
    >
      {rotations.map((rotation) => (
        <option key={rotation} value={rotation}>
          {rotation === "Auto" ? "Auto" : `${rotation}°`}
        </option>
      ))}
    </select>
  )
}
