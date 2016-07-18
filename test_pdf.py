from pathlib import Path

resources_path = Path(
    ".\Resources")
pdf_files = list(resources_path.glob('**/*.pdf'))

print(pdf_files)
