import streamlit as st

# --- 1. ゲームの状態（パラメータ・フラグ）の初期化 ---
def init_game():
    st.session_state.page = 'select_char'
    st.session_state.char = None
    # パラメータ管理
    st.session_state.params = {"好感度": 0, "勇気": 0, "知識": 0}
    # フラグ管理
    st.session_state.flags = {"アイテムA所持": False}
    st.session_state.result = ""

if 'page' not in st.session_state:
    init_game()

# --- 2. ページごとの処理 ---

# 画面1: キャラクター選択
if st.session_state.page == 'select_char':
    st.title("キャラクター選択")
    char_list = ["勇者", "魔法使い", "盗賊"]
    for char in char_list:
        if st.button(char):
            st.session_state.char = char
            st.session_state.page = 'scene_1'
            st.rerun()

# 画面2: シーン1（フラグの取得とパラメータ変化）
elif st.session_state.page == 'scene_1':
    st.title(f"{st.session_state.char}の章")
    st.write("古い神殿で何かを見つけた。")
    
    col1, col2 = st.columns(2)
    if col1.button("「勇気の剣」を拾う (勇気+2)"):
        st.session_state.params["勇気"] += 2
        st.session_state.flags["アイテムA所持"] = True
        st.write("勇気が上がった！アイテムを手に入れた！")
    if col2.button("書物を読む (知識+2)"):
        st.session_state.params["知識"] += 2
        st.write("知識が上がった！")
    
    if st.button("次へ"):
        st.session_state.page = 'final_scene'
        st.rerun()

# 画面3: 最終シーン（パラメータによる分岐・マルチエンディング）
elif st.session_state.page == 'final_scene':
    st.title("結末の時")
    st.write(f"現在の能力: {st.session_state.params}")
    
    # 条件分岐によるマルチエンディング
    if st.session_state.params["勇気"] >= 2 and st.session_state.flags["アイテムA所持"]:
        st.success("隠しエンディング：伝説の英雄になった！")
    elif st.session_state.params["勇気"] >= 2:
        st.info("ハッピーエンド：勇者として称えられた。")
    elif st.session_state.params["知識"] >= 2:
        st.info("ノーマルエンド：賢者として生きた。")
    else:
        st.error("バッドエンド：何も残らなかった…")

    if st.button("リセットして最初から"):
        init_game()
        st.rerun()
