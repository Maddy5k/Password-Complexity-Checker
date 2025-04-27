import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    strength = {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'number': bool(re.search(r'[0-9]', password)),
        'special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
    }

    feedback = []

    if not strength['length']:
        feedback.append("Password must be at least 8 characters long.")
    if not strength['uppercase']:
        feedback.append("Password must contain at least one uppercase letter.")
    if not strength['lowercase']:
        feedback.append("Password must contain at least one lowercase letter.")
    if not strength['number']:
        feedback.append("Password must contain at least one number.")
    if not strength['special']:

