import streamlit as st
import requests
import replicate
import os

st.set_page_config(page_title="URDreamWifeAI", layout="centered")

st.markdown("# 💍 URDreamWifeAI")
st.caption("Design your dream waifu. Your prompt. Your fantasy. UR rules.")

if "coins" not in st.session_state:
    st.session_state.coins = 100
if "gallery" not in st.session_state:
    st.session_state.gallery = []
if "nsfw_unlocked" not in st.session_state:
    st.session_state.nsfw_unlocked = False

st.markdown(f"### 💰 DreamCoins: `{st.session_state.coins}`")

# Prompt builder
hairstyle = st.selectbox("Hairstyle", ["blonde", "brunette", "pink", "black", "surprise me"])
outfit = st.selectbox("Outfit", ["lingerie", "bikini", "elegant dress", "school uniform"])
scene = st.selectbox("Scene", ["bedroom", "beach", "cyberpunk city", "fantasy forest"])

style = st.selectbox("Style", ["Realistic", "Anime", "Cartoon"])
gender = st.selectbox("Gender", ["Female", "Male", "Surprise Me"])

prompt = f"{hairstyle} {gender.lower()} in {outfit}, {scene}, {style.lower()} style"

st.markdown(f"**Auto-generated prompt:** _{prompt}_")

if not st.session_state.nsfw_unlocked:
    st.checkbox("🔞 Unlock NSFW mode (200 coins)", value=False, disabled=True)
    st.warning("NSFW mode is locked. Unlock it with DreamCoins.")

if st.button("🎨 Generate Waifu (10 coins)"):
    if st.session_state.coins < 10:
        st.error("Not enough DreamCoins.")
    else:
        with st.spinner("Dreaming up your waifu..."):
            try:
                replicate_token = os.getenv("REPLICATE_API_TOKEN", "your_replicate_api_key_here")
                os.environ["REPLICATE_API_TOKEN"] = replicate_token

                model = replicate.models.get("stability-ai/stable-diffusion")
                version = model.versions.get("db21e45e5b6e4b01a15fc7c85f7af054c9db3d963fdb1378bcf003e437c1d47f")
                output = version.predict(prompt=prompt)

                st.image(output[0], caption="Here she is 💖", use_column_width=True)
                st.session_state.coins -= 10
                st.session_state.gallery.append(output[0])
            except Exception as e:
                st.error(f"Generation error: {e}")

if st.button("🔓 Unlock NSFW Mode"):
    if st.session_state.coins < 200:
        st.error("You need 200 DreamCoins to unlock NSFW Mode.")
    else:
        st.session_state.coins -= 200
        st.session_state.nsfw_unlocked = True
        st.success("NSFW Mode unlocked! Welcome to AIWifey2Life 💋")

if st.session_state.gallery:
    st.markdown("### 🖼️ Your Waifu Gallery")
    for img in st.session_state.gallery[-5:][::-1]:
        st.image(img, width=400)

st.markdown("---")
st.markdown("📥 Want NSFW mode? Unlock the vault. 💋 Coming soon: AIWifey2Life mode.")
