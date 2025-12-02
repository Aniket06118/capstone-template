from dotenv import load_dotenv
from langgraph.graph import START,END,StateGraph
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage,HumanMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_tavily import TavilySearch
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv(override=True)

#model initialization
model=ChatGroq(model="llama-3.3-70b-versatile")
model2=ChatGoogleGenerativeAI(model="gemini-2.5-pro")
model3=ChatGroq(model='llama-3.1-8b-instant')
model4=ChatOpenAI(model='gpt-4o-mini')

#adding tools
pdf_path = r"C:\Users\Aniket\Desktop\Machine Learning.pdf"  
loader = PyPDFLoader(pdf_path)
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
splits = text_splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(splits, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

@tool
def search_pdf(query: str) -> str:
    """Search for information in the PDF document. Use this when the user asks questions about the document content."""
    docs = retriever.invoke(query)
    context = "\n\n".join([doc.page_content for doc in docs])
    return f"Relevant information from PDF:\n{context}"


search_tool=TavilySearch(max_results=2)
tools=[search_tool,search_pdf]
model_with_tools = model3.bind_tools(tools)

# defining my state
class chatbot(TypedDict):

    messages: Annotated[list[BaseMessage],add_messages]

#defining my nodes
def chat_node(state:chatbot):

    message=state['messages']
    response=model_with_tools.invoke(message)
    return {'messages':[response]}

tool_node=ToolNode(tools)

#initializing my graph
checkpointer=InMemorySaver()
graph=StateGraph(chatbot)

graph.add_node('chat_node',chat_node)
graph.add_node('tools',tool_node)

graph.add_edge(START,'chat_node')
graph.add_conditional_edges('chat_node',tools_condition)
graph.add_edge('tools','chat_node')
graph.add_edge('chat_node',END)

workflow=graph.compile(checkpointer=checkpointer)

#reply=workflow.invoke({'messages':[HumanMessage(content='how many worldcups has india won till now')]},config={'configurable':{'thread_id':'2'}})
#print(reply['messages'][-1].content)
