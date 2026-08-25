import { useState } from "react"

import Header from "../components/Header"
import UploadCard from "../components/UploadCard"
import SettingsCard from "../components/SettingsCard"
import ProgressCard from "../components/ProgressCard"
import ResultCard from "../components/ResultCard"

import useProcess from "../hooks/useProcess"
import useStatus from "../hooks/useStatus"

export default function Home() {
  const [pdf, setPdf] = useState(null)

  const [pages, setPages] = useState(3)

  const [pdfRotation, setPdfRotation] = useState("0")

  const [ocrRotation, setOcrRotation] = useState("Auto")

  const [code, setCode] = useState("Auto")

  const [running, setRunning] = useState(false)

  const [resultBlob, setResultBlob] = useState(null)

  const [completed, setCompleted] = useState(false)

  const { process, loading } = useProcess(setRunning)

  const { progress, status } = useStatus(running)

  async function handleProcess() {
    if (!pdf) {
      alert("Choose PDF")
      return
    }

    setCompleted(false)

    const formData = new FormData()

    formData.append("pdf", pdf)

    formData.append("pages_per_request", pages)

    formData.append("fixed_code", code === "Auto" ? "" : code)

    formData.append("pdf_rotation", pdfRotation === "Auto" ? "0" : pdfRotation)

    formData.append("ocr_rotation", ocrRotation === "Auto" ? "0" : ocrRotation)

    formData.append("auto_rotate", ocrRotation === "Auto")

    const blob = await process(formData)

    if (blob) {
      setResultBlob(blob)
      setCompleted(true)
    }
  }

  function handleDownload() {
    if (!resultBlob) return

    const url = window.URL.createObjectURL(resultBlob)

    const a = document.createElement("a")

    a.href = url

    a.download = "Requests.zip"

    a.click()

    window.URL.revokeObjectURL(url)
  }

  return (
    <div className="min-h-screen bg-zinc-950">
      <Header />

      <div className="max-w-7xl mx-auto p-8 space-y-8">
        <div className="grid lg:grid-cols-2 gap-8">
          <UploadCard pdf={pdf} setPdf={setPdf} />

          <SettingsCard
            pages={pages}
            setPages={setPages}
            pdfRotation={pdfRotation}
            setPdfRotation={setPdfRotation}
            ocrRotation={ocrRotation}
            setOcrRotation={setOcrRotation}
            code={code}
            setCode={setCode}
            loading={loading}
            onProcess={handleProcess}
          />
        </div>

        <ProgressCard progress={progress} status={status} />

        {completed && <ResultCard download={handleDownload} />}
      </div>
    </div>
  )
}
