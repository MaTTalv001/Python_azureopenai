#参考
#https://docs.streamlit.io/library/get-started

#ライブラリの読み込み
import time
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression


#タイトル
st.title("AIによる表データテキスト変換")
st.write("streamlitで実装")

# 以下をサイドバーに表示
st.sidebar.markdown("### 変換処理を行うcsvファイルを入力してください")
#ファイルアップロード
uploaded_files = st.sidebar.file_uploader("Choose a CSV file", accept_multiple_files= False)
#ファイルがアップロードされたら以下が実行される
if uploaded_files:
      with st.container(border=True):
            df = pd.read_csv(uploaded_files)
            df_columns = df.columns
            #入力データを目視で確認
            st.markdown("### 入力データ（確認）")
            st.dataframe(df.head(5).style.highlight_max(axis=0))
      with st.container(border=True):
            #プロンプトで変換するカラムの選択
            st.markdown("### パラメータの設定")
            #データフレームのカラムを選択オプションに設定する
            text_column = st.selectbox("変換対象のカラムを選択", df_columns)
            #プロンプトセットの読み込み
            df_prompt = pd.read_csv("promptset.csv")
            prompt_sets = df_prompt["Department"].values
            #プロンプトプリセットの選択）
            prompt_column = st.selectbox("プロンプトセットを選択してください", prompt_sets)
            if prompt_column:
                  prompt = str(df_prompt[df_prompt["Department"]==prompt_column]["Prompt"].values[0])
                  st.success(prompt, icon="✅")
      with st.container(border=True):
            #ID・パスワードの入力
            st.markdown("### IDの入力")
            st.info('このシステムではID・パスワードをハッシュ化したものを個人識別キーとして使用しています', icon="ℹ️")
            s_num = st.text_input('ID', placeholder="IDを入力してください")
            s_pass = st.text_input('Password', type="password", placeholder="パスワードを入力してください")

    


      #execute = st.button("実行")
            
           
            #実行ボタンを押したら下記が進む
            #if execute:


