import discord
import asyncio

intents = discord.Intents.default()
intents.message_content = True

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from the Discord Developer Portal
client = discord.Client(intents=intents)

structures = {}

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!set_timer'):
        args = message.content.split(maxsplit=2)
        if len(args) != 3:
            await message.channel.send('Invalid usage. Use !set_timer <structure_name> <time_in_minutes>')
            return

        structure_name = args[1]
        try:
            time_in_minutes = int(args[2])
            if time_in_minutes <= 0:
                await message.channel.send('Please provide a positive value for the timer.')
                return
        except ValueError:
            await message.channel.send('Invalid time value. Please provide a valid number of minutes.')
            return

        # Store the structure and timer in the 'structures' dictionary
        timers = structures.get(structure_name, [])
        timers.append({
            'user_id': message.author.id,
            'time_in_minutes': time_in_minutes,
        })
        structures[structure_name] = timers

        await message.channel.send(f'Timer set for {structure_name} - {time_in_minutes} minutes.')

    elif message.content.startswith('!check_timers'):
        if not structures:
            await message.channel.send('No timers are currently set.')
        else:
            response = 'Current timers:\n'
            for structure_name, timers in structures.items():
                response += f'{structure_name}:'
                for timer in timers:
                    user = client.get_user(timer['user_id'])
                    response += f' {user.mention} ({timer["time_in_minutes"]} minutes),'
                response = response.rstrip(',') + '\n'
            await message.channel.send(response)

@client.event
async def check_timers():
    await client.wait_until_ready()
    while not client.is_closed():
        await asyncio.sleep(60)  # Check every minute

        for structure_name, timers in structures.items():
            for timer in timers:
                timer['time_in_minutes'] -= 1

        expired_timers = [(structure_name, timer) for structure_name, timers in structures.items() for timer in timers if timer['time_in_minutes'] <= 0]

        for structure_name, timer in expired_timers:
            user = client.get_user(timer['user_id'])
            await user.send(f'{user.mention}, your timer for {structure_name} is up!')
            structures[structure_name].remove(timer)

client.loop.create_task(check_timers())
# Replace 'YOUR_BOT_TOKEN' with your actual bot token from the Discord Developer Portal
client.run('MTEzMzc1NDc3NjQ2MzYyNjI4MA.GOB_gq.Y0kNW-W2XDmpznOwesFycVDLKRsWw1YSqFndSA')
