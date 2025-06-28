import stripe
from flask import Flask, request

app = Flask(__name__)
endpoint_secret = "whsec_..."  # Replace with your real webhook secret

@app.route("/webhook", methods=["POST"])
def webhook():
    payload = request.data
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except stripe.error.SignatureVerificationError as e:
        return f"Webhook signature verification failed: {e}", 400

    # Handle event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print("✅ Payment complete:", session)

        # Here you would add DreamCoins to user's account

    return '', 200

if __name__ == "__main__":
    app.run(port=4242)
