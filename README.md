## Flask Application Design for Complaint Gathering

### HTML Files

- **complaint_form.html**:
   - Contains an HTML form with inputs for collecting user complaints.
   - Includes fields for name, email, complaint description, and a submit button.

### Routes

- **@app.route('/')**:
   - Home page route that displays the complaint form (complaint_form.html).

- **@app.route('/submit_complaint', methods=['POST'])**:
   - Complaint submission route that handles the POST request from the complaint form.
   - It extracts complaint details from the request data and stores them in a database or other persistent storage.
   - Returns a confirmation message to the user.