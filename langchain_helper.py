from langchain_openai.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import streamlit as st
import os
os.environ['OPENAI_API_KEY'] = os.environ['open_api_key']
llm = OpenAI(temperature=0.5)


def generate_name_and_items(cuisine):
    prompt_template_name = PromptTemplate(
          input_variables=['cuisine'],
          template="I want to open a {cuisine} restaurant.suggest me only one fancy name."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    prompt_template_item = PromptTemplate(
          input_variables=['restaurant_name'],
          template="I have a restaurant called {restaurant_name},suggest me some menu items."
    )
    item_chain = LLMChain(llm=llm, prompt=prompt_template_item, output_key="items")



    chain = SequentialChain(
        chains=[name_chain, item_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'items'],
    )
    response = chain({'cuisine': cuisine})
    return response


if __name__=="__main__":
    print(generate_name_and_items("italian"))