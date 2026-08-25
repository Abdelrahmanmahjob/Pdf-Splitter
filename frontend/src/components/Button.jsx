export default function Button({ children, onClick, disabled = false }) {
  return (
    <button
      disabled={disabled}
      onClick={onClick}
      className="

            w-full

            py-4

            rounded-xl

            bg-blue-600

            hover:bg-blue-500

            duration-300

            font-semibold

            text-lg

            disabled:opacity-40

            "
    >
      {children}
    </button>
  )
}
