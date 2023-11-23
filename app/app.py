from flask import Flask, jsonify, request, send_file
import tempfile
import os
from fpdf import FPDF  

app = Flask(__name__)

@app.route('/redact-document', methods=['GET'])
def redact_document():
    try:

        redacted_document_path = redact_pdf()
        return send_file(
            redacted_document_path,
            mimetype='application/pdf',
            as_attachment=True,
            download_name='redacted_document.pdf',
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def redact_pdf():

    # this logic should be replaced actual PDF redaction logic
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Redacted Document", ln=True, align='C')

    # Save redacted PDF to a temporary file
    temp_dir = tempfile.mkdtemp()
    redacted_document_path = os.path.join(temp_dir, 'redacted_document.pdf')
    pdf.output(redacted_document_path)

    return redacted_document_path

if __name__ == '__main__':
    app.run(debug=True, port=5500)