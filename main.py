import streamlit as st

st.set_page_config(page_title="Sidebar Layout", layout="wide")

# Sidebar content
with st.sidebar:
    # Multi-select box
    st.write("Choose model you want train")
    favorite_model = st.multiselect("", options=["LSTM", "BI-LSTM", "GPT", "Transformer", "BERT"], default=["GPT", "Transformer"])
    
    # First Section - Category
    st.write("---")  # Horizontal line
    st.header("Category")
    category_input = st.text_input(" ", placeholder="text input", key="category_input")
    col1, col2 = st.columns([6, 1])
    with col1:
        category_slider = st.slider(" ", min_value=0, max_value=10, value=5, label_visibility="collapsed", key="category_slider")
    with col2:
        category_number = st.number_input(" ", min_value=0, max_value=10, value=category_slider, label_visibility="collapsed", key="category_number")

    # Second Section - Model
    st.write("---")  # Horizontal line
    st.header("Model")
    model_input = st.text_input(" ", placeholder="text input", key="model_input")
    col3, col4 = st.columns([6, 1])
    with col3:
        model_slider = st.slider(" ", min_value=0, max_value=10, value=5, label_visibility="collapsed", key="model_slider")
    with col4:
        model_number = st.number_input(" ", min_value=0, max_value=10, value=model_slider, label_visibility="collapsed", key="model_number")

# Main content to display selected values
st.write("### Selected Values")
st.write(f"**Favorite model:** {', '.join(favorite_model)}")
st.write(f"**Category Input:** {category_input}")
st.write(f"**Category Slider:** {category_slider}")
st.write(f"**Model Input:** {model_input}")
st.write(f"**Model Slider:** {model_slider}")