from smolagents import CodeAgent, HfApiModel
from tools import fetch_url_content, format_blog_post
from dotenv import load_dotenv
import os 

load_dotenv()

# Retrieve the Hugging Face API key
hf_api_key = os.getenv("HF_API_KEY")

# Check if the API key is properly loaded
if not hf_api_key:
    raise ValueError("The Hugging Face API key is missing! Add it to your .env file.")

# Initialize the language model
model = HfApiModel(model_id="google-t5/t5-small", token=hf_api_key)

# Create the agent with the custom tools, agent that writes actions in code
agent = CodeAgent(tools=[fetch_url_content, format_blog_post], model=model)

# Define the prompt
prompt = '''
1. Fetch the content from the URL: 'https://www.cnbc.com/2025/01/18/perplexity-ai-makes-a-bid-to-merge-with-tiktok-us.html'.
2. Summarize the content.
3. Format the summary into a blog post with a main headline, three main takeaways, and a conclusion.
'''

# Run the agent with the prompt
response = agent.run(prompt)

# Output the response
print(response)
