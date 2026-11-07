from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv() 
import asyncio  ## python module for asynchronous programming


async def main():
  client=MultiServerMCPClient(
    {
      "math":{
        "command":'python',
        "args":["mathserver.py"], #make sure correct absolute path
        "transport":'stdio'
      },
      "weather":{
        "url":"http://127.0.0.1:8000/mcp", ## make sure server is running here
        "transport":"streamable-http"
      }
    }
  )

  tools=await client.get_tools()
  model=init_chat_model(
    'google_genai:gemini-3.5-flash-lite'
  )

  agent=create_react_agent(
    model,tools
  )

  math_response=await agent.ainvoke(
    {
      'messages':[
        {
          'role':'user',
          'content':'what is (3+5)*10'
        }
      ]
    }
  )


  weather_response=await agent.ainvoke(
      {
        'messages':[
          {
            'role':'user',
            'content':'what is the weather in california'
          }
        ]
      }
    )

  print('math_response from agent',math_response['messages'][-1].content[0]['text'])
  print('weather_response from agent',weather_response['messages'][-1].content[0]['text'])

asyncio.run(main())

## Important points
 # 1.With the single client you can call multiple mcp tool servers


