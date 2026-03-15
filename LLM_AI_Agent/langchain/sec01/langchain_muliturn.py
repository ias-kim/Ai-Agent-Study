from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

message = [
    SystemMessage("너는 사용자를 도와주는 상담사야")
]

while True:
    user_input = input("사용자 :")
    
    if user_input == "exit":
        break

    message.append(
        HumanMessage(user_input)
    )

    ai_respone = llm.invoke(message)

    message.append(
        ai_respone
    )

    print("AI: " + ai_respone.content)

