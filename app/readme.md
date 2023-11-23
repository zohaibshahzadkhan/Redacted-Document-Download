# Redacted Document Download Feature

This feature allows users to download a copy of a PDF document with all annotation locations redacted.

## Frontend (JavaScript)

The frontend is a simple HTML page with a button triggering the redacted document download.

### Usage

Open `index.html` in a web browser and click the "Download Redacted Document" button.

## Backend (Python)

The backend is a Flask application in Python using the `fpdf` library for PDF processing.

### Installation

1. Install the required Python packages:

   ```bash
   pip install Flask fpdf


## Run the Flask application:

```bash
python app.py 
```

## API Endpoint
### POST /redact-document: 
Initiates the redaction process and returns the redacted document for download.
### Dependencies

Flask: Web framework for Python.

fpdf: PDF generation library for Python.
[redacted_document.pdf](https://github.com/zohaibshahzadkhan/Redacted-Document-Download/files/13448632/redacted_document.pdf)

