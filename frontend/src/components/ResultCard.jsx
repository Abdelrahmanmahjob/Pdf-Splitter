import Button from "./Button"

export default function ResultCard({ download }) {
  return (
    <div className="bg-zinc-900 rounded-2xl p-6">
      <h2 className="text-2xl font-bold">Completed</h2>

      <p className="text-zinc-400 mt-3">Processing Finished Successfully</p>

      <div className="mt-6">
        <Button onClick={download}>Download ZIP</Button>
      </div>
    </div>
  )
}
