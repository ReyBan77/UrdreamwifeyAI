import streamlit as st
from prompt_builder import build_prompt
from gallery import save_image_to_gallery
from dreamcoin_manager import get_dreamcoin_balance, unlock_nsfw
from email_capture import capture_email
from utils import get_styles
from email_capture import capture_email

st.set_page_config(page_title="URDreamWifeyAI", layout="centered")

st.markdown(get_styles(), unsafe_allow_html=True)

st.title("💘 URDreamWifeyAI")
st.caption("Design your dream waifu. Your prompt. Your fantasy. UR rules.")

with st.form("dream_form"):
    hairstyle = st.selectbox("Hairstyle", ["blonde", "brunette", "redhead", "pink", "black"])
    outfit = st.selectbox("Outfit", ["casual", "lingerie", "armor", "wedding dress"])
    scene = st.selectbox("Scene", ["bedroom", "beach", "fantasy temple", "school", "cafe"])
    style = st.selectbox("Style", ["Realistic", "Anime", "Sketch", "Cyberpunk"])
    gender = st.selectbox("Gender", ["Female", "Male", "Androgynous"])

    auto_prompt = build_prompt(hairstyle, outfit, scene, style, gender)
    st.markdown(f"**Auto-generated prompt:** `{auto_prompt}`")

    nsfw_toggle = st.checkbox("🔞 Unlock NSFW mode (200 coins)")
    generate = st.form_submit_button("Generate Image 🧃")

coins = get_dreamcoin_balance()

if generate:
    if nsfw_toggle and coins < 200:
        st.error("You need 200 DreamCoins to unlock NSFW mode.")
    else:
        if nsfw_toggle:
            unlock_nsfw()

        with st.spinner("Generating your waifu..."):
            image_url = f"https://via.placeholder.com/512x512?text={auto_prompt.replace(' ', '+')}"
            st.image(image_url)  # TEMP MOCK

        save_image_to_gallery(auto_prompt.encode(), "test_user")
        st.success("Your dream waifu has been generated!")

st.divider()
st.markdown(f"🌕 **DreamCoins Balance:** `{coins}`")
capture_email()
