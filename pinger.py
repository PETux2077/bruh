print("Loading...")
import os
import sys
import discord
import asyncio
import time
from discord.ext import commands
from discord.utils import get
import youtube_dl
import pafy

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="$", intents=intents)

client = commands.Bot(command_prefix="$" , intents = discord.Intents.all())

@bot.event
async def on_ready():
  print("We haved logged as {0.user}".format(bot))

@bot.command()
async def ping(ctx, a: str):
  await ctx.channel.send("Ile razy chcesz go / ja zapingowac?Od 1 do 20")

  try:
    message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
    timeout=30.0)

  except asyncio.TimeoutError:
    await ctx.channel.send("Z jakiego pozwolenia ty mnie ignorujesz?")

  else:
    if message.content.lower() == "1":
      await ctx.channel.send(a)

    elif a == ("@Ultimate Pinger"):
      ctx.channel.send("Po co mnie pingowac? Jusz tu jestem!")

    elif message.content.lower() == "2":
      await ctx.channel.purge(limit = 2)
      await ctx.channel.send(a)
      await ctx.channel.send(a)   
      await ctx.channel.send("Zawołać sprzontaczke?(tak/nie)")
      try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)
      
      except asyncio.TimeoutError:
        return

      if message.content.lower() == "nie":
        return

      elif message.content.lower() == "tak":
        await ctx.channel.purge(limit = 4)

      else:
        return
    elif message.content.lower() == "3":
      await ctx.channel.purge(limit = 2)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)  
      await ctx.channel.send("Zawołać sprzontaczke?(tak/nie)")
      try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)
      
      except asyncio.TimeoutError:
        return

      if message.content.lower() == "nie":
        return

      elif message.content.lower() == "tak":
        await ctx.channel.purge(limit = 5)

      else:
        return
    
    elif message.content.lower() == "4":
      await ctx.channel.purge(limit = 2)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send("Zawołać sprzontaczke?(tak/nie)")
      try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)
      
      except asyncio.TimeoutError:
        return

      if message.content.lower() == "nie":
        return

      elif message.content.lower() == "tak":
        await ctx.channel.purge(limit = 6)

      else:
        return
    elif message.content.lower() == "5":
      await ctx.channel.purge(limit = 2)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send("Zawołać sprzontaczke?(tak/nie)")
      try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)
      
      except asyncio.TimeoutError:
        return

      if message.content.lower() == "nie":
        return

      elif message.content.lower() == "tak":
        await ctx.channel.purge(limit = 7)

      else:
        return
    elif message.content.lower() == "6":
      await ctx.channel.purge(limit = 2)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send("Zawołać sprzontaczke?(tak/nie)")
      try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)
      
      except asyncio.TimeoutError:
        return

      if message.content.lower() == "nie":
        return

      elif message.content.lower() == "tak":
        await ctx.channel.purge(limit = 8)

      else:
        return
    elif message.content.lower() == "7":
      await ctx.channel.purge(limit = 2)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send("Zawołać sprzontaczke?(tak/nie)")
      try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)
      
      except asyncio.TimeoutError:
        return

      if message.content.lower() == "nie":
        return

      elif message.content.lower() == "tak":
        await ctx.channel.purge(limit = 9)

      else:
        return
    elif message.content.lower() == "8":
      await ctx.channel.purge(limit = 2)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send("Zawołać sprzontaczke?(tak/nie)")
      try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)
      
      except asyncio.TimeoutError:
        return

      if message.content.lower() == "nie":
        return

      elif message.content.lower() == "tak":
        await ctx.channel.purge(limit = 10)

      else:
        return
    elif message.content.lower() == "9":
      await ctx.channel.purge(limit = 2)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send("Zawołać sprzontaczke?(tak/nie)")
      try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)
      
      except asyncio.TimeoutError:
        return

      if message.content.lower() == "nie":
        return

      elif message.content.lower() == "tak":
        await ctx.channel.purge(limit = 11)

      else:
        return
    elif message.content.lower() == "10":
      await ctx.channel.purge(limit = 2)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send("Zawołać sprzontaczke?(tak/nie)")
      try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)
      
      except asyncio.TimeoutError:
        return

      if message.content.lower() == "nie":
        return

      elif message.content.lower() == "tak":
        await ctx.channel.purge(limit = 12)

      else:
        return
    elif message.content.lower() == "11":
      await ctx.channel.purge(limit = 2)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send("Zawołać sprzontaczke?(tak/nie)")
      try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)
      
      except asyncio.TimeoutError:
        return

      if message.content.lower() == "nie":
        return

      elif message.content.lower() == "tak":
        await ctx.channel.purge(limit = 13)

      else:
        return
    elif message.content.lower() == "12":
      await ctx.channel.purge(limit = 2)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send("Zawołać sprzontaczke?(tak/nie)")
      try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)
      
      except asyncio.TimeoutError:
        return

      if message.content.lower() == "nie":
        return

      elif message.content.lower() == "tak":
        await ctx.channel.purge(limit = 14)

      else:
        return
    elif message.content.lower() == "13":
      await ctx.channel.purge(limit = 2)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send("Zawołać sprzontaczke?(tak/nie)")
      try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)
      
      except asyncio.TimeoutError:
        return

      if message.content.lower() == "nie":
        return

      elif message.content.lower() == "tak":
        await ctx.channel.purge(limit = 15)

      else:
        return
    elif message.content.lower() == "14":
      await ctx.channel.purge(limit = 2)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send("Zawołać sprzontaczke?(tak/nie)")
      try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)
      
      except asyncio.TimeoutError:
        return

      if message.content.lower() == "nie":
        return

      elif message.content.lower() == "tak":
        await ctx.channel.purge(limit = 16)

      else:
        return
    elif message.content.lower() == "15":
      await ctx.channel.purge(limit = 2)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send("Zawołać sprzontaczke?(tak/nie)")
      try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)
      
      except asyncio.TimeoutError:
        return

      if message.content.lower() == "nie":
        return

      elif message.content.lower() == "tak":
        await ctx.channel.purge(limit = 17)

      else:
        return
    elif message.content.lower() == "16":
      await ctx.channel.purge(limit = 2)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send("Zawołać sprzontaczke?(tak/nie)")
      try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)
      
      except asyncio.TimeoutError:
        return

      if message.content.lower() == "nie":
        return

      elif message.content.lower() == "tak":
        await ctx.channel.purge(limit = 18)

      else:
        return

    elif message.content.lower() == "17":
      await ctx.channel.purge(limit = 2)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send("Zawołać sprzontaczke?(tak/nie)")
      try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)
      
      except asyncio.TimeoutError:
        return

      if message.content.lower() == "nie":
        return

      elif message.content.lower() == "tak":
        await ctx.channel.purge(limit = 19)

      else:
        return
    elif message.content.lower() == "18":
      await ctx.channel.purge(limit = 2)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send("Zawołać sprzontaczke?(tak/nie)")
      try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)
      
      except asyncio.TimeoutError:
        return

      if message.content.lower() == "nie":
        return

      elif message.content.lower() == "tak":
        await ctx.channel.purge(limit = 20)

      else:
        return

    elif message.content.lower() == "19":
      await ctx.channel.purge(limit = 2)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send("Zawołać sprzontaczke?(tak/nie)")
      try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)
      
      except asyncio.TimeoutError:
        return

      if message.content.lower() == "nie":
        return

      elif message.content.lower() == "tak":
        await ctx.channel.purge(limit = 21)

      else:
        return
    elif message.content.lower() == "20":
      await ctx.channel.purge(limit = 2)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      time.sleep(0.01)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send(a)
      await ctx.channel.send("Zawołać sprzontaczke?(tak/nie)")
      try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)
      
      except asyncio.TimeoutError:
        return

      if message.content.lower() == "nie":
        return

      elif message.content.lower() == "tak":
        await ctx.channel.purge(limit = 22)

      else:
        return

    else:
      await ctx.channel.send("Nie bende tego robil")

