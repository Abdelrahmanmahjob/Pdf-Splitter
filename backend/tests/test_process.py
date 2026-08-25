from app.services.process_engine import ProcessEngine

engine = ProcessEngine()

engine.process(
    pdf_path="uploads/document.pdf",
    pages_per_request=4,
    output_folder="output/final",
    # fixed_code="B"
)

print("Finished")