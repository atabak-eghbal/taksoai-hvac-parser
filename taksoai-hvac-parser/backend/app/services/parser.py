# backend/app/services/parser.py
import pdfplumber
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser

# ------------------------------
# PDF Extraction and Chunking
# ------------------------------

def extract_text_from_pdf(file_path: str) -> list:
    """
    Extract text from a PDF file using pdfplumber.
    Returns a list of text strings, one per page.
    """
    texts = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            texts.append(page.extract_text())
    return texts

def chunk_text(texts: list, max_chars: int = 1500) -> list:
    """
    Naively split each page of text into chunks of up to max_chars characters.
    """
    chunks = []
    for text in texts:
        for i in range(0, len(text), max_chars):
            chunks.append(text[i:i + max_chars])
    return chunks

def create_parsing_prompt(chunk: str) -> str:
    """
    Create a prompt for the LLM instructing it to extract product information.
    """
    return f"""
Extract all products from the following text.
For each product, provide a JSON with the fields:
product_name, model_number, category, specs, manufacturer.
Text: {chunk}
"""

# ------------------------------
# Structured Output Parsing Setup
# ------------------------------

# Define the product schema with Pydantic
class Product(BaseModel):
    product_name: str = Field(..., description="Product name")
    model_number: str = Field(..., description="Model number")
    category: str = Field(..., description="Product category")
    specs: str = Field(..., description="Key product specifications")
    manufacturer: str = Field(None, description="Manufacturer, if available")

# Create an output parser based on the Product schema.
output_parser = PydanticOutputParser(pydantic_object=Product)

def parse_product_data(prompt: str) -> list:
    """
    Replace the dummy LLM call with a simulated LLM response.
    
    In a real scenario, you would call your LLM (e.g. via HuggingFacePipeline)
    to generate output from the prompt.
    """
    # Simulated response (this string would normally come from the LLM)
    simulated_llm_response = """
    {
      "product_name": "SuperCool Chiller 3000",
      "model_number": "X100",
      "category": "Chillers",
      "specs": "Capacity: 5 Ton, Power: 55k BTU",
      "manufacturer": "ACME Corp."
    }
    """
    # Parse and validate the simulated response using the output parser.
    try:
        product = output_parser.parse(simulated_llm_response)
    except Exception as e:
        print("Error parsing LLM output:", e)
        return []
    # Return a list containing the parsed product dictionary.
    return [product.dict()]
