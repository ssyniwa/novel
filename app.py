import streamlit as st

# セッション状態の初期化
if 'page' not in st.session_state:
    st.session_state.page = 'select_char'
if 'selected_char' not in st.session_state:
    st.session_state.selected_char = None

# 画面遷移の制御
def set_page(page_name):
    st.session_state.page = page_name

# --- ページごとの処理 ---

# 1. キャラクター選択画面
if st.session_state.page == 'select_char':
    st.title("ノベルゲームへようこそ")
    st.write("キャラクターを選んでください：")
    
    col1, col2, col3 = st.columns(3)
    
    if col1.button("勇者"):
        st.session_state.selected_char = "勇者"
        set_page('scene_1')
    if col2.button("魔法使い"):
        st.session_state.selected_char = "魔法使い"
        set_page('scene_1')
    if col3.button("盗賊"):
        st.session_state.selected_char = "盗賊"
        set_page('scene_1')

# 2. ストーリー分岐画面
elif st.session_state.page == 'scene_1':
    st.title(f"{st.session_state.selected_char}の物語")
    st.write("目の前に分かれ道が現れた。どちらに進む？")
    
    if st.button("右の洞窟へ進む"):
        st.session_state.result = "洞窟で宝を見つけた！"
        set_page('ending')
    if st.button("左の森へ進む"):
        st.session_state.result = "森で迷子になった..."
        set_page('ending')

# 3. 終了画面
elif st.session_state.page == 'ending':
    st.title("結果")
    st.write(f"結果: {st.session_state.result}")
    
    if st.button("最初からやり直す"):
        set_page('select_char')
