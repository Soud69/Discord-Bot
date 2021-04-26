import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='69')
# Prefix = 69
bot.remove_command('help')
# Remove 69help Command

@bot.command()
async def av(ctx, member: discord.Member=None):
	if member is None:
		me = ctx.author
		av = me.avatar_url
	else:
		av = member.avatar_url
	eme = discord.Embed()
	eme.set_image(url=av)
	await ctx.reply(embed = eme, mention_author=True)
# 69av - 69av @Member Command

@bot.event
async def on_ready():
	print("Bot Is Online !")
	print(f"Bot Username: {bot.user.name}")
	print(f"Bot ID: {bot.user.id}")
	await bot.change_presence(status = discord.Status.idle, activity = discord.Game("Instagram @8Y"))
# When Bot Online print name + id + Change Bot Status

bot.run('YOUR BOT TOKEN')
# Bot Token From https://discord.com/developers/applications
