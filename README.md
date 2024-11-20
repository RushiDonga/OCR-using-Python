# PDF Information Extraction Tool with OpenAI API on AWS Lambda

This project provides Python scripts for extracting specific information (e.g., patient details, medicines, and other important data) from PDF documents. It also includes a solution that integrates AWS Lambda and the OpenAI API for extracting structured data about medicines based on a query. The system accepts a query with a medicine name and returns detailed information such as the full brand name, strength, route, drug class, drug category, and manufacturer.

The core functionality is based on AWS Lambda for serverless execution, OpenAI's GPT model for intelligent extraction, and several libraries to process and extract data from PDF documents.


### Features
- PDF Extraction: Extracts structured information (e.g., patient details, medicines) from PDFs.
- OpenAI Integration: Utilizes OpenAI's API to generate detailed information about medicines based on a query.
- AWS Lambda: Serverless execution of functions to process requests and return responses.
- Multi-Library Support: Includes support for libraries like PyPDF2, pdfplumber, and Apache Tika for text extraction from PDFs.


### Key Components

1. PDF Extraction Tools:
- Extracts text from PDFs using PyPDF2, Apache Tika, and pdfplumber.
- Extracts key data such as Name, Age, Gender, Medicines, and Other Information.
- Outputs extracted data in JSON format.

2. AWS Lambda OpenAI Integration:
- Accepts a medicine name and retrieves detailed information using the OpenAI GPT model.
- Returns a structured JSON response with the medicine's brand name, strength, route, drug class, drug category, and manufacturer.

### Libraries and Toold Used

1. PyPDF2
- Lightweight library for extracting text from PDFs.
- Best for text-based PDFs with straightforward layouts.

2. Apache Tika
- Robust and versatile library for extracting text from PDFs and other document types.
- Can handle both text-based and image-based PDFs (with OCR support if configured).

3. pdfplumber
Provides precise control over text and table extraction.
Suitable for complex PDF layouts, such as tables or forms.


