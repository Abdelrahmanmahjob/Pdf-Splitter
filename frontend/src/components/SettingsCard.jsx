import RotationSelect from "./RotationSelect"
import PagesInput from "./PagesInput"
import CodeSelector from "./CodeSelector"
import Button from "./Button"

export default function SettingsCard({
  pages,
  setPages,
  pdfRotation,
  setPdfRotation,
  ocrRotation,
  setOcrRotation,
  code,
  setCode,
  loading,
  onProcess,
}) {
  return (
    <div className="bg-zinc-900 rounded-2xl p-8">
      <h2 className="text-2xl font-bold mb-8">Processing Settings</h2>

      <div className="space-y-7">
        <div>
          <label className="block mb-2 text-zinc-400">Pages Per Request</label>

          <PagesInput value={pages} setValue={setPages} />
        </div>

        <div>
          <label className="block mb-2 text-zinc-400">PDF Rotation</label>

          <RotationSelect value={pdfRotation} setValue={setPdfRotation} />
        </div>

        <div>
          <label className="block mb-2 text-zinc-400">OCR Rotation</label>

          <RotationSelect value={ocrRotation} setValue={setOcrRotation} />
        </div>

        <div>
          <label className="block mb-2 text-zinc-400">Code Detection</label>

          <CodeSelector value={code} setValue={setCode} />
        </div>

        <Button disabled={loading} onClick={onProcess}>
          {loading ? "Processing..." : "Split Requests"}
        </Button>
      </div>
    </div>
  )
}
