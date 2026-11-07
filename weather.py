## one more server
from mcp.server.fastmcp import FastMCP


mcp=FastMCP('weather')
@mcp.tool()
def getWeather(location:str)->str:
  """Get the weather details"""
  return "The weather in california is normal"

if __name__ == "__main__":
  mcp.run(transport='streamable-http')

## After running
 # This server runs on the port 8000  