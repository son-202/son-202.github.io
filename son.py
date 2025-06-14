import streamlit as st

# Danh sách tài khoản mẫu
users = {
    "admin": "123456",
    "user": "password"
}

def login(username, password):
    if username in users and users[username] == password:
        return True
    return False

def main():
    st.set_page_config(page_title="Login Page", page_icon="🔐", layout="centered")

    st.title("🔐 Đăng Nhập Hệ Thống")

    # Form đăng nhập
    with st.form("login_form"):
        username = st.text_input("👤 Tên đăng nhập")
        password = st.text_input("🔑 Mật khẩu", type="password")
        submitted = st.form_submit_button("Đăng nhập")

        if submitted:
            if login(username, password):
                st.success(f"✅ Chào mừng, {username}!")
                st.balloons()
            else:
                st.error("❌ Sai tên đăng nhập hoặc mật khẩu.")

if __name__ == "__main__":
    main()
