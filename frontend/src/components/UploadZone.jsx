import { useDropzone } from "react-dropzone"
import { FaFilePdf } from "react-icons/fa6"

export default function UploadZone({ pdf, setPdf }) {
  const { getRootProps, getInputProps } = useDropzone({
    accept: {
      "application/pdf": [".pdf"],
    },

    multiple: false,

    onDrop: (files) => {
      setPdf(files[0])
    },
  })

  return (
    <div
      {...getRootProps()}
      className="

            border-2

            border-dashed

            border-zinc-700

            rounded-2xl

            p-10

            text-center

            cursor-pointer

            hover:border-blue-500

            duration-300

            "
    >
      <input {...getInputProps()} />

      <FaFilePdf className="mx-auto text-red-500" size={60} />

      <h2 className="mt-5 text-xl">Drag PDF Here</h2>

      <p className="text-zinc-500 mt-2">or click to browse</p>

      {pdf && (
        <div className="mt-6">
          <p className="text-green-400">{pdf.name}</p>
        </div>
      )}
    </div>
  )
}
