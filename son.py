import streamlit as st

# Danh sách laptop mẫu
laptops = [
    {
        "name": "Laptop ASUS VivoBook",
        "price": 15990000,
        "image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.asus.com%2Fvn%2Flaptops%2Ffor-home%2Fvivobook%2Fvivobook-15-x1502%2F&psig=AOvVaw0HV3U8n3THg6VKP6mAkdgO&ust=1749967464323000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCMjFlfye8I0DFQAAAAAdAAAAABAE"
    },
    {
        "name": "Laptop Dell Inspiron",
        "price": 17990000,
        "image": "https://cdn.tgdd.vn/Products/Images/44/304495/dell-inspiron-15-3530-i5-71006208-thumb-600x600.jpg"
    },
    {
        "name": "Laptop MacBook Air M2",
        "price": 28990000,
        "image": "https://cdn.tgdd.vn/Products/Images/44/289691/apple-macbook-air-13-inch-m2-2022-600x600.jpg"
    }
]

# Session state cho giỏ hàng
if "cart" not in st.session_state:
    st.session_state.cart = []

# Header
st.set_page_config(page_title="Cửa Hàng Laptop", layout="wide")
st.title("🛒 CỬA HÀNG LAPTOP ONLINE")

st.markdown("### Danh sách sản phẩm")

# Hiển thị laptop theo dạng cột
cols = st.columns(len(laptops))

for i, laptop in enumerate(laptops):
    with cols[i]:
        st.image(laptop["image"], width=200)
        st.write(f"**{laptop['name']}**")
        st.write(f"💵 Giá: {laptop['price']:,} VND")
        if st.button(f"🛒 Thêm vào giỏ - {i}"):
            st.session_state.cart.append(laptop)
            st.success(f"Đã thêm **{laptop['name']}** vào giỏ hàng!")

# Giỏ hàng
st.markdown("---")
st.markdown("## 🧺 Giỏ hàng")

if st.session_state.cart:
    total = 0
    for item in st.session_state.cart:
        st.write(f"- {item['name']} - 💵 {item['price']:,} VND")
        total += item['price']
    st.markdown(f"### ✅ Tổng cộng: **{total:,} VND**")
else:
    st.info("Giỏ hàng của bạn đang trống.")

