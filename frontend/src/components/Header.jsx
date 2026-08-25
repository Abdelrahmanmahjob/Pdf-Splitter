import { FileText } from "lucide-react"

export default function Header() {
  return (
    <header className="border-b border-zinc-800 bg-zinc-950">
      <div className="max-w-7xl mx-auto px-8 py-5 flex items-center justify-between">
        <div className="flex items-center gap-4">
          <div className="w-12 h-12 rounded-xl bg-blue-600 flex items-center justify-center">
            <FileText className="text-white" size={22} />
          </div>

          <div>
            <h1 className="text-2xl font-bold">Request Splitter Pro</h1>

            <p className="text-zinc-400 text-sm">OCR PDF Request Extractor</p>
          </div>
        </div>
      </div>
    </header>
  )
}
