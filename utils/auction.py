import discord
import utils.db


class listing:
    """
    A live listing.

    Attributes:
        starting (int): starting bid
        ending (int): ending UNIX time
        price (int): current price of item
        alive (bool): status of the auction; True if ongoing, False if ended
    """

    def __init__(self, starting: int, ending: int, alive=True) -> utils.auction.listing:
        """
        Args:
            starting (int): starting bid
            ending (int): ending UNIX time
            alive (bool): status of the auction; True if ongoing, False if ended

        Returns:
            utils.auction.listing: instance of this class
        """
        pass

    async def list(self, name) -> utils.auction.listing:
        """
        Create an auction channel and generate an embed for a listing.

        Args:
            name (str): name of thing being listed

        Returns:
            utils.auction.listing: instance of this class
        """
        pass

    async def unlist(self) -> utils.auction.listing:
        """
        Archive the listing and remove the channel.

        Returns:
            utils.auction.listing: instance of this class
        """
        pass

    async def bid(amount: int) -> utils.auction.listing:
        """
        Bid on the listing.

        Args:
            amount (int): how much to upbid by
        """
        pass


async def ticker(listing: utils.auction.listing):
    """
    Keep channel topic countdowns up to date/ensure proper listing expiry.

    Args:
        listing (utils.auction.listing): a listing object of which to keep the channel topic up to date
    """
    pass
