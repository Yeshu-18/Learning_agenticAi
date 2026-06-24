import streamlit as st
from engine import ExtractionEngine

# Page Config
st.set_page_config(page_title="AI Dev Logger", page_icon="🚀")

st.title("🚀 AI Developer Logger")
st.subheader("Transform daily notes into professional content")

# Initialize Engine
engine = ExtractionEngine(model_name="gemma4:e4b") 


# Input Area
raw_input = st.text_area(
    "Paste your daily notes here:",
    placeholder="Today I: Learned ReAct, Studied MCP, Fixed a bug in the API...",
    height=200
)

if st.button("Generate Content ✨"):
    if not raw_input.strip():
        st.warning("Please paste some notes first!")
    else:
        with st.spinner("Gemma is thinking..."):
            try:
                # Run the extraction
                result = engine.process_notes(raw_input)

                st.success("Done! Here is your content:")
                st.divider()

                # Display Results in Columns
                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("### 🧠 Learning Topics")
                    for topic in result.learning_topics:
                        st.write(f"- {topic}")

                    st.markdown("### 💻 Coding Work")
                    for task in result.coding_work:
                        st.write(f"- {task}")

                with col2:
                    st.markdown("### 👔 LinkedIn Post")
                    st.info(result.linkedin_post)
                    st.button("Copy LinkedIn", key="copy_li", on_click=None) # Placeholder

                    st.markdown("### 🐙 GitHub Update")
                    st.code(result.github_update, language="text")

            except Exception as e:
                st.error(f"An error occurred: {e}")

# Sidebar Info
st.sidebar.title("Settings")
st.sidebar.info("Phase 1: MVP\n\nStatus: Operational\n\nModel: Gemma 2B")
