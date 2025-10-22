import streamlit as st
import pandas as pd
import requests
from io import BytesIO
from PIL import Image

# Configure page settings
st.set_page_config(
    page_title="BillYourBite", 
    page_icon="🍽️", 
    layout="centered"
)

# --- DATA LOADING ---
@st.cache_data
def load_menu():
    """Load and cache menu data from CSV file."""
    try:
        return pd.read_csv("mess_menu.csv")
    except FileNotFoundError:
        st.error("❌ Menu data file not found. Please ensure mess_menu.csv exists.")
        st.stop()
    except pd.errors.EmptyDataError:
        st.error("❌ Menu data file is empty or corrupted.")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error loading menu data: {str(e)}")
        st.stop()

@st.cache_data
def load_thumbnail():
    """Load and cache the app thumbnail image."""
    thumbnail_url = "https://raw.githubusercontent.com/MeeraYasmin/BillYourBite/main/asset/BillYourBite%20Thumbnail.png"
    try:
        response = requests.get(thumbnail_url, timeout=10)
        response.raise_for_status()
        return BytesIO(response.content)
    except requests.RequestException:
        return None


def calculate_bill(selected_dishes, quantities, dishes_df):
    """Calculate bill items and total cost."""
    bill_items = []
    total = 0.0
    
    for dish in selected_dishes:
        try:
            price = float(dishes_df[dishes_df["Dish_Name"] == dish]["Average_Price"].values[0])
            qty = int(quantities[dish])
            subtotal = round(price * qty, 2)
            total += subtotal
            bill_items.append({
                "Dish": dish, 
                "Unit Price": f"₹{price:.2f}", 
                "Quantity": qty, 
                "Total": f"₹{subtotal:.2f}"
            })
        except (IndexError, ValueError) as e:
            st.error(f"❌ Error calculating price for {dish}: {str(e)}")
            continue
    
    return bill_items, round(total, 2)


def render_sidebar(menu):
    """Render the sidebar with student and meal selection."""
    st.sidebar.header("🎓 Student Information")
    with st.sidebar.form("student_form"):
        name = st.text_input("Full Name", placeholder="Enter your name")
        reg_no = st.text_input("Registration Number", placeholder="e.g., 123456789")
        dept = st.selectbox("Department", [
            "CSE", "CSE-AIDS", "CSE-IOT", "CSE-CSBT", "IT", "ICT", "RAI", "ECE", "EEE", "VLSI", "Mech", "Civil", "Aero", "Biotech", "BioEngg", "Other"
        ])
        year = st.selectbox("Year of Study", ["I", "II", "III", "IV","V"])
        submitted = st.form_submit_button("Save Student Info")
    
    if submitted:
        if not name or not reg_no:
            st.sidebar.warning("⚠️ Please enter both name and registration number.")
        else:
            st.sidebar.success(f"✅ Welcome, {name} ({reg_no}) - {dept}, Year {year}")

    st.sidebar.header("🍴 Build Your Bill")
    
    week = st.sidebar.selectbox(
        "Step 1: Week Type", 
        menu['Week_Type'].unique(),
        help="Select whether it's an odd or even week"
    )
    
    day = st.sidebar.selectbox(
        "Step 2: Day", 
        menu['Day'].unique(),
        help="Choose the day of the week"
    )
    
    meal = st.sidebar.selectbox(
        "Step 3: Meal", 
        menu['Meal_Type'].unique(),
        help="Select breakfast, lunch, snacks, or dinner"
    )
    
    return name, reg_no, dept, year, week, day, meal


