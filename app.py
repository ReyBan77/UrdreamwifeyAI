import os
import replicate
from dotenv import load_dotenv
import streamlit as st
import replicate
from dreamcoin_manager import get_dreamcoin_balance, unlock_nsfw

REPLICATE_API_TOKEN = st.secrets["REPLICATE_API_TOKEN"]
os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

def generate_waifu(prompt):
    model = replicate.models.get("cjwbw/anything-v4.0")
    version = model.versions.get("f5a17c3d56499899a9c3c0c4fd0bcd87a4b96b4c16f0fdfcda4e9b9c1ab36a5d")
    output = version.predict(prompt=prompt, width=512, height=512, num_outputs=1)
    return output[0]

st.title("🌸 Dream Waifu Generator")

with st.form("dream_form"):
    hairstyle = st.selectbox("Hairstyle", ["blonde", "brunette", "redhead", "pink"])
    outfit = st.selectbox("Outfit", ["casual", "lingerie", "armor", "wedding dress"])
    scene = st.selectbox("Scene", ["beach", "bedroom", "cafe"])
    style = st.selectbox("Style", ["Realistic", "Anime", "Sketch"])
    gender = st.selectbox("Gender", ["Female", "Male", "Androgynous"])
    nsfw_toggle = st.checkbox("🔞 Unlock NSFW mode (200 coins)")

    auto_prompt = f"{style} {gender} with {hairstyle} hair wearing {outfit} in a {scene}"
    st.markdown(f"**Auto-generated Prompt:** `{auto_prompt}`")

    generate = st.form_submit_button("Generate Image 💫")

if generate:
    coins = get_dreamcoin_balance()
    if nsfw_toggle and coins < 200:
        st.error("You need 200 DreamCoins to unlock NSFW mode.")
    else:
        if nsfw_toggle:
            unlock_nsfw()

        with st.spinner("Generating your waifu..."):
            try:
                image_url = generate_waifu(auto_prompt)
                st.image(image_url, caption="✨ Your Dream Waifu ✨", use_column_width=True)
                st.success("Your dream waifu has been generated!")
            except Exception as e:
                st.error(f"Failed to generate image: {e}")

    st.markdown(f"💰 **DreamCoins Balance:** `{coins}`")
