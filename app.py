import streamlit as st
import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", feedback
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", feedback
    else:
        return "❌ Weak Password - Improve it using the suggestions above.", feedback

def suggest_strong_password():
    length = 12
    characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        "!@#$%^&*"
    )
    
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit App Interface
st.title("🔐 Password Strength Meter")

# Input for password
password = st.text_input("Enter your password:", type='password')

# Display password strength and feedback instantly
if password:
    strength_message, feedback = check_password_strength(password)
    st.success(strength_message)
    for note in feedback:
        st.error(note)
else:
    st.warning("Please enter a password to check.")

# Suggest a strong password
if st.checkbox("Show a suggested strong password"):
    suggested_password = suggest_strong_password()
    st.write(f"Suggested Strong Password: **{suggested_password}**")