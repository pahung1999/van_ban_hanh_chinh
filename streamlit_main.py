import streamlit as st
import os
from pdf2image import convert_from_bytes
import pytesseract


os.system("clear")
st.set_page_config(layout="wide")

st.header("OCR Văn bản hành chính")

upload_methods = ["Từ thư viện trong máy"] #, "Chụp ảnh mới"]
upload_method = st.radio("Phương pháp upload ảnh", upload_methods)

pdf_file = st.file_uploader("Upload file")

left, right = st.columns(2)

if pdf_file is not None:
    images= convert_from_bytes(pdf_file.getvalue())

    for image in images:
        left.image(image)
    submit = left.button("Nhận dạng")
else:
    submit = clear = False

if submit:
    with st.spinner(text="Processing..."):

        ocr_pages=[]
        for image in images:
            ocr_content=ocr_content = pytesseract.image_to_string(image,lang='vie',config='--oem 1')
            ocr_pages.append(ocr_content)
        
        full_content=""

        for i in range(len(ocr_pages)):
            full_content+=ocr_pages[i]
            full_content+=f"\n --------------Page {i+1}------------ \n"
        right.write(full_content)