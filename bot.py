print("Starting bot...")

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connected as {bot.user}")

@bot.event
async def on_member_join(member):
    try:
        await member.send(
            f"""
⚔️  Welcome to {member.guild.name}  ⚔️

**Getting Cleared for Multiplayer**
1. Read https://discord.com/channels/1381673661869588653/1394290515368738858 and follow the steps listed there to be cleared for multiplayer games.  
2. Download and install the required mods found in https://discord.com/channels/1381673661869588653/1385912784469885019.  Double-check they are installed in the correct load order.
3. Once everything is set up, read https://discord.com/channels/1381673661869588653/1386320776252227694 and https://discord.com/channels/1381673661869588653/1406917469490122793 to ensure balanced gameplay.

**Server Channels Overview**
• https://discord.com/channels/1381673661869588653/1446144776020824066 — Check regularly for important updates and server news.
• https://discord.com/channels/1381673661869588653/1444876328795897887 — Shows all cities available to play and where to find them.  
• https://discord.com/channels/1381673661869588653/1420809250573123655 — Post battle results and YouTube-worthy replays.  
• https://discord.com/channels/1381673661869588653/1446177139903823954 — Used to organize and program scenario-based games.

**Player Conduct & Expectations**
• Wait for all players before pressing Start.
• Build armies within 5 minutes to keep things moving.
• Deploy within 10 minutes once the battle starts.
• Stay mature — no griefing, rage-quitting, or toxicity.
• Play fair — follow rules and avoid exploits.

Make sure you understand everything before joining battles.
If you need guidance, seek out our server owner VO, or our admins rwx358 and dickborne.

“What we do in life echoes in eternity”

"""
        )
        print(f"DM sent to {member.name}")
    except Exception as e:
        print(f"Could not DM {member.name}: {e}")

bot.run(os.getenv("TOKEN"))
