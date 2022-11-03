import streamlit as st
import graphviz

graph = graphviz.Digraph()

surgery = st.radio("手术", ('已手术', '未手术'))
er = st.radio('ER',('阳性','阴性'))
pr = st.radio('ER',('阳性','阴性'))
size = st.radio('大小',('大','小'))
lymphnode = st.radio('淋巴结',('转移','未转移'))
her2 = st.radio('HER-2',('阳性','阴性'))
conserve = st.radio('保乳',('是','否','未知'))


# if surgery == '已手术':
#     graph.edge('评估', '新辅助化疗')
# if surgery == '未手术':
#     graph.edge('评估', '手术')

st.graphviz_chart(graph)