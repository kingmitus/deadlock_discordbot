import discord
from discord.ext import commands
from discord import app_commands
import os

def hero_id():
    return "Hero ID: 1234"

def patch_notes():
    return "Patch notes: Updated hero abilities and bug fixes."

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.author == self.user:
            return 
        if message.content.startswith('hello'):
            await message.channel.send(f'Hawk tuah {message.author} spit on that thang')
        if message.content.startswith('send a link'):
            await message.channel.send(f'https://www.youtube.com/watch?v=Pu-7b_AHcJ4')
    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('deez nutz')
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'{member} joined, hawk tuah')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = Client(command_prefix="/", intents=intents)

GUILD_ID = 1179614426983321710

@client.tree.command(name='hawk_tuah', guild=discord.Object(id=GUILD_ID))
async def hawk_tuah(interaction: discord.Interaction):
    await interaction.response.send_message('hawk tuah')

@client.tree.command(name='hero', description='Get a deadlock hero id', guild=discord.Object(id=GUILD_ID))
async def hero(interaction: discord.Interaction):
    await interaction.response.send_message(hero_id())

@client.tree.command(name='patch', description='most recent patch notes', guild=discord.Object(id=GUILD_ID))
async def patch(interaction: discord.Interaction):
    await interaction.response.send_message(patch_notes())

@client.event
async def on_ready():
    await client.tree.sync()


client.run('MTMxMjg5OTI1NDA3NTAwMjkzMQ.GMnxKW.i3wsERhJP57qQOK0EbISs7rvei6hVCJq7tLTuo')




