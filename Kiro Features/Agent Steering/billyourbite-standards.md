# BillYourBite Development Standards

## Project Overview
BillYourBite is a Streamlit-based mess billing application for SASTRA students that helps calculate meal costs based on menu selections and includes student information management.

## Code Standards

### Python/Streamlit Guidelines
- Use `@st.cache_data` for data loading functions
- Maintain consistent sidebar organization with student info + meal selection
- Use semantic emojis for UI elements (🍽️, 🍲, 💰, 🎓, etc.)
- Follow PEP 8 naming conventions
- Keep functions focused and single-purpose
- Implement proper form validation and error handling

### UI/UX Principles
- Maintain centered layout with `layout="centered"`
- Use consistent color scheme (primary: #00897b for totals, #e8f5e9 for student info)
- Provide helpful tooltips and user guidance
- Include error handling with user-friendly messages
- Use balloons() for positive feedback
- Ensure responsive design with proper column layouts
- Student information should be prominently displayed when available

### Data Handling & Security
- CSV data should be cached and validated
- Price calculations must be accurate to 2 decimal places
- Support both Odd/Even week types
- Validate user inputs (quantities 1-10, student info format)
- **Student Data Privacy**: Never log or inappropriately cache student information
- Sanitize all student inputs to prevent injection attacks
- Use secure file naming that includes student info appropriately

### Student Information Requirements
- Full Name: Required, non-empty string
- Registration Number: Required, alphanumeric format
- Department: Predefined list of SASTRA departments
- Year of Study: Roman numerals I-V
- Form validation must prevent submission with incomplete data
- Student info should enhance file naming for downloads

### File Structure
```
├── app.py              # Main Streamlit application
├── mess_menu.csv       # Menu data source
├── requirements.txt    # Dependencies (if needed)
└── .kiro/             # Kiro IDE configuration
```

## Feature Development Process
1. Create spec for new features
2. Update menu data if needed
3. Test with sample data including student scenarios
4. Validate calculations and student data handling
5. Test security and privacy compliance
6. Update documentation

## Testing Guidelines
- Test all week/day/meal combinations
- Verify price calculations with various quantities
- Test student information form validation
- Test edge cases (no selections, max quantities, invalid student data)
- Validate CSV download functionality with student-specific naming
- Test responsive design on different screen sizes
- Verify accessibility compliance for forms and inputs