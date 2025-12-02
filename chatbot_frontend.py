import streamlit as st
from app import workflow
from langchain_core.messages import HumanMessage,AIMessage

if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]

for i in st.session_state['message_history']:
    with st.chat_message(i['role']):
        st.text(i['content'])

user_input=st.chat_input('type here')

if user_input:
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.text(user_input)

    response=workflow.invoke({'messages':[HumanMessage(content=user_input)]},config={'configurable':{'thread_id':'1'}})['messages'][-1].content
    with st.chat_message('assistant'):
        st.text(response)
    st.session_state['message_history'].append({'role':'assistant','content':response})





  #STREAMING
    #'''
    #with st.chat_message('assistant'):
      #def ai_only_stream():
         # for message_chunk,metadata in workflow.stream(
          #    {'messages':[HumanMessage(content=user_input)]},
          #    config={'configurable':{'thread_id':'1'}},
           #   stream_mode='messages'
          #  ):
           #   if isinstance(message_chunk,AIMessage):
           #       yield message_chunk.content
    
    #ai_message=st.write_stream(ai_only_stream())    
    #  
    #st.session_state['message_history'].append({'role':'assistant','content':ai_message})
    #'''