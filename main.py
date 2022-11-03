import streamlit as st
import graphviz

graph = graphviz.Digraph()

col1, col2 = st.columns([3, 1])

with col1:
    surgery = st.radio("手术", ('已手术', '未手术'))
    er = st.radio('ER',('阳性','阴性'))
    pr = st.radio('PR',('阳性','阴性'))
    size = st.radio('大小',('大','小'))
    lymphnode = st.radio('淋巴结',('转移','未转移'))
    her2 = st.radio('HER-2',('阳性','阴性'))
    conserve = st.radio('保乳',('是','否','未知'))

with col2:
    if surgery == '未手术' or lymphnode == '转移' or her2 == '阳性' or (er=='阴性' and pr=='阴性' and her2=='阴性') or conserve=='是':
        graph.edge('评估', '新辅助化疗')
    else:
        graph.edge('评估', '手术')

st.graphviz_chart(graph)