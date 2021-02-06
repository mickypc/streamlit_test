#!/usr/local/bin/python3

import streamlit as st
import numpy as np
import pandas as pd
import time

#st.title("test title")
#st.write("Here's our first attempt at using data to create a table:")
#st.write(pd.DataFrame({
#    'first column': [1, 2, 3, 4],
#    'second column': [10, 20, 30, 40]
#}))
#
#x = st.slider('x')
#st.write(x, 'squared is', x * x)

"""
# My first app
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
df

chart_data = pd.DataFrame(
     np.random.randn(20, 3), columns=['a', 'b', 'c'])
chart_data
st.line_chart(chart_data)


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
map_data
st.map(map_data)


if st.checkbox('Show dataframe'):
  chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=['a', 'b', 'c'])

  st.line_chart(chart_data)

option = st.selectbox(
    'Which number do you like best?',
     df['first column'],
     key="sel1")

'You selected: ', option

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'],
     key="sel2")

'You selected: ', option

left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

''
text_label = st.empty()
text_label.text('Starting a long computation...')
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)
text_label.text('...and now we\'re done!')