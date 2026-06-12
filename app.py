import streamlit as st
import json

# --- 1. データの読み込み ---

def load_scenario():
    with open("scenario.json", "r", encoding="utf-8") as f:
        return json.load(f)

SCENARIO = load_scenario()

# --- 2. 初期化 ---
def init_game():
    st.session_state.page = 'select_char'
    st.session_state.char = None
    st.session_state.params = {"勇気": 0, "知識": 0, "好感度": 0}
    st.session_state.page_id = "start"

if 'page' not in st.session_state:
    init_game()

# --- 3. アプリ実行 ---
st.title("ノベルゲーム")

if st.session_state.page == 'select_char':
    st.write("キャラクターを選んでください")
    char_list = list(SCENARIO.keys())
    cols = st.columns(len(char_list))
    for i, char in enumerate(char_list):
        if cols[i].button(char):
            st.session_state.char = char
            st.session_state.page = 'game'
            st.rerun()

elif st.session_state.page == 'game':
    # 現在のシーンデータを取得
    node = SCENARIO[st.session_state.char][st.session_state.page_id]
    
    # 画像表示（辞書に画像パスがあれば表示）
    if "image" in node:
        try:
            st.image(node["image"], use_container_width=True)
        except:
            st.warning("画像が見つかりません")
    
    st.write(node["text"])
    
    # 選択肢表示
    for opt in node.get("options", []):
        if st.button(opt["label"]):
            # パラメータ更新
            if "effect" in opt:
                for k, v in opt["effect"].items():
                    st.session_state.params[k] += v
            
            # ページ遷移
            st.session_state.page_id = opt["next"]
            
            # 終了判定
            if opt["next"].startswith("ending"):
                st.session_state.page = "result"
            st.rerun()

elif st.session_state.page == 'result':
    st.title("結末")
    st.write(f"最終ステータス: {st.session_state.params}")
    if st.button("タイトルへ戻る"):
        init_game()
        st.rerun()
