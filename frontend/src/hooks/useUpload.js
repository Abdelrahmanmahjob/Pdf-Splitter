import { useState } from "react"

export default function useUpload() {
  const [loading, setLoading] = useState(false)

  const [progress, setProgress] = useState(0)

  const [downloadUrl, setDownloadUrl] = useState(null)

  return {
    loading,
    setLoading,

    progress,
    setProgress,

    downloadUrl,
    setDownloadUrl,
  }
}
