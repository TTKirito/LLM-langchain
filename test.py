from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linkedin_profile

information = """
A member of the wealthy South African Musk family, Elon was born in Pretoria and briefly attended the University of Pretoria before immigrating to Canada at age 18, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University at Kingston in Canada. Musk later transferred to the University of Pennsylvania, and received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University. However, Musk dropped out after two days and, with his brother Kimbal, co-founded online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999, and, that same year Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal.

In October 2002, eBay acquired PayPal for $1.5 billion, and that same year, with $100 million of the money he made, Musk founded SpaceX, a spaceflight services company. In 2004, he became an early investor in electric vehicle manufacturer Tesla Motors, Inc. (now Tesla, Inc.). He became its chairman and product architect, assuming the position of CEO in 2008. In 2006, Musk helped create SolarCity, a solar-energy company that was acquired by Tesla in 2016 and became Tesla Energy. In 2013, he proposed a hyperloop high-speed vactrain transportation system. In 2015, he co-founded OpenAI, a nonprofit artificial intelligence research company. The following year, Musk co-founded Neuralink—a neurotechnology company developing brain–computer interfaces—and the Boring Company, a tunnel construction company. In 2022, he acquired Twitter for $44 billion. He subsequently merged the company into newly created X Corp. and rebranded the service as X the following year. In March 2023, he founded xAI, an artificial intelligence company.

Musk has expressed views that have made him a polarizing figure.[7][8][9] He has been criticized for making unscientific and misleading statements, including COVID-19 misinformation, transphobia[10][11][12] and antisemitic conspiracy theories.[7][13][14][15] His ownership of Twitter has been similarly controversial, including; laying off a large number of employees, an increase in hate speech and misinformation and disinformation on the website, as well as changes to Twitter Blue verification. In 2018, the U.S. Securities and Exchange Commission (SEC) sued him for falsely tweeting that he had secured funding for a private takeover of Tesla. To settle the case, Musk stepped down as the chairman of Tesla and paid a $20 million fine.
"""

if __name__ == "__main__":
    print("Hello LangChain!")

#1 create prompt
    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """
#2 create prompt template
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
#3 create chat model
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
#4 create chain
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

#5 integrate api to langchain
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url='https://www.linkedin.com/in/ton-thuan-3477b624a/')

    print(chain.run(information=linkedin_data))