def render_main_content():
    """Render the main application content."""
    # Load data
    menu = load_menu()
    
    # Display thumbnail
    thumbnail = load_thumbnail()
    if thumbnail:
        st.image(thumbnail, use_container_width=True)
    else:
        st.warning("⚠️ Thumbnail could not be loaded.")
    
    # Sidebar: student + meal info
    name, reg_no, dept, year, week, day, meal = render_sidebar(menu)

    # Filter dishes based on selections
    dishes_df = menu[
        (menu['Week_Type'] == week) & 
        (menu['Day'] == day) & 
        (menu['Meal_Type'] == meal)
    ]
    
    if dishes_df.empty:
        st.warning("⚠️ No dishes available for the selected combination.")
        return
    
    dish_options = dishes_df['Dish_Name'].tolist()
    
    selected_dishes = st.multiselect(
        "🍲 Select Your Dishes", 
        dish_options, 
        help="Choose everything you ate for this meal!"
    )
    
    # Quantity form
    with st.form("quantities_form"):
        if selected_dishes:
            st.subheader("📝 Enter Quantity for Each Dish")
            
            num_cols = min(len(selected_dishes), 3)
            qty_cols = st.columns(num_cols)
            quantities = {}
            
            for i, dish in enumerate(selected_dishes):
                with qty_cols[i % num_cols]:
                    quantities[dish] = st.number_input(
                        f"{dish}", 
                        min_value=1, 
                        max_value=10, 
                        value=1, 
                        step=1, 
                        key=f"qty_{dish}",
                        help=f"Quantity for {dish} (1-10)"
                    )
            
            bill_items, total = calculate_bill(selected_dishes, quantities, dishes_df)
            
            if bill_items:
                st.divider()
                st.subheader("💰 Your Bill Summary")
                bill_df = pd.DataFrame(bill_items)
                st.dataframe(bill_df, use_container_width=True, hide_index=True)
                st.markdown(
                    f"<h3 style='color: #00897b; text-align: center;'>Total: ₹{total:.2f}</h3>", 
                    unsafe_allow_html=True
                )
            
            submit = st.form_submit_button("🎉 Generate Bill & Show Extras")
        else:
            st.info("👆 Please select some dishes to generate your bill!")
            submit = st.form_submit_button("🎉 Generate Bill & Show Extras", disabled=True)
    
    # Handle form submission
    if submit and selected_dishes:
        st.balloons()
        st.success("✅ Your bill has been generated successfully!")
        
        # Student summary banner
        if name and reg_no:
            st.markdown(
                f"<div style='background-color:#e8f5e9;padding:10px;border-radius:10px;text-align:center;'>"
                f"<b>Student:</b> {name} ({reg_no}) &nbsp;&nbsp;|&nbsp;&nbsp; "
                f"<b>Department:</b> {dept} &nbsp;&nbsp;|&nbsp;&nbsp; "
                f"<b>Year:</b> {year}</div>", unsafe_allow_html=True
            )
        
        # Rating and review section
        with st.expander("🌟 Rate & Review Your Meal Experience", expanded=True):
            st.write("Help us improve the mess experience by rating your dishes:")
            
            for dish in selected_dishes:
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.markdown(f"**{dish}**")
                    st.slider(
                        f"Rate {dish}", 
                        1, 5, 
                        value=5, 
                        key=f"star_{dish}",
                        help="1 = Poor, 5 = Excellent"
                    )
                with col2:
                    st.text_area(
                        f"Feedback for {dish}", 
                        key=f"ta_{dish}",
                        placeholder="Share your thoughts about this dish...",
                        height=60
                    )
        
        st.info("🙏 Thanks for helping improve the mess experience!")
        
        # Download functionality
        if bill_items:
            bill_df = pd.DataFrame(bill_items)
            csv_data = bill_df.to_csv(index=False).encode('utf-8')
            filename = f"billyourbite_summary_{name}_{reg_no}_{week}_{day}_{meal}.csv".replace(" ", "_")
            
            download = st.download_button(
                "⬇️ Download Bill Summary (CSV)",
                csv_data,
                filename,
                "text/csv",
                help="Download your personalized bill summary"
            )
            
            if download:
                st.success("📄 Your personalized bill summary has been downloaded!")

if __name__ == "__main__":
    render_main_content()

# Footer
st.markdown("""
---
<center>
🧑‍💻 <em>Made with love for SASTRA students.<br/>Eat fair, pay fair – every bite counts!</em>
</center>
""", unsafe_allow_html=True)
