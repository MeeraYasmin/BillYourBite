---
inclusion: fileMatch
fileMatchPattern: "app.py"
---

# Student Data Handling Guidelines for BillYourBite

## Data Collection Standards
- **Minimal Data**: Only collect necessary student information
- **Required Fields**: Name, Registration Number, Department, Year
- **Optional Fields**: Avoid collecting unnecessary personal data

## Form Validation Rules
```python
# Student name validation
if not name or len(name.strip()) < 2:
    st.warning("Please enter a valid full name")

# Registration number validation  
if not reg_no or not reg_no.isalnum():
    st.warning("Registration number should be alphanumeric")

# Department validation
valid_departments = ["CSE", "CSE-AIDS", "CSE-IOT", "CSE-CSBT", "IT", "ICT", "RAI", "ECE", "EEE", "VLSI", "Mech", "Civil", "Aero", "Biotech", "BioEngg", "Other"]
```

## Security Best Practices
- **Input Sanitization**: Clean all user inputs
- **No Logging**: Never log student personal information
- **Session Management**: Use `st.session_state` appropriately
- **File Naming**: Include student info in downloads but avoid exposing sensitive data

## Privacy Compliance
- Display student information only when explicitly provided
- Use student data only for bill generation and file naming
- Provide clear feedback about data usage
- Ensure data is not persisted beyond the session

## UI/UX for Student Forms
- Use `st.form()` for student information to prevent constant reruns
- Provide clear placeholders and help text
- Show success confirmation when student info is saved
- Display student summary prominently in bill generation

## Error Handling Patterns
```python
# Graceful form validation
with st.sidebar.form("student_form"):
    name = st.text_input("Full Name", placeholder="Enter your name")
    if submitted and not name:
        st.sidebar.error("Name is required")
        return None, None, None, None
```

## File Download Security
- Sanitize filenames to prevent path traversal
- Use student info appropriately in naming
- Format: `billyourbite_summary_{name}_{reg_no}_{week}_{day}_{meal}.csv`
- Replace spaces and special characters safely