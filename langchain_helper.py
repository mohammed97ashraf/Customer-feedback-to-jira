import os
from dotenv import load_dotenv
from langchain.chains import SimpleSequentialChain
from langchain.document_loaders import WebBaseLoader
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List, Optional

# load the environment variables from .env file
load_dotenv()

# set the openai key from the .env
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


class web_parse(BaseModel):
    app_name: str = Field(..., description="app name")
    app_description: str = Field(..., description="app description")
    user_comments: List[str] = Field(..., description="A list of user comments or feedback on this app.")

def get_page_content(url : str) -> str:
    loader = WebBaseLoader(url)
    data = loader.load()
    return data[0].page_content

def tagging_chain_web_parse(web_text: str) -> BaseModel:
    tagging_prompt = ChatPromptTemplate.from_template(
            """
        Given to you is a web page content for a App in google play store.

        Extract the desired information from the following web page content.

        Only extract the properties mentioned in the 'web_parse' function.

        content:
        {input}
        """)
    
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini").with_structured_output(
                        web_parse
                    )
    chain = tagging_prompt | llm

    result = chain.invoke({"input": web_text})

    return result


def get_negative_comments(user_comments: BaseModel) -> dict:
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", """You are an experienced product manager who enhances user satisfaction and app performance.

You have been given a collection of user comments from the Google Play Store for the mobile app {app_name}. The app's description is as follows: {app_description}.

Your primary task is to thoroughly analyze these comments to identify recurring themes, with a focus on any technical issues or bugs that users have reported. Pay close attention to performance-related concerns, crashes, feature malfunctions, and other usability challenges hindering the user experience. Provide a summary of the most critical technical problems, along with insights into potential areas of improvement

Return a JSON

```json
comment_text:<comment_text>,

summary:<summary>
```
         """),
        ("user", "user comments: {user_comments}")
    ])

    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini",top_p=0.90,model_kwargs={"response_format": {"type": "json_object"}})

    chain = prompt_template | llm | JsonOutputParser()

    result = chain.invoke({"app_name": user_comments.app_name, "app_description": user_comments.app_description, "user_comments": user_comments.user_comments})

    return result

def get_jira_tickets(Report: dict) -> dict:
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", """You are an expert product manager responsible for managing technical issues reported by users.

You have been given a report detailing the issues faced by the users of the app. Your task is to create a JIRA ticket for each bug described in the report.

Follow these steps carefully:

1. Identify each distinct bug or technical issue mentioned in the report.

2. For each bug, generate a ticket with a title that summarizes the issue.

3. Write a description of the bug in markdown format, including:

       - A brief overview of the issue.

       - Steps to reproduce the problem (if available).

       - Expected behavior versus actual behavior.

       - Any relevant additional information provided in the report.

Return the result as a JSON list in the following format:

'''

title:<bug title>

descrption :<description>

''' """),
        ("user", "Report: {report}")
    ])

    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini",top_p=0.90,model_kwargs={"response_format": {"type": "json_object"}})

    chain = prompt_template | llm | JsonOutputParser()
   
    result = chain.invoke({"report":Report})

    return result






