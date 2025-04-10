from fastapi import FastAPI, Request, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.services import parser  # Your previously defined parser module
import os

app = FastAPI(title="HVAC Parser API")

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up the templates directory
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_index(request: Request):
    # Render the index.html template at the root endpoint
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/test_parse")
def test_parse():
    sample_pdf_path = "data/sample_brochure.pdf"
    if not os.path.exists(sample_pdf_path):
        raise HTTPException(status_code=404, detail="Sample brochure not found.")
    
    texts = parser.extract_text_from_pdf(sample_pdf_path)
    chunks = parser.chunk_text(texts, max_chars=1500)
    
    results = []
    for chunk in chunks:
        prompt = parser.create_parsing_prompt(chunk)
        product_data = parser.parse_product_data(prompt)
        results.extend(product_data)
    
    return JSONResponse(content={"products": results})

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        temp_file_path = f"data/temp_{file.filename}"
        with open(temp_file_path, "wb") as buffer:
            buffer.write(await file.read())
        
        texts = parser.extract_text_from_pdf(temp_file_path)
        chunks = parser.chunk_text(texts, max_chars=1500)
        
        results = []
        for chunk in chunks:
            prompt = parser.create_parsing_prompt(chunk)
            product_data = parser.parse_product_data(prompt)
            results.extend(product_data)
        
        os.remove(temp_file_path)
        return JSONResponse(content={"products": results})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
