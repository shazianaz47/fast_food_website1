import streamlit as st

# st.title("Hello ShazCo!")
# st.write("Welcome to your fast food website.")
st.set_page_config(page_title="ShazCo Fast Food", layout="wide")

# Header
st.markdown("<h1 style='text-align: center; color: #E63946;'>Welcome to ShazCo 🍔</h1>", unsafe_allow_html=True)
st.markdown("### Flavor Meets Fast – Taste the Difference!")

# Navigation Menu (Optional)
menu = st.sidebar.selectbox("Navigate", ["Home", "Menu", "Order Now", "About Us","Why ShazCo?", "Contact"])

# Home Page
if menu == "Home":
    st.image("images/hero-banner.jpg", use_container_width=True)
    st.subheader("🔥 Today's Special Combos")
    st.write("- **Spicy Zinger + Fries + Drink** – Rs.499")
    st.write("- **Family Feast (2 Burgers, Fries, 2 Drinks)** – Rs.899")
    st.markdown("👉 **Order Now and Get Free Delivery!**")

# Menu Page
elif menu == "Menu":
    st.markdown("## 📋 Our Menu")
    st.markdown("#### Flavor Meets Fast – Taste the Difference!")

    # Menu Items List (for easy editing/looping)
    menu_items = [
        ("images/menu_sample2.jpg", "🍔 Zinger Burger", 400),
        ("images/menu_sample3.jpg", "🌯 Shawarma Wrap", 200),
        ("images/menu_sample4.jpg", "🍟 Masala Fries", 150),
        ("images/menu_sample5.jpg", "🥤 Cold Drink", 80),
        ("images/menu_sample6.jpg", "🌮 Taco", 400),
        ("images/menu_sample7.jpg", "🥟 Momos", 200),
        ("images/menu_sample8.jpg", "🍗 Chicken Nuggets", 150),
        ("images/menu_sample9.jpg", "🍖 Fried Chicken", 80),
        ("images/menu_sample10.jpg", "🍕 Pizza", 1500),
        ("images/menu_sample11.jpg", "🥪 Club Sandwich", 999),
        ("images/menu_sample12.jpg", "🔥 Tandoori Pizza", 990),
        ("images/menu_sample13.jpg", "🥨 Pretzels", 500),
    ]

    # Render 4 items per row responsively
    for i in range(0, len(menu_items), 4):
        cols = st.columns(4)
        for col, (img_path, name, price) in zip(cols, menu_items[i:i+4]):
            with col:
                st.image(img_path, caption=f"{name} - Rs.{price}", use_container_width=True)

# Order Page (mock-up)
elif menu == "Order Now":
    st.markdown("### 🛒 Place Your Order")
    name = st.text_input("Enter Your Name")
    item = st.selectbox("Select Item", ["Zinger Burger", "Shawarma", "Fries", "Cold Drink","Taco" ,"momos","chicken nuggets","fried chicken","Pizza","Club Sandwich","Tandoori Pizza","Pretzels"])
    quantity = st.slider("Quantity", 1, 20)
    if st.button("Confirm Order"):
        st.success(f"Thank you, {name}! You've ordered {quantity} x {item}. We'll contact you soon!")

# About Page
elif menu == "About Us":
    st.markdown("### 👨‍🍳 About ShazCo")
    st.write("Welcome to ShazCo – Where Flavor Meets Fast!")
    st.write("Craving something delicious, quick, and unforgettable?")
    st.write("ShazCo brings you the boldest bites, juiciest burgers, crispy fries, and refreshing drinks – all crafted to satisfy your hunger on the go. " )
    st.write("Whether you're dining in, ordering online, or grabbing a quick bite, ShazCo is your ultimate fast food destination.")
    st.write("Started in 2024, we aim to serve flavorful fast food across Pakistan with premium ingredients.")

 # Why Choose ShazCo
elif menu == "Why ShazCo?":
    st.markdown("### 🌟 Why Choose ShazCo?")
    st.write("1. **Fresh Ingredients**: We use only the freshest and finest ingredients.")
    st.write("2. **Fast Service**: Fast food doesn't mean compromising on quality.")
    st.write("3. **Affordable Prices**: Enjoy delicious meals without breaking the bank.")
    st.write("5. **Order Online**: Fast delivery at your doorstep in just a few clicks.")

# Contact Page
elif menu == "Contact":
    st.markdown("### 📞 Contact Us")
    st.write("📍 Location: Main Market, Karachi")
    st.write("📱 Phone: +92 311 8274522")
    st.write("📧 Email: shazianaz2417@gmail.com")
    st.text_input("Your Message")
    if st.button("Send"):
        st.success("Thanks! We'll get back to you shortly.")