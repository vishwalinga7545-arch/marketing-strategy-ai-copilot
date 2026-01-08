from langchain.llms import OpenAI
from langchain.chains import LLMChain
from prompts.data_analysis_prompts import DATA_ANALYST_PROMPT

def analyze_marketing_data(data_summary):
    llm = OpenAI(temperature=0)

    chain = LLMChain(
        llm=llm,
        prompt=DATA_ANALYST_PROMPT
    )

    return chain.run(data_summary=data_summary)
