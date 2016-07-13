from pathlib import Path
import pdf

resources_path = Path(
    ".\Resources")
pdf_files = list(resources_path.glob('**/*.pdf'))

print(pdf_files)
