# Feature Planing to Download Redacted Documents

## Overview

This README contains a guide on the conceptualization, technical execution, security measures, user experience, and code structure for implementing this feature.

## Conceptualization

### User Flow

1. Redaction process is initiated by users from the document view page.
2. The redaction process will be done on the server side, We also need to ensure the original document remains unchanged.
3. Users are presented with the redacted document.

### Technical Execution

1. **Server-Side Processing:**
   - Create a server-side method that allows you to remove redact sensitive data from PDFs.
   - Use a PDF processing library to alter the document and hide specified areas.
   - created an endpoint that should return redacted file.

2. **Annotation Handling:**
   - Include annotations, identify and hide sensitive information.
   - Validate the document to check that the redaction process does not affect the non-sensitive aread.

3. **User Interface:**
   - Add "Download Redacted" button within the document view page.

4. **File Generation:**
   - Generate redacted file dynamically on user request
   - store redacted files in db. (Note: there should be only one latest copy of redacted file in db always)

### Security Measures

1. **Data Encryption:**
   - Encrypt data before stoting in database.
   - Encrypt data for secure transmission.

2. **Permanent Redaction:**
   - create a process to permanently remove redacted information from the server after the redacted document is downloaded.
   - If we donot need a copy of redacted data in database we can trigger a function to remove redacted file from the database

## User Experience

1. **User Guidance:**
   - Provide clear instructions on what does "Redacted Document Download" button do.
   - Display confirmation messages upon successful redaction and download.

## Code

### Assumptions

- I assumed that that we have PDF processing library for server-side redaction.
- Assumed a secure database is integrated for the storage of redacted files.

### Considerations for Maintainability and Scalability

- Code should be well documented.
- Should print logs for tracking redaction process.
- Must have error handling
- Should be scalable, incase of increase user demand.  

### Potential Challenges and Strategies

1. **Performance Concerns:**
   - Challenge: Performance can get impacted if we Redacting large documents.
   - Strategy: asynchronous/perallel processing to handle large documents that should not effect user experience.

2. **Annotation Complexity:**
   - Challenge: Annotations may contain complex structures.
   - Strategy: Look for PDF processing libraries compare pros and cons use the one that fits best for our use case.

3. **File Security:**
   - Challenge: Secure transmission of redacted files.
   - Strategy: Implement encryption

