import discord
from discord.ext import commands

intenciones = discord.Intents.default()
intenciones.message_content=True

bot = commands.Bot(command_prefix = "$", intents = intenciones)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("Olvidaste subir la imagen :(")

@bot.event
async def on_ready():
    print("El bot está en línea")

@bot.command()
async def check(ctx):
    if ctx.message.attachment:
        for archivo in ctx.message.attachment:
            nombre =  archivo.filename
            await archivo.save(f"./img/{nombre}")
        await ctx.send("Se guardó exitosamente la información.")
    else:
        await ctx.send("Para que funcione el comando, necesita una imagen.")

bot.run("Token")
