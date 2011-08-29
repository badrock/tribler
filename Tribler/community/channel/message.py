from Tribler.Core.dispersy.message import DelayMessage

class DelayMessageReqChannelMessage(DelayMessage):
    """
    Raised during ChannelCommunity.check_ if the channel message has not been received yet.
    """
    def __init__(self, delayed, community = None):
        if __debug__:
            from Tribler.Core.dispersy.message import Message
        assert isinstance(delayed, Message.Implementation)
        
        if not community:
            community = delayed.community
        cid = community.cid.encode("HEX")
        
        # the footprint that will trigger the delayed packet
        footprint = "".join(("channel",
                             " Community:", cid))

        # the request message that asks for the message that will
        # trigger the delayed packet
        meta = community.get_meta_message(u"missing-channel")
        message = meta.implement(meta.authentication.implement(),
                                 meta.distribution.implement(community.global_time),
                                 meta.destination.implement(delayed.address),
                                 meta.payload.implement())

        super(DelayMessageReqChannelMessage, self).__init__("Missing channel-message", footprint, message, delayed)