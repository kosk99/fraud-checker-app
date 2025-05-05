import streamlit as st
import openai

st.title("🤖 詐欺判定AIアプリ")
st.write("副業・事業の内容を入力すると、詐欺の可能性をAIが％で評価します。")

user_input = st.text_area("勧誘内容を入力してください：", "")

if st.button("判定する"):
    if not user_input.strip():
        st.warning("勧誘内容を入力してください。")
    else:
        with st.spinner("AIが判定中..."):
            openai.api_key = "あなたのAPIキーをここに"
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "あなたは詐欺の専門家です。"},
                    {"role": "user", "content": f"{user_input} これは詐欺の可能性が何％ありますか？"}
                ]
            )
            result = response.choices[0].message.content
            st.success("✅ 判定結果")
            st.write(result)
