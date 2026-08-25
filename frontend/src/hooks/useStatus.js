import { useEffect, useState } from "react"
import { getStatus } from "../api/statusApi"

export default function useStatus(isRunning) {
  const [progress, setProgress] = useState(0)

  const [status, setStatus] = useState("Idle")

  useEffect(() => {
    if (!isRunning) return

    const interval = setInterval(async () => {
      const data = await getStatus()

      setProgress(data.progress)

      setStatus(data.status)
    }, 500)

    return () => clearInterval(interval)
  }, [isRunning])

  return {
    progress,
    status,
  }
}
