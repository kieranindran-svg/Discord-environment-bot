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
    'us': 'https://www.nature.org/en-us/get-involved/how-to-help/volunteer/',
    'france': 'https://benevole.com/en/missions?domain=environnement',
    'africa': 'https://africanimpact.com/volunteer-projects/environmental-sustainability/',
}




@bot.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@bot.command()
async def hello(ctx):
      await ctx.send("Hi!")

@bot.command()
async def help(ctx):
      await ctx.send("Hello! I can provide you with information about volunteering opportunities in different countries. Use the command !volunteer <country> to get started. For example, !volunteer uk or !volunteer us.")

@bot.command()
async def volunteer(ctx, country:str):
      if country in countries:
        await ctx.send(countries[country])
      else:
        await ctx.send("Sorry, I don't have information for that country.")
      

bot.run("YOUR_BOT_TOKEN")