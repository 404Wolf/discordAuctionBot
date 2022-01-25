import aiosqlite
import discord
import utils


class db:
    """
    Database for auction bot.

    Attributes:
        name (str): filename of db
    """

    def __init__(self, name) -> utils.db.db:
        """
        Set up db instance.

        Args:
            name (str): filename of db

        Returns:
            utils.db.db: instance of this class
        """
        self.name = name
        pass

    async def setup(self) -> utils.db.db:
        """
        Load the sqllite db and set up auction.listing for all alive listings.

        Returns:
            utils.db.db: instance of this class
        """
        pass

    async def addGuild(self, guild: int, data: dict, overwrite=True) -> dict:
        """
        Create/overwrite config for a guild.

        Args:
            guild (int): guild id to create config for/overwrite config for
            data (dict): data for guild config (example: {"roles":{"manager":1234,"priorityBidder":5678}})
            overwrite (bool): if True replaces guild config with config being set, if False appends new config to old config

        Returns:
            dict: data for guild config of the guild id passed

        Raises:
            ValueError: if overwrite is False and there is no old data to merge
        """
        # merge old "config" data into new config data if overwrite is False
        # create entry in guild with primary key "config" if it doesn't exist yet
        # set "config" primary key for guild's table to the dict
        # return dict
        pass

    async def fetchGuild(self, guild: int) -> dict:
        """
        Fetch guild config.

        Args:
            guild (int): guild id to fetch config data for

        Returns:
            dict: data for guild config of the guild id passed

        Raises:
            ValueError: table for guild not found
        """
        # if guild has a table return the "config" primary key, else raise a value error
        pass

    async def guildExists(self, guild: int) -> bool:
        """
        Determine if there is a given guild existant in the db.

        Args:
            guild (int): guild id to check for

        Returns:
            bool: True if guild is in db, False if guild is not in db
        """
        # return True if guild in db, return False if guild not in db
        pass


    async def createListing(self, listing: utils.auction.listing) -> utils.db.db:
        """
        Create entry in db for the new listing.

        Args:
            listing (utils.auction.listing): the listing to add to the db

        Returns:
            utils.db.db: instance of this class

        Raises:
            TypeError: listing is not of the proper type (proper type is utils.auction.listing)
            IndexError: listing of the given id already exists
        """
        # generate id for listing (via generateId(guildId))
        # append to the guild's table in the db the listing data (using the attributes of the listing object passed)
        # return (self)
        pass

    async def updateListing(self, price: int, active: int, alive=True) -> utils.db.db:
        """
        Update a listing. Sets current bidder and price, and archives previous status.

        price (int): current price of listing
        active (int): discord id of active bidder
        alive (bool): status of the auction; True if ongoing, False if ended

        Returns:
            utils.db.db: instance of this class
        """
        pass

    async def getListingId(self) -> str:
        """
        Obtain a listing id from a channel id.

        Args:
            channel (int): id of channel associated with listing

        Returns:
            str: listing id

        Raises:
            ValueError: listing not found
        """
        pass

    async def fetchListing(self, id) -> utils.auction.listing:
        """
        Obtain a utils.auction.listing object from a given listing id

        Args:
            id (str): listing id

        Returns:
            utils.auction.listing: a listing object for the given auction id passed
        """
        pass

    async def generateId(self, guild: int) -> str:
        """
        Generate 18 digit random id. Ensure listing id does not already exist in guild's db. 

        Args:
            guild (int): guild id to generate an id for
        """
        # while true:
        # generate random 18 digit string
        # ensure id doesn't exist in guild's db
        # yield the id
        pass