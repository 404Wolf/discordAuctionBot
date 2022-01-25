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

@client.event()
async def on_guild_join(guild):
    """
    Set up new guild in db, create needed roles for new guild, or ignore if guild already exists.

    Args:
        guild (discord.guild): guild that the bot just joined
    """
    # send welcome/help message
    #
    # create empty dict, and then add role/catagory/channel ids to the dict as the setup process proceeds
    #
    # check if guild already exists in the db:
    # if guild already exists then return, else check perms of bot and make sure 
    #
    # create "Bid Priority" role; a role which allows access to locked auctions
    # create "Bid Manager" role; and give it to anyone who already has admin perms, or roles named "staff", "admin", ext
    # dm anyone who automatically was determined to be a bid manager telling them how they can assign new managers (the bid manager role just created)
    #
    # create "Auctions" catagory
    #
    # store guild config data in db
    pass

@client.command(name="list", description="list something for sale")
async def list(
    message: discord.Message,
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
        message (discord.message): the trigger message
        name (str): name of thing being listed
        starting (int): starting bid
        ending (int): number of days until auction end
    """
    # create empty dict to store ids for chats created
    #
    # check that listing doesn't already exist; if it does return an error
    # create channel for listing (store channel id)
    # send message in channel with embed showing details (store message id)
    # attach the bid buttons to the message
    #
    # create server event for listing
    # create db entry for listing
    pass


async def bid(message: discord.message) -> None:
    """
    Trigger a DM-Confirmation prompt to bid on an item

    Args:
        message (discord.message): discord context   
    """
    # detect which button was clicked and set a variable to amount shown on button clicked
    # update the db with the new bid
    # fetch message id of 
    # change the embed to new current bid
    # dm previous bidder, or don't if the new bidder is the same as the previous bidder
    # modify db entry for auction with new bid and bidder
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