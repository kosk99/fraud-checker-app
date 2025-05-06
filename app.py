import openai
import streamlit as st
import os

# 環境変数からAPIキーを読み込む
openai.api_key = os.getenv("OPENAI_API_KEY")

# ページ設定
st.set_page_config(page_title="副業詐欺チェッカー", page_icon="🕵️", layout="centered")

# タイトルと説明
st.title("🕵️‍♀️ 副業詐欺チェッカーAI")
st.markdown("""
あなたが考えている副業・ビジネスが詐欺かどうか、AIが判定します。  
詐欺の可能性、理由、似た事例まで詳しく解説します。  
""")

# テキスト入力
user_input = st.text_area("✍️ 副業・ビジネスの内容を入力してください", height=200, placeholder="例：LINEで月30万円稼げると紹介されて…")

# 送信ボタン
if st.button("🔍 判定する"):
    if not user_input.strip():
        st.warning("内容を入力してください。")
    else:
        with st.spinner("AIが詐欺の可能性を分析中..."):
            try:
                # OpenAIに問い合わせ
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": """あなたは入力された副業・事業の説明が詐欺の可能性があるかを判断するAIです。

1. 詐欺の可能性を 0%〜100% の確率で表示してください。
2. その理由を日本語で解説してください。
3. 過去に似たような詐欺がある場合、その詐欺の名称（例：マルチ商法、情報商材詐欺など）を挙げてください。
4. その詐欺の具体的な手口や事例をわかりやすく説明してください。
5. 最後に、ユーザーに対する注意点やアドバイスがあれば加えてください。"""
                        },
                        {"role": "user", "content": user_input}
                    ]
                )

                ai_response = response.choices[0].message.content

                # 結果表示
                st.success("✅ 判定結果")
                st.markdown(ai_response)

            except Exception as e:
                st.error(f"エラーが発生しました: {e}")
