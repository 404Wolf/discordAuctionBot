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

    async def setup() -> utils.db.db:
        """
        Load the sqllite db and set up auction.listing for all alive listings

        Returns:
            utils.db.db: instance of this class
        """
        pass

    async def update(price: int, active: int, alive=True) -> utils.db.db:
        """
        Update a listing. Sets current bidder and price, and archives previous status.

        price (int): current price of listing
        active (int): discord id of active bidder
        alive (bool): status of the auction; True if ongoing, False if ended

        Returns:
            utils.db.db: instance of this class
        """
        pass

    async def id() -> str:
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

    async def fetch(id) -> utils.auction.listing:
        """
        Obtain a utils.auction.listing object from a given listing id

        Args:
            id (str): listing id

        Returns:
            utils.auction.listing: a listing object for the given auction id passed
        """
        pass
