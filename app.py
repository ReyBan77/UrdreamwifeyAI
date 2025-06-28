import streamlit as st
import requests
import replicate
import os

# Set page config
st.set_page_config(page_title="URDreamWifeAI", layout="centered")

# Header
st.markdown("# 💍 URDreamWifeAI")
st.markdown("Design your dream waifu. Your prompt. Your fantasy. UR rules.")

# Prompt input
prompt = st.text_input("Describe your dream wife ✨", placeholder="e.g., elegant blonde in a flowing white dress")

# Style and gender
col1, col2 = st.columns(2)
with col1:
    style = st.selectbox("Style", ["Realistic", "Anime", "Cartoon"])
with col2:
    gender = st.selectbox("Gender", ["Female", "Male", "Surprise Me"])

# Add NSFW toggle preview (doesn't trigger anything yet)
nsfw_toggle = st.checkbox("🔞 Unlock NSFW mode (coming soon...)", value=False, disabled=True)

# Generate button
if st.button("Generate Image 💫") and prompt:
    with st.spinner("Summoning your dream waifu..."):
        try:
            # Replace with your Replicate API token
            replicate_token = os.getenv("REPLICATE_API_TOKEN", "your_replicate_api_key_here")
            os.environ["REPLICATE_API_TOKEN"] = replicate_token

            model = replicate.models.get("stability-ai/stable-diffusion")
            version = model.versions.get("db21e45e5b6e4b01a15fc7c85f7af054c9db3d963fdb1378bcf003e437c1d47f")

            output = version.predict(prompt=prompt)

            st.image(output[0], caption="Here she is 💖", use_column_width=True)
        except Exception as e:
            st.error(f"Failed to generate image: {e}")
else:
    st.caption("Enter a dreamy prompt to begin the magic...")

# Footer
st.markdown("---")
st.markdown("🔓 Want NSFW mode? Unlock the vault soon... 💋 Coming soon: AIWifey2Life mode.")
