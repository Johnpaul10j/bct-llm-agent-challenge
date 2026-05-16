# app.py
import streamlit as st
import requests

st.set_page_config(page_title="BCT LLM Agent", layout="wide")
st.title("🧠 BCT LLM Agent Challenge")
st.markdown("**DSN × Bluechip Technologies LLM Agent Challenge**")

# Allow user to change API URL
api_url = st.text_input("FastAPI Base URL", value="http://127.0.0.1:8000", help="Change if using Docker or deployed version")

tab1, tab2 = st.tabs(["Generate Review (Task A)", "Personalized Recommendations (Task B)"])

with tab1:
    st.subheader("Task 1 - Generate Review & Rating")
    persona = st.text_area("User Persona", "A 28-year-old Nigerian guy who loves tech gadgets, football, and spicy food", height=100)
    product = st.text_input("Product Name", "Samsung Galaxy A35")
    category = st.text_input("Category", "Smartphone")
    description = st.text_area("Product Description", "Mid-range smartphone with good camera and battery", height=80)
    
    if st.button("Generate Review", type="primary"):
        with st.spinner("Generating realistic review..."):
            try:
                response = requests.post(
                    f"{api_url}/generate_review",
                    json={
                        "persona": persona,
                        "product_name": product,
                        "category": category,
                        "product_description": description
                    },
                    timeout=30
                )
                if response.status_code == 200:
                    result = response.json()
                    st.success(f"⭐ Rating: {result.get('rating', 'N/A')}/5")
                    st.write(result.get('review_text', 'No review generated'))
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"Cannot connect to FastAPI at {api_url}. Make sure the backend is running.")

with tab2:
    st.subheader("Task 2 - Get Recommendations")
    persona2 = st.text_area("User Persona", "A 28-year-old Nigerian lady who is a foodie, loves fashion and Nollywood movies", height=100)
    n = st.slider("Number of Recommendations", 3, 8, 5)
    
    if st.button("Get Recommendations", type="primary"):
        with st.spinner("Generating recommendations..."):
            try:
                response = requests.post(
                    f"{api_url}/recommend",
                    json={"persona": persona2, "n_recommendations": n},
                    timeout=30
                )
                if response.status_code == 200:
                    result = response.json()
                    for rec in result.get("recommendations", []):
                        st.write(f"**{rec.get('item_name')}**")
                        st.write(rec.get('reason'))
                        st.caption(rec.get('category', ''))
                        st.divider()
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"Cannot connect to FastAPI at {api_url}.")

st.caption("Built for DSN X BCT LLM Agent Challenge")