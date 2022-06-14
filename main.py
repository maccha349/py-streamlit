from cgitb import text
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)
'Done!!'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('右カラム')

expander = st.expander('問い合わせ1')
expander.write('問い合わせ内容を書く')
expander = st.expander('問い合わせ2')
expander.write('問い合わせ内容を書く')
expander = st.expander('問い合わせ3')
expander.write('問い合わせ内容を書く')


text = st.text_input('あなたの趣味を教えて下さい')
'あなたの趣味: ', text

condition = st.slider('あなたの調子は?', 10, 100, 50)
'コンディション:', condition


option = st.selectbox(
    '数字を選択',
    list(range(1,11))
)
'選択した数字は',option,'です'

# if st.checkbox('Show Image'):
#     img = Image.open('./sample.jpg')
#     st.image(img, caption='sample', use_column_width=True)

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df)


df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40],
})

st.write('write')
st.write(df)
# dataframeで引数が指定できる
st.write('dataframe')
st.dataframe(df.style.highlight_max(axis=0, color='orange'))

# 静的なテーブル
st.write('table')
st.table(df.style.highlight_max(axis=0, color='orange'))

# マークアップ
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """