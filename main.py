import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Introduction of Streamlit')

st.write('Display Progressbar')
'Start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done'

# if st.checkbox('Show Image'):
#     img = Image.open('img1.png')
#     st.image(img, caption='Sample', use_column_width=True)

left_column, right_column = st.beta_columns(2)
button = left_column.button('Display message')
if button:
    right_column.write('Button clicked')

expander = st.beta_expander('expander')
expander.write('This is expander paragraph')

# option = st.selectbox(
#     'Select #',
#     list(range(1,11))
# )

# 'You selection is', option

# text = st.text_input('Please input your hobby')
# condition = st.slider('Your feeling', 0, 100, 50)

# 'Your hobby:', text
# 'condition:', condition