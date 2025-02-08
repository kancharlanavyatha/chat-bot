#this is an langchain  based chatbot
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template= """" 
Answer the question below.

Here is the converstaion history:{context}

Question:{question}

Answer:
"""

model =OllamaLLM(model="llama3")#you can choose any llm example Gemma2,llama 
#system responses will be dependant on the specs  
prompt = ChatPromptTemplate.from_template(template)#creation of a template 
chain=prompt | model#using langcahin to bind the prompt and model 

def handle_conversation():
    context=""
    print("welcome to the  museuAI chatbot ,Here to answer your query regarding museum ! Type 'exit' to quit.")
    while True:
        user_input=input("You: ")
        if user_input.lower() == "exit":                         #usage of loops and conditonal statement for continuous responses 
            break 
        result=chain.invoke({"context":"","question":user_input})
        print("Bot:",result)
        context+= f"\nUser:{user_input}\nAI:{result}"


if __name__ == "__main__":            #creation of a conversation history for the bot to refer to 
    handle_conversation()