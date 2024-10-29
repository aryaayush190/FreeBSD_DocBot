# FreeBSD_DocBot

FreeBSD is a server-grade operating system that is known for its reliability, scalability, and networking capabilities. It's also customizable and can be used in embedded systems, making it suitable for consumer electronics.
https://en.wikipedia.org/wiki/FreeBSD  
https://freebsdfoundation.org/freebsd/ 

![Free BSD](https://github.com/user-attachments/assets/42ad35c7-794a-4684-b137-57fb5eafc351)

# Overview  
FreeBSD_DocBot is an innovative tool designed to streamline your interaction with the FreeBSD operating system. By leveraging the power of Large Language Models (LLMs), LangChain, and Astra DB, this project provides a user-friendly interface to access and understand FreeBSD commands and configurations.  
1. Prompt-Based Interaction: Simply input your command request in plain language.
2. LLM Processing: The LLM analyzes your command and identifies the relevant FreeBSD command or concept.
3. Knowledge Base Access: LangChain efficiently retrieves information from the Astra DB, which stores a comprehensive knowledge base of FreeBSD documentation and commands.
4. Response Generation: The LLM generates a clear and concise response, explaining the command's syntax, usage, and potential output.

# Installation:
### Pre-requisites:
#### 1. Create a Database Administrator Token:

 •  Log in to the Astra DB portal.  
 •  Navigate to the desired database.  
 •  Click the Generate Token button.  
 •  Select the Database Administrator role.  
 •  Copy the generated token.  

#### 2. Identify Your Database ID:

•  Locate the API endpoint URL for your database.  
•  Extract the portion between https:// and .apps.astra.datastax.com.  
•  This is your Database ID.    
  
You also need an [OpenAI API Key](https://cassio.org/start_here/#llm-access) .      

### Required Dependencies
```python
!pip install -q cassio datasets langchain openai tiktoken  
!pip install PyPDF2    
!pip install -U langchain-community    
!pip install openai==0.28
```
