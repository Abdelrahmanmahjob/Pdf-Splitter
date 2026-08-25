import api from "../services/api"

export async function processPDF(formData) {
  const response = await api.post("/process", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
    responseType: "blob",
  })

  return response.data
}
