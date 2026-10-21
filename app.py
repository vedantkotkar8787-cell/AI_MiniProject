import streamlit as st
from data import load_books
from recommender import get_rule_based_recommendations

# Load dataset
books_data = load_books()

# Page Configuration
st.set_page_config(page_title="Book Recommendation Engine", page_icon="📚", layout="centered")

st.title("📚 Rule-Based Book Recommender (Pure Python)")
st.write("Find your next read based on custom rules tailored to your current preferences.")

st.markdown("---")

# Sidebar Controls (Extracting unique values using Python sets)
st.sidebar.header("Define Your Rules")

genres = ["Any"] + sorted(list(set(b["genre"] for b in books_data)))
moods = ["Any"] + sorted(list(set(b["mood"] for b in books_data)))
lengths = ["Any"] + sorted(list(set(b["length"] for b in books_data)))

selected_genre = st.sidebar.selectbox("1. Select Genre", genres)
selected_mood = st.sidebar.selectbox("2. Select Mood", moods)
selected_length = st.sidebar.selectbox("3. Select Preferred Length", lengths)

# Recommendation Trigger
if st.sidebar.button("Get Recommendations 🚀"):
    results = get_rule_based_recommendations(books_data, selected_genre, selected_mood, selected_length)
    
    st.subheader("💡 Recommended Books")
    
    if not results:
        st.warning("No books found matching all selected criteria. Try relaxing one of your filters!")
    else:
        st.success(f"Found {len(results)} book(s) matching your rules:")
        
        for book in results:
            with st.expander(f"📖 **{book['title']}** by {book['author']} ⭐ {book['rating']}/5"):
                st.write(f"**Genre:** {book['genre']} | **Mood:** {book['mood']} | **Length:** {book['length']}")
                st.write(f"**Summary:** {book['description']}")
else:
    st.info("👈 Use the controls in the sidebar to define your rules and click **Get Recommendations**.")

st.markdown("---")

# Database Preview
with st.expander("🔍 View All Books in Database"):
    for book in books_data:
        st.markdown(f"- **{book['title']}** ({book['genre']}) - ⭐ {book['rating']}")