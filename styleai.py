import streamlit as st
from PIL import Image

# Page Config
st.set_page_config(page_title="StyleAI - Fashion Advisor", layout="centered")

# Title
st.title("👗 StyleAI - Personal Fashion Assistant")
st.subheader("AI-Based Gender-Specific Fashion Recommendations")

# Upload Photo
st.markdown("### 📸 Upload Your Photo")
photo = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])

if photo:
    image = Image.open(photo)
    st.image(image, caption="Uploaded Photo", width=250)

# Gender Preference (Fixed to Female for this project)
gender = "Female"

# Dress Code Selection
st.markdown("### 👚 Select Dress Code")
dress_code = st.selectbox(
    "Choose Occasion",
    ["Formal", "Business", "Casual", "Party"]
)

# Skin Tone Input
st.markdown("### 🎨 Select Your Skin Tone")
skin_tone = st.selectbox(
    "Choose Skin Tone",
    ["Fair", "Wheatish", "Medium", "Olive", "Dark"]
)

# Generate Button
if st.button("✨ Generate Recommendations"):

    st.markdown("---")
    st.header("💎 Your Personalized Style Guide")

    # ---------- Outfit Recommendations ----------
    st.subheader("👗 Outfit Suggestions")

    if dress_code == "Formal":
        top = "Silk blouse / Formal shirt"
        bottom = "Pencil skirt / Tailored trousers"
        shoes = "Heels / Closed pumps"

    elif dress_code == "Business":
        top = "Blazer + Shirt"
        bottom = "Formal pants / Skirt"
        shoes = "Block heels / Loafers"

    elif dress_code == "Casual":
        top = "T-shirt / Crop top"
        bottom = "Jeans / Skirt"
        shoes = "Sneakers / Flats"

    else:  # Party
        top = "Sequin top / Off-shoulder top"
        bottom = "Mini skirt / Palazzos"
        shoes = "Stilettos / Heeled sandals"

    st.write(f"*Top:* {top}")
    st.write(f"*Bottom:* {bottom}")
    st.write(f"*Shoes:* {shoes}")

    # ---------- Hairstyle ----------
    st.subheader("💇 Hairstyle Suggestions")

    hairstyles = {
        "Fair": "Soft curls / Side-parted straight hair",
        "Wheatish": "Layered waves / Ponytail",
        "Medium": "Beach waves / Braids",
        "Olive": "Sleek bun / Bob cut",
        "Dark": "Natural curls / High puff"
    }

    maintenance = {
        "Fair": "Use heat protectant and mild shampoo",
        "Wheatish": "Apply hair serum weekly",
        "Medium": "Oil massage twice a week",
        "Olive": "Deep conditioning monthly",
        "Dark": "Moisturize curls regularly"
    }

    st.write(f"*Recommended Style:* {hairstyles[skin_tone]}")
    st.write(f"*Maintenance Tip:* {maintenance[skin_tone]}")

    # ---------- Accessories ----------
    st.subheader("💍 Accessories")

    st.write("*Earrings:* Studs / Hoops")
    st.write("*Necklace:* Pendant / Choker")
    st.write("*Bracelet:* Charm / Bangles")
    st.write("*Watch:* Slim analog watch")

    # ---------- Color Palette ----------
    st.subheader("🎨 Color Palette Guidance")

    colors = {
        "Fair": ("Pastel Pink", "Lavender", "Silver"),
        "Wheatish": ("Peach", "Olive Green", "Gold"),
        "Medium": ("Teal", "Mustard", "Rose Gold"),
        "Olive": ("Emerald", "Navy", "Copper"),
        "Dark": ("Royal Blue", "Burgundy", "Bronze")
    }

    primary, secondary, accent = colors[skin_tone]

    st.write(f"*Primary Color:* {primary}")
    st.write(f"*Secondary Color:* {secondary}")
    st.write(f"*Accent Color:* {accent}")

    # ---------- Explanation ----------
    st.subheader("📝 Why This Works for You")

    explanation = f"""
    Your *{skin_tone} skin tone* pairs well with *{primary} and {secondary} shades*,
    which enhance your natural complexion.  
    The *{accent} accent color* adds elegance and contrast.

    The selected *{dress_code} outfit* balances comfort and style,
    while the recommended hairstyle highlights your facial features.

    These accessories complement your outfit without overpowering it,
    giving you a polished and confident appearance.
    """

    st.success(explanation)

    # ---------- Footer ----------
    st.markdown("---")
    st.caption("✨ Powered by StyleAI | Personalized Fashion System")