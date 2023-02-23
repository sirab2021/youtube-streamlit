import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'スタート！'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'終わり！！'



left_column, right_column = st.columns(2)
button = left_column.button('右列に文字を表示')
if button:
    right_column.write('ここは右列です。')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ回答1')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ回答２')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ回答３')


#st.write('Display Image')

#Sidebarの表示
#text = st.sidebar.text_input('あなたの趣味を教えてください')
#'あなたの趣味は：', text, 'です。'
#スライドバーの表示
#condition = st.sidebar.slider('あなたの今の調子は',0,100,50)
#'あなたの今の調子は：', condition, 'です。'

#セレクトボックスの表示
#option = st.selectbox(
#    'あなたが好きな数字を入れてください',
#    list (range(1,11))
#    )
#'あなたが好きな数字は', option, 'です。'

#チェックボックスの表示
#if st.checkbox('Show Image'):
#    img = Image.open('2020kaho.jpg')
#    st.image(img, caption='A drawig by kaho', use_column_width=True)


