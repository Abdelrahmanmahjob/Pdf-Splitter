from app.services.split_service import SplitService

splitter = SplitService(
    "uploads/document.pdf"
)

splitter.split(

    pages_per_request=3,

    output_folder="output/splitted"

)

print("Done")