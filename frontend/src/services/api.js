import axios from "axios"

// const base = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000"

export default axios.create({
  baseURL: "/api", // يشير تلقائياً إلى نفس نطاق Vercel
  headers: {
    "Content-Type": "application/json",
  },
})
