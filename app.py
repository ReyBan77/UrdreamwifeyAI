import os
import replicate
import streamlit as st
from dreamcoin_manager import get_dreamcoin_balance, unlock_nsfw

REPLICATE_API_TOKEN = st.secrets["REPLICATE_API_TOKEN"]
os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

def generate_waifu(prompt):
    model = replicate.models.get("fofr/realistic-vision-v5")
    version = model.versions.get("5f8fbe1c794607d1797b4cfcb7911f0e98cbe44e3d9b4e60e90cc3a3ef8e3d4b")
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
if st.form_submit_button("Generate Image 🌟"):
    if get_dreamcoin_balance() >= 100:  # Optional coin logic
with st.spinner("Summoning your waifu..."):
    try:
        image_url = generate_waifu(auto_prompt)
        st.image(image_url, caption="✨ Your Dream Waifu ✨", use_column_width=True)
        st.success("Your dream waifu has been generated!")
except Exception as e:
        st.error(f"Failed to generate image: {e}")
                
    else:
        st.warning("Not enough DreamCoins!")

if generate:
    coins = get_dreamcoin_balance()
  
    try:
        mage_url = generate_waifu(auto_prompt)
        st.image(image_url, caption="✨ Your Dream Waifu ✨", use_column_width=True)
        st.success("Your dream waifu has been generated!")
        except Exception as e:
        st.error(f"Failed to generate image: {e}")

    st.markdown(f"💰 **DreamCoins Balance:** `{coins}`")
