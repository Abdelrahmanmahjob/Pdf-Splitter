import { useState } from "react"
import { processPDF } from "../api/processApi"

export default function useProcess(setRunning) {
  const [loading, setLoading] = useState(false)

  async function process(formData) {
    setLoading(true)
    if (typeof setRunning === "function") setRunning(true)

    try {
      const zipBlob = await processPDF(formData)

      const url = window.URL.createObjectURL(zipBlob)

      const a = document.createElement("a")

      a.href = url

      a.download = "Requests.zip"

      a.click()

      window.URL.revokeObjectURL(url)

      return zipBlob
    } finally {
      setLoading(false)
      if (typeof setRunning === "function") setRunning(false)
    }
  }

  return {
    loading,

    process,
  }
}
