# https://www.youtube.com/watch?v=zp-kAt1Ih5k
# Youtubeチャンネル　いまにゅプログラミング塾より

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プレグレスバー')
'Start!!'

latest_itration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_itration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.02)
'Done!!!'

st.write('Interractive Widgets')
# Expanderの追加
expander = st.expander('問合せ1')
expander.write('問合せ１の回答')
expander = st.expander('問合せ2')
expander.write('問合せ2の回答')
expander = st.expander('問合せ3')
expander.write('問合せ3の回答')


# 2カラム表示
left_column, right_column = st.columns(2)
# 左カラム→ボタン、右カラム→テキスト
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

# サイドバーはst.sidebar.slider　と入れるだけ
# スライダー(最小値、最大値、デフォルト値)
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# テキストボックス
text = st.text_input('あなたの趣味を教えてください。')

'コンディション：', condition
'あなたの趣味：', text, 'です。'


# セレクトボックス
option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)
'あなたの好きな数字は、', option, 'です。'


# チェックボックスはTrue Falseを返す
if st.checkbox('Show Image'):
    # 写真の表示
    img = Image.open('macaroon.jpg')
    st.image(img, caption='Family', use_column_width=True)


st.write('Map')

# 地図の表示
df1 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [34.41, 135.31],
    columns=['lat', 'lon']
)
st.map(df1)


# 折れ線グラフの描画
df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
# 折れ線グラフ
st.line_chart(df2)
# エリアチャート
st.area_chart(df2)
# 棒グラフ
st.bar_chart(df2)


# マジックコマンド
"""
# 章
## 節
### 項

'''python
import streamlit as st
import numpy as np
import pandas as pd
'''
"""

# 表の表示
# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })
# st.dataframe(df.style.highlight_max(axis=0))