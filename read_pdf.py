import pypdf

filename = "kyyeu-2024.pdf"

try:
    reader = pypdf.PdfReader(filename)
    # The user said page 488. In PDFs, page labels often match physical pages if straightforward.
    # I will print the text of the page at index 487 (which is the 488th page) and 488 (489th) to be sure.
    
    print("--- Page 488 (Index 487) ---")
    if len(reader.pages) > 487:
        print(reader.pages[487].extract_text())
    
    print("\n--- Page 489 (Index 488) ---")
    if len(reader.pages) > 488:
        print(reader.pages[488].extract_text())

except Exception as e:
    print(f"Error: {e}")
