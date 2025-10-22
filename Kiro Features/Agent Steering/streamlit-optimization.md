---
inclusion: fileMatch
fileMatchPattern: "*.py"
---

# Streamlit Optimization Guidelines for BillYourBite

## Performance Optimization
- Use `@st.cache_data` for expensive operations (CSV loading, calculations)
- Implement `@st.cache_resource` for one-time resource initialization
- Use `st.session_state` for maintaining state across reruns
- Minimize widget recreation in loops

## Code Organization
```python
# Recommended structure
def load_data():
    """Load and cache menu data"""
    pass

def calculate_bill(selected_dishes, quantities):
    """Pure function for bill calculations"""
    pass

def render_ui():
    """Main UI rendering logic"""
    pass

if __name__ == "__main__":
    render_ui()
```

## Error Handling Patterns
```python
try:
    # Risky operation
    result = risky_function()
except SpecificException as e:
    st.error(f"User-friendly error message: {str(e)}")
    st.stop()
```

## State Management
- Use `st.session_state` for form data persistence
- Store student information in session state after validation
- Clear state appropriately on navigation
- Handle browser refresh gracefully
- Avoid storing sensitive student data in session state unnecessarily

## Form Handling Best Practices
```python
# Use forms to prevent constant reruns
with st.form("student_form"):
    # Form inputs here
    submitted = st.form_submit_button("Save")
    
if submitted:
    # Validation and processing
    if validate_student_data(name, reg_no):
        st.session_state.student_info = {...}
```

## UI Best Practices
- Use `st.columns()` for responsive layouts (max 3 columns for readability)
- Implement proper loading states with `st.spinner()`
- Add `help` parameters to widgets for user guidance
- Use `st.expander()` for optional content like reviews
- Display student information prominently when available
- Use consistent styling for student info banners

## Student Data UI Patterns
```python
# Student info display
if student_info:
    st.markdown(
        f"<div style='background-color:#e8f5e9;padding:10px;border-radius:10px;'>"
        f"Student: {name} ({reg_no})</div>", 
        unsafe_allow_html=True
    )
```