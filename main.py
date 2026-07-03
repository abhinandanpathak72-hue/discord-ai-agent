import discord
from dotenv import load_dotenv
load_dotenv()
import os
from langchain.messages import HumanMessage

from agent import agent

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    async with message.channel.typing():
       
        content = message.content
    
        response = await agent.ainvoke({"messages": [HumanMessage(content)]})
        
        agent_message = response["messages"][-1].text
    
    await message.channel.send(agent_message)
    
 
client.run(token = os.getenv("DISCORD_API_KEY"))

