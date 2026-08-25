export default function ProgressCard({ progress, status }) {
  return (
    <div className="bg-zinc-900 rounded-xl p-6 border border-zinc-800">
      <h2 className="text-xl font-bold mb-5">Progress</h2>

      <div className="w-full bg-zinc-700 rounded-full h-4 overflow-hidden">
        <div
          className="bg-blue-500 h-full transition-all duration-500"
          style={{
            width: `${progress}%`,
          }}
        />
      </div>

      <p className="mt-4 text-zinc-300">{status}</p>

      <p className="text-blue-400 font-bold">{progress}%</p>
    </div>
  )
}
