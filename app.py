import streamlit as st
from supabase_config import supabase
import bcrypt

st.set_page_config(page_title="Supabase Auth App", page_icon="🔑")

menu = st.sidebar.selectbox("メニュー", ["ログイン", "新規登録"])

# ユーザー登録
def register_user(email, password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    data = {"email": email, "password": hashed_password}
    response = supabase.table("users").insert(data).execute()
    return response

# ユーザー認証
def authenticate_user(email, password):
    response = supabase.table("users").select("*").eq("email", email).execute()
    if response.data:
        stored_password = response.data[0]["password"]
        return bcrypt.checkpw(password.encode(), stored_password.encode())
    return False

if menu == "ログイン":
    st.header("🔑 ログイン")

    email = st.text_input("メールアドレス")
    password = st.text_input("パスワード", type="password")

    if st.button("ログイン"):
        if authenticate_user(email, password):
            st.success(f"ログイン成功！ {email}")
            st.session_state["logged_in"] = True
            st.session_state["email"] = email
        else:
            st.error("メールアドレスまたはパスワードが間違っています")

elif menu == "新規登録":
    st.header("📝 新規登録")

    email = st.text_input("メールアドレス")
    password = st.text_input("パスワード", type="password")
    confirm_password = st.text_input("パスワード（確認用）", type="password")

    if st.button("登録"):
        if password == confirm_password:
            response = register_user(email, password)
            if "error" not in response:
                st.success("登録成功！ログインしてください")
            else:
                st.error("登録に失敗しました（メールアドレスが既に使用されている可能性があります）")
        else:
            st.error("パスワードが一致しません")
