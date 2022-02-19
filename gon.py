# imports
from email import message
import discord
import art
from art import *
import json
#terminal
tprint("Gon",font="block",chr_ignore=True)
tprint('Discord Bot')

# client
client = discord.Client()

@client.event
async def on_ready():
# Go online
    general_channel = client.get_channel()

    await general_channel.send('ONLINE \N{WHITE HEAVY CHECK MARK}')
    await general_channel.send('https://media.giphy.com/media/krip8KzajyDsilW6K5/giphy.gif')
#g!
@client.event
async def on_message(message):
    #commands made by riely
    if "g!play" in message.content:
     await message.channel.send("@everyone can anyone play rn?")
     await message.channel.send("https://media.giphy.com/media/Cf1ilXyXIquMCVZLIt/giphy.gif")

    if "g!event" in message.content:
     await message.channel.send("@everyone Big event going down on server hop on")
     await message.channel.send("https://media.giphy.com/media/3f22y4dDVzHfGxeJnQ/giphy.gif")

    if "g!minecraft" in message.content:
     await message.channel.send("@everyone can you play minecraft")
     await message.channel.send("https://media.giphy.com/media/3f22y4dDVzHfGxeJnQ/giphy.gif")

    if "g!test" in message.content:
     await message.channel.send("testing testing")

    if "g!forza" in message.content:
     await message.channel.send("@everyone can anyone play forza?")
     await message.channel.send("https://media.giphy.com/media/Cf1ilXyXIquMCVZLIt/giphy.gif")
     
    if "g!ratio" in message.content:
     await message.channel.send("don't care + didn't ask + cry about it + stay mad + get real + L + mald seethe cope harder + hoes mad + basic + skill issue + ratio + you fell off + the audacity + triggered + any askers + redpilled + get a life + ok and? + cringe + touch grass + donowalled + not based + your're a (insert stereotype) + not funny didn't laugh + you're + grammar issue + go outside + get good + reported + ad hominem + GG! + ask deez + ez dap + straight cash + ratio again + final ratio + stay mad + stay pressed + pedophile + cancelled + done for + mad free + freer than air + rip bozo + slight_smile + cringe again + mad cuz bad + lol + irrelevant + cope + jealous + go ahead whine about it + your problem + don't care even more + sex offender + sex defender + not okay + glhf + problematic there!!+nuked+ called 911 + nuked multiverse + mid + ugly + rinnosuke is sexy + forgot to laugh + L + Ratio + Bozo + Mad + Reported + Unfollowed + Blocked + Cancelled + 9-1-1'ed + Swatted + Called The Mayor + Called The Governor + Called the President of the United States + Called the Dictator of North Korea + Called the President of Russia + Called the United Nations + Nuked + koishi sucks + your favorite character sucks + wriggle sucks")
    #ben
    
    if message.content.startswith('g!my special friend'):
        await message.channel.send("UR MOM L")
    if message.content.startswith('^botservers'):

        await message.channel.send("I'm in " + str(len(client.guilds)) + " servers!")
#other
#!ghelp
    if message.content.startswith('g!help'):
        embedVar = discord.Embed(title="Commands", color=0x00ff00)
        embedVar.add_field(name="List of commands:", value="g!help \n g!event \n g!play \n g!minecraft \n g!test \n g!forza \n g!ratio \n", inline=False)
        await message.channel.send("https://media.giphy.com/media/4SdFG1BbqiJEI/giphy.gif")
        await message.channel.send(embed=embedVar)
# Run the client on the server
client.run('')


