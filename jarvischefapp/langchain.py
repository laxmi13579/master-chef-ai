from langchain_openai import ChatOpenAI
from langchain_core.prompts import HumanMessagePromptTemplate,SystemMessagePromptTemplate, ChatPromptTemplate
from decouple import config

def askJarvisChef(recipe_message):
    SECRETE_KEY = config("OPENAI_API_KEY")
    chat = ChatOpenAI(openai_api_key=SECRETE_KEY)
    systemMessagePrompt = SystemMessagePromptTemplate.from_template("you are an expert chef.")
    humanMessagePrompt = HumanMessagePromptTemplate.from_template("{ask_recipe}")

    chatPrompt = ChatPromptTemplate.from_messages([
        systemMessagePrompt, humanMessagePrompt
    ])

    formattedPrompt = chatPrompt.format_messages(ask_recipe=recipe_message)
    response = chat.invoke(formattedPrompt)
    return response.content