@bot.command()
@commands.has_role("Admin")
async def sprzontaczka(ctx, b:int):
  await ctx.channel.purge( limit = b)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@commands.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await client.kick(member)
  await ctx.send(f'User {member} has been kick')

@bot.command()
async def awa(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)


class Player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        self.song_queue = {}

        self.setup()

    def setup(self):
        for guild in self.bot.guilds:
            self.song_queue[guild.id] = []

    async def check_queue(self, ctx):
        if len(self.song_queue[ctx.guild.id]) > 0:
            await self.play_song(ctx, self.song_queue[ctx.guild.id][0])
            self.song_queue[ctx.guild.id].pop(0)

    async def search_song(self, amount, song, get_url=False):
        info = await self.bot.loop.run_in_executor(None, lambda: youtube_dl.YoutubeDL({"format" : "bestaudio", "quiet" : True}).extract_info(f"ytsearch{amount}:{song}", download=False, ie_key="YoutubeSearch"))
        if len(info["entries"]) == 0: return None

        return [entry["webpage_url"] for entry in info["entries"]] if get_url else info

    async def play_song(self, ctx, song):
        url = pafy.new(song).getbestaudio().url
        ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url)), after=lambda error: self.bot.loop.create_task(self.check_queue(ctx)))
        ctx.voice_client.source.volume = 0.5

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            return await ctx.send("You are not connected to a voice channel, please connect to the channel you want the bot to join.")

        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()

        await ctx.author.voice.channel.connect()

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client is not None:
            return await ctx.voice_client.disconnect()

        await ctx.send("I am not connected to a voice channel.")

    @commands.command()
    async def play(self, ctx, *, song=None):
        if song is None:
            return await ctx.send("You must include a song to play.")

        if ctx.voice_client is None:
            if ctx.author.voice is None:
              return await ctx.send("You are not connected to a voice channel, please connect to the channel you want the bot to join.")

            if ctx.voice_client is not None:
                await ctx.voice_client.disconnect()

            await ctx.author.voice.channel.connect()

        # handle song where song isn't url
        if not ("youtube.com/watch?" in song or "https://youtu.be/" in song):
            await ctx.send("Searching for song, this may take a few seconds.")

            result = await self.search_song(1, song, get_url=True)

            if result is None:
                return await ctx.send("Sorry, I could not find the given song, try using my search command.")

            song = result[0]

        if ctx.voice_client.source is not None:
            queue_len = len(self.song_queue[ctx.guild.id])

            if queue_len < 10:
                self.song_queue[ctx.guild.id].append(song)
                return await ctx.send(f"I am currently playing a song, this song has been added to the queue at position: {queue_len+1}.")

            else:
                return await ctx.send("Sorry, I can only queue up to 10 songs, please wait for the current song to finish.")

        await self.play_song(ctx, song)
        await ctx.send(f"Now playing: {song}")

    @commands.command()
    async def search(self, ctx, *, song=None):
        if song is None: return await ctx.send("You forgot to include a song to search for.")

        await ctx.send("Searching for song, this may take a few seconds.")

        info = await self.search_song(5, song)

        embed = discord.Embed(title=f"Results for '{song}':", description="*You can use these URL's to play an exact song if the one you want isn't the first result.*\n", colour=discord.Colour.red())
        
        amount = 0
        for entry in info["entries"]:
            embed.description += f"[{entry['title']}]({entry['webpage_url']})\n"
            amount += 1

        embed.set_footer(text=f"Displaying the first {amount} results.")
        await ctx.send(embed=embed)

    @commands.command()
    async def queue(self, ctx): # display the current guilds queue
        if len(self.song_queue[ctx.guild.id]) == 0:
            return await ctx.send("There are currently no songs in the queue.")

        embed = discord.Embed(title="Song Queue", description="", colour=discord.Colour.dark_gold())
        i = 1
        for url in self.song_queue[ctx.guild.id]:
            embed.description += f"{i}) {url}\n"

            i += 1

        embed.set_footer(text="Thanks for using me!")
        await ctx.send(embed=embed)

    @commands.command()
    async def skip(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send("I am not playing any song.")

        if ctx.author.voice is None:
            return await ctx.send("You are not connected to any voice channel.")

        if ctx.author.voice.channel.id != ctx.voice_client.channel.id:
            return await ctx.send("I am not currently playing any songs for you.")

        poll = discord.Embed(title=f"Vote to Skip Song by - {ctx.author.name}#{ctx.author.discriminator}", description="**80% of the voice channel must vote to skip for it to pass.**", colour=discord.Colour.blue())
        poll.add_field(name="Skip", value=":white_check_mark:")
        poll.add_field(name="Stay", value=":no_entry_sign:")
        poll.set_footer(text="Voting ends in 15 seconds.")

        poll_msg = await ctx.send(embed=poll) # only returns temporary message, we need to get the cached message to get the reactions
        poll_id = poll_msg.id

        await poll_msg.add_reaction(u"\u2705") # yes
        await poll_msg.add_reaction(u"\U0001F6AB") # no
        
        await asyncio.sleep(15) # 15 seconds to vote

        poll_msg = await ctx.channel.fetch_message(poll_id)
        
        votes = {u"\u2705": 0, u"\U0001F6AB": 0}
        reacted = []

        for reaction in poll_msg.reactions:
            if reaction.emoji in [u"\u2705", u"\U0001F6AB"]:
                async for user in reaction.users():
                    if user.voice.channel.id == ctx.voice_client.channel.id and user.id not in reacted and not user.bot:
                        votes[reaction.emoji] += 1

                        reacted.append(user.id)

        skip = False

        if votes[u"\u2705"] > 0:
            if votes[u"\U0001F6AB"] == 0 or votes[u"\u2705"] / (votes[u"\u2705"] + votes[u"\U0001F6AB"]) > 0.79: # 80% or higher
                skip = True
                embed = discord.Embed(title="Skip Successful", description="***Voting to skip the current song was succesful, skipping now.***", colour=discord.Colour.green())

        if not skip:
            embed = discord.Embed(title="Skip Failed", description="*Voting to skip the current song has failed.*\n\n**Voting failed, the vote requires at least 80% of the members to skip.**", colour=discord.Colour.red())

        embed.set_footer(text="Voting has ended.")

        await poll_msg.clear_reactions()
        await poll_msg.edit(embed=embed)

        if skip:
            ctx.voice_client.stop()


    @commands.command()
    async def pause(self, ctx):
        if ctx.voice_client.is_paused():
            return await ctx.send("I am already paused.")

        ctx.voice_client.pause()
        await ctx.send("The current song has been paused.")

    @commands.command()
    async def resume(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send("I am not connected to a voice channel.")

        if not ctx.voice_client.is_paused():
            return await ctx.send("I am already playing a song.")
        
        ctx.voice_client.resume()
        await ctx.send("The current song has been resumed.")

    @commands.command()
    async def fs(self, ctx):
      ctx.voice_client.stop()


async def setup():
    await bot.wait_until_ready()
    bot.add_cog(Player(bot))

bot.loop.create_task(setup())

bot.run("OTA5NTUxMDA5NTY1NjUwOTY0.YZF7Yw.ff4L8hXwGq_fmb9i0gZfG-Y3mas")
