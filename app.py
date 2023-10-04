## Importing the Lanchain Libraries

from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

import os
import openai
from dotenv import load_dotenv, find_dotenv

a = load_dotenv(find_dotenv())   # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

## Input variable
# -------------------------------------------------------------------------------------

information  = """ 
Abdul Kalam 
"""

if __name__ == '__main__':
    print(" Hello Langchain!")

## Summary--> This is prompt and 'information' --it is the variable that we pass each time in prompt
#-------------------------------------------------------------------------------------------------------------

summary_template = """
    Given the information {information} about a person from that I want you to create:
    1. A short summary
    2. Two Intersting fact about that person
"""

## Prompt Template
#--------------------------------------------------------------------------------------------------------

summary_prompt_template = PromptTemplate(
    input_variables=["information"], template=summary_template)

## LLM model - Using ChatopenAI

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

## Now we are tie everything together in a chain

chain = LLMChain(llm =llm, prompt=summary_prompt_template)

print(chain.run(information=information))


