import UploadZone from "./UploadZone"

export default function UploadCard({ pdf, setPdf }) {
  return (
    <div className="bg-zinc-900 rounded-2xl p-6">
      <h2 className="text-xl font-bold mb-6">Upload PDF</h2>

      <UploadZone pdf={pdf} setPdf={setPdf} />
    </div>
  )
}
