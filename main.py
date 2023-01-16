from fastapi import FastAPI, UploadFile, File, Form
from typing import List
import uvicorn
from pdf2image import convert_from_bytes
import pytesseract

app = FastAPI()


@app.post("/uploadfile/vbhc")
# async def create_upload_file(file: Union[UploadFile, None] = None):
def upload(
        file: UploadFile = File(...)
):
    if not file:
        return {"message": "No upload file sent"}
    else:
        
        images= convert_from_bytes(file.file.read())
        ocr_pages=[]
        for image in images:
            ocr_content=ocr_content = pytesseract.image_to_string(image,lang='vie',config='--oem 1')
            ocr_pages.append(ocr_content)
        
        full_content=""

        for i in range(len(ocr_pages)):
            full_content+=ocr_pages[i]
            full_content+=f"\n --------------Page {i+1}------------ \n"
        print(full_content)
        return full_content



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000,  reload=True)
