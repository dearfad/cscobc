import streamlit as st
import graphviz

graph = graphviz.Digraph()

surgery = st.radio("是否手术", ('已手术', '未手术'))

if surgery == '已手术':
    graph.edge('评估', '新辅助化疗')

if surgery == '未手术':
    graph.edge('评估', '手术')


st.graphviz_chart(graph)