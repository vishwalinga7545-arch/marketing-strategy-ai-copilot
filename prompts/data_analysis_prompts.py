from langchain.prompts import PromptTemplate

DATA_ANALYST_PROMPT = PromptTemplate(
    input_variables=["data_summary"],
    template="""
You are a senior marketing data analyst.

Analyze the following marketing data summary.
Give insights in bullet points.

Data:
{data_summary}
"""
)
