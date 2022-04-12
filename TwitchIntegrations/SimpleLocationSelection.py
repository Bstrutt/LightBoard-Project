
from twitchio.ext import commands
import re
from rpi_ws281x import Color, PixelStrip, ws
from DisplayColorMatrix import display_color_matrix

blue = Color(0,0,255)
blank = Color(0,0,0)
green = Color(255,0,0)
red = Color(0,255,0)

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token='rejfa91ji58uty2kg9bnt50lppdz7y', prefix='!', initial_channels=['fluxsb'])
        self.single = False
        self.colorBoard =  [[0 for j in range(12)] for i in range(12)]
        for i in range(12):
            for j in range(12):
                self.colorBoard[i][j] = blank
        display_color_matrix(self.colorBoard)   

        

        
    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return
        
        print(message.content)
        
        matches = re.findall("\({1}[0-9]+,{1}[0-9]+,{1}(?:red|green|blue|blank){1}\){1}",message.content)

        if len(matches) > 0:
            if self.single:
                matches = [matches[0]]
            for match in matches:
                #[int(s) for s in 
                coordinates = [int(s)for s in re.findall("\d+", match)]
                print(coordinates)         

                if len(coordinates) > 2:
                    return
                if coordinates[0] > 11 or coordinates[0] < 0 or coordinates[1] > 11 or coordinates[1] < 0:
                    await commands.Context.send('Coords between 0 and 11')
                    return
                print(match)
                color = re.findall("red|green|blue|blank", match)[0]
                print(color)
                if color == "red":
                    self.colorBoard[coordinates[0]][coordinates[1]] = red
                elif color == "green":
                    self.colorBoard[coordinates[0]][coordinates[1]] = green
                elif color == "blue":
                    self.colorBoard[coordinates[0]][coordinates[1]] = blue
                elif color == "blank":
                    self.colorBoard[coordinates[0]][coordinates[1]] = blank
                    
            print(self.colorBoard)
            display_color_matrix(self.colorBoard)   
        
        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def single(self, ctx: commands.Context):
        
        if self.single == False:
            await ctx.send('single mode activated: one coord at a time.')
            self.Single = True
        if self.single == True:
            await ctx.send('single mode deactivated: separate coords by at least a space')
            self.single = False

bot = Bot()
bot.run()
# bot.run(