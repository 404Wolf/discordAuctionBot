import logging
import sys
import discord
from discord.commands import Option
from math import ceil
import utils
from dotenv import load_dotenv
from os import getenv

# setup logging
logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
logging.getLogger("discord").setLevel(logging.CRITICAL)

client = discord.Bot()


@client.command(name="list", description="list something for sale")
async def list(
    ctx: discord.Message,
    name: Option(
        str,
        "name of item being listed",
        required=True,
    ),
    starting: Option(
        int,
        "starting bid for item",
        required=True,
    ),
    ending: Option(
        str,
        "number of days until auction end",
        required=True,
    ),
) -> None:
    """
    List an item for sale in a server.

    Args:
        ctx (discord.message): the trigger message
        name (str): name of thing being listed
        starting (int): starting bid
        ending (int): number of days until auction end
    """
    pass


async def bid(ctx: discord.context) -> None:
    """
    Bid on an item.

    Args:
        ctx (discord.context): discord context
    """
    pass


buttons = (5, 10, 20, 50, 100)
buttons = [  # create a button object for every amount in the above tuple, in two rows of three buttons
    discord.ui.Button(
        label=f"Upbid ${amount}",
        style=discord.ButtonStyle.secondary,
        row=ceil(row * 0.5),
        custom_id=str(amount),
        callback=bid,
    )
    for row, amount in enumerate(buttons)
]

load_dotenv()  # load discord token from .env file
client.run(getenv("TOKEN"))