import streamlit as st
import stripe

stripe.api_key = "sk_test_your_secret_key"  # Replace with your real key

# Product-to-price mapping
price_ids = {
    "100 Coins – $5": "price_123abc",  # Replace with real Price IDs
    "250 Coins – $10": "price_456def",
    "500 Coins – $18": "price_789ghi",
    "1000 Coins – $30": "price_101xyz"
}

st.set_page_config(page_title="💳 DreamCoin Vault", layout="centered")

st.title("🏦 DreamCoin Vault Shop")
st.markdown("Buy DreamCoins to unlock your ultimate waifu fantasy 💖")

package = st.selectbox("Choose your DreamCoin bundle", list(price_ids.keys()))

if st.button("Proceed to Checkout"):
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price": price_ids[package],
                "quantity": 1,
            }],
            mode="payment",
            success_url="https://yourdomain.com/success",
            cancel_url="https://yourdomain.com/cancel",
        )
        st.success("Redirecting to checkout...")
        st.markdown(f"[Click here if not redirected automatically]({session.url})")
    except Exception as e:
        st.error(f"Stripe error: {e}")
