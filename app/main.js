
const redactedFileName = "redacted_document.pdf";


// This event listner will listen to click event of download button
document.getElementById('downloadButton').addEventListener('click', async () => {
    try {
        const response = await fetch('/redact-document', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(),
        });

        if (!response.ok) {
            throw new Error('Redaction failed');
        }

        const fileBlob = await response.blob();
        const link = document.createElement('a');
        link.href = window.URL.createObjectURL(fileBlob);
        link.download = redactedFileName;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    } catch (error) {
        console.error('Error:', error.message);
    }
});