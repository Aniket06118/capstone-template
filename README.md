Template for creating and submitting MAT496 capstone project.

# Overview of MAT496

In this course, we have primarily learned Langgraph. This is helpful tool to build apps which can process unstructured `text`, find information we are looking for, and present the format we choose. Some specific topics we have covered are:

- Prompting
- Structured Output 
- Semantic Search
- Retreaval Augmented Generation (RAG)
- Tool calling LLMs & MCP
- Langgraph: State, Nodes, Graph

We also learned that Langsmith is a nice tool for debugging Langgraph codes.

------

# Capstone Project objective

The first purpose of the capstone project is to give a chance to revise all the major above listed topics. The second purpose of the capstone is to show your creativity. Think about all the problems which you can not have solved earlier, but are not possible to solve with the concepts learned in this course. For example, We can use LLM to analyse all kinds of news: sports news, financial news, political news. Another example, we can use LLMs to build a legal assistant. Pretty much anything which requires lots of reading, can be outsourced to LLMs. Let your imagination run free.


-------------------------

# Project report Template

## Title: [Chatbot with Web Search RAG Capabilities]

## Overview

This project is a LangGraph-based chatbot capable of answering user queries using both LLM reasoning and real-time web search. The system integrates multiple LLMs (Groq, Gemini, OpenAI) and a Tavily web search tool into a LangGraph workflow consisting of:
- A chat node that processes conversation history
- A tool node that performs web search when needed
- Automatic tool selection using LangGraph’s tools_condition
- State and message management using typed states
- The chatbot currently supports:
- Multi-model inference
- Inline tool calling
- Real-time web search
- Threaded conversation memory using LangGraph checkpointers

A future enhancement (planned) is a Retrieval Augmented Generation (RAG) pipeline, allowing users to upload PDFs and chat with their content, extending the system beyond web search to user-provided document understanding.

This project revises and applies all major concepts from the MAT496 course including prompting, structured outputs, semantic search, RAG, tool-calling, LangGraph nodes, and state machines.

## Reason for picking up this project
This project aligns strongly with MAT496 because:
- It uses LangGraph’s node-based architecture, including states, graph compilation, conditions, and tool routing.
- It applies tool-calling LLMs, which was a major topic in this course.
- It incorporates semantic search concepts through Tavily.
- It sets the foundation for Retrieval Augmented Generation (RAG) — a key part of the course.
- It uses multiple LLM models (Groq, Gemini, OpenAI), demonstrating the flexibility and interoperability we studied.
- The planned PDF-chat RAG pipeline directly tests our understanding of retrieval, chunking, embeddings, and document-augmented QA.
- Overall, this project demonstrates practical application of nearly every major topic covered in the course.

## Plan

I plan to execute these steps to complete my project:
- [DONE] Step 1: Initialize multiple LLM models (Groq, Gemini, OpenAI) and load environment variables.
- [DONE] Step 2: Add and configure the Tavily web search tool and bind tools to an LLM.
- [DONE] Step 3: Define LangGraph state using TypedDict and Annotated message history.
- [DONE] Step 4: Create the chat node responsible for invoking the LLM with or without tools.
- [DONE] Step 5: Create the tool node using LangGraph's ToolNode.
- [DONE] Step 6: Build the graph — add nodes, edges, conditional edges, and connect START/END.
- [DONE] Step 7: Add a checkpointer to enable threaded conversation memory.
- [DONE] Step 8: Compile the workflow and test base chatbot with web search.
- [TODO] Step 9: Add PDF loader and split it into chunks using the "RecursiveCharacterTextSplitter"
- [TODO] Step 10: use a embeddings model to convert chunks into embeddings and store it in a vector db
- [TODO] Step 11: Add a Retriever 
- [TODO] Step 9:  make a tool named search_pdf using the @tool decorator 
- [TODO] Step 12: Integrate RAG into the final response pipeline.
- [TODO] Step 13: Build a final interface using streamlit.
- [TODO] Step 14: Thoroughly test and refine model routing, tool usage, and RAG.

## Conclusion:
I had planned to build a LangGraph-based chatbot capable of intelligent conversation and web search, while also preparing the foundation for a future RAG pipeline.
I believe I have successfully achieved the first part of the project:
- LangGraph structure is set up correctly.
- Tool calling and web search work as expected.
- Multi-model support is implemented.
- State management and graph compilation are functioning.

I am partially satisfied because the full RAG pipeline (chat with PDF) is not yet implemented. However, the system architecture is designed in a way that allows RAG to be plugged in naturally, and I have a clear plan for adding it.

With more time, I can complete PDF-based retrieval, making the chatbot capable of both internet search and document understanding, covering all topics of the MAT496 course comprehensively.

----------

# Added instructions:

- This is a `solo assignment`. Each of you will work alone. You are free to talk, discuss with chatgpt, but you are responsible for what you submit. Some students may be called for viva. You should be able to each and every line of work submitted by you.

- `commit` History maintenance.
  - Fork this respository and build on top of that.
  - For every step in your plan, there has to be a commit.
  - Change [TODO] to [DONE] in the plan, before you commit after that step. 
  - The commit history should show decent amount of work spread into minimum two dates. 
  - **All the commits done in one day will be rejected**. Even if you are capable of doing the whole thing in one day, refine it in two days.  
 
 - Deadline: Nov 30, Sunday 11:59 pm


# Grading: total 25 marks

- Coverage of most of topics in this class: 20
- Creativity: 5
  
