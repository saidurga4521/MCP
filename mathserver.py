from mcp.server.fastmcp import FastMCP 
##fastmcp
# used to make mcp server very easily
# without this fastmcp you would need to handle mcp protocol implementation also

# create an MCP server
mcp=FastMCP('math')

#Creating tool
@mcp.tool()
def addition(a:int,b:int)->int:
  """Addtion of two numbers"""
  return a+b

@mcp.tool()
def multiplication(a:int,b:int)->int:
  """Multiplication of two numbers"""
  return a*b


if __name__=="__main__":
  mcp.run(transport='stdio')

  # transport: It is the communication channel how the mcp client and mcp server exchange their messages
  # Different types of transports : 1.stdio 2.streamble-http
  # When the client connects using STDIO:
     # 1. The client starts the MCP Server as a separate process.
     # 2. The client sends MCP messages through the server's standard input (stdin).(Basically you can send the messages using command prompt)
     # 3. The server reads those messages and processes them.
     # 4. The server sends responses through standard output (stdout).(The response back to command prompt)
     # Important: With STDIO, the client typically launches and manages the server process. Both run on the same machine.
  
  # When the client connects using HTTP:
      # You start the MCP Server independently.
      # The server listens for incoming HTTP requests.
      # The MCP Client sends requests to the server's URL.
      # The server processes the request.
      # The server returns the response.

## When should you use each one?
# Use STDIO when:
    # - You are developing a local MCP Server.
    # - Your MCP Client and Server run on the same machine.
    # - You want the client to manage the server process.
    # - Good for debugging
# Use Streamable HTTP when:
    # - Multiple applications need to access the same MCP Server.
    # - You want to host your MCP Server independently.
    # - Your client and server communicate over a network.