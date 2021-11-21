from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/912026705974136873/5OaCldRjZsVOewDu0gs7_8yllFtdiNJI41wUt8NiN4sjKMV59Uw4ORUWpoRgnah9eqrQ')
embed = DiscordEmbed(title='Successful checkout', description='', color='03b2f8')
embed.set_thumbnail(url='https://sun9-70.userapi.com/impf/763Y2_UgFOojM96QNOiwVB3qqC9f_zBTpnyo5w/qAuONuQB0gI.jpg?size=1080x1080&quality=95&sign=975fee700fa344929f7edeb9f31c5fd5&type=album')
embed.set_footer(text='HyPE Binance Autocheckout', icon_url='https://sun9-70.userapi.com/impf/763Y2_UgFOojM96QNOiwVB3qqC9f_zBTpnyo5w/qAuONuQB0gI.jpg?size=1080x1080&quality=95&sign=975fee700fa344929f7edeb9f31c5fd5&type=album')
embed.set_timestamp()
embed.add_embed_field(name='Quantity:', value='1', inline=False)
embed.add_embed_field(name='Product Id:', value='158036705914976256')

webhook.add_embed(embed)

response = webhook.execute()
