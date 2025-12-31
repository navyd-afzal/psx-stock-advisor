import streamlit as st
from openai import OpenAI

st.title("📊 PSX Stock Advisor")

api_key = st.text_input("Enter OpenAI API Key", type="password")

stock = st.text_input("Stock Name")
last_close = st.number_input("Last Closing Price", min_value=0.0)
current_price = st.number_input("Current Price", min_value=0.0)

if st.button("Analyze"):
    if not api_key:
        st.error("API key required")
    else:
        client = OpenAI(api_key=api_key)

        prompt = f"""
You are a Pakistan Stock Exchange analyst.

Stock: {stock}
Last Close: {last_close}
Current Price: {current_price}

Analyze trend and give BUY / HOLD / AVOID with target & stop loss.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        st.write(response.choices[0].message.content)
