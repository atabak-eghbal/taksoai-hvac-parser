# backend/test_parser.py

from app.services import parser

def test_extract_text():
    # For testing, we'll simulate a PDF file.
    # If you have a sample PDF (e.g. backend/data/sample_brochure.pdf), use its path.
    sample_pdf = "data/sample_brochure.pdf"
    try:
        texts = parser.extract_text_from_pdf(sample_pdf)
        print("Extracted text from PDF:")
        for i, text in enumerate(texts):
            print(f"Page {i+1}:", text[:100], "...\n")  # Show the first 100 characters of each page
    except Exception as e:
        print("Error extracting text from PDF:", e)

def test_chunking_and_prompt():
    # Simulate extracted text as a list of strings (like pages)
    sample_texts = [
        "This is a sample text representing a page from the brochure. It includes product details and specifications.",
        "Another page with more information. More product data here."
    ]
    chunks = parser.chunk_text(sample_texts, max_chars=50)
    print("Chunks:")
    for chunk in chunks:
        print(f"'{chunk}'")
    
    # Create a prompt from the first chunk
    prompt = parser.create_parsing_prompt(chunks[0])
    print("\nSample Prompt:\n", prompt)

def test_llm_stub():
    # Use the stub function to simulate product extraction.
    sample_chunk = "Sample product text with details."
    prompt = parser.create_parsing_prompt(sample_chunk)
    products = parser.parse_product_data(prompt)
    print("\nLLM Parsing Stub Output (should be empty list):", products)

if __name__ == "__main__":
    print("Running PDF Parsing Tests...\n")
    test_extract_text()
    print("\n--------------------\n")
    test_chunking_and_prompt()
    print("\n--------------------\n")
    test_llm_stub()
