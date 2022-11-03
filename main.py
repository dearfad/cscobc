import streamlit as st
import graphviz

# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge('评估', '新辅助化疗')
graph.edge('评估', '手术')


st.graphviz_chart(graph)