import discord
from discord.ext import commands

# intents variable stores the permissions of the bot
intents = discord.Intents.default()
# Enable the permission to read message content
intents.message_content = True
# Create a bot and pass the intents
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

countries = {
    'uk': 'https://www.gov.uk/government/collections/national-nature-reserves-in-england',
}




@bot.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@bot.command()
async def hello(ctx):
      await ctx.send("Hi!")

@bot.command()
async def volunteer(ctx, country:str):
      if country in countries:
        await ctx.send(countries[country])
      else:
        await ctx.send("Sorry, I don't have information for that country.")
      

bot.run("YOUR_BOT_TOKEN")