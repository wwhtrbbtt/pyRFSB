class message_formats():
    def __init__(self, TOKEN) -> None:
        self.url = f"wss://zoom.raidforums.com/socket.io/?token={TOKEN}&EIO=3&transport=websocket"

    def ping(self) -> str:
        """
        The ping. Classik, yet cool. Has to be send every 25 seconds,
        the connection times out after 1m
        """
        return "2"

    def start_sequence(self) -> list:
        """
        These two messages have to be send at the very start. 
        iterate over them or something lol
        """
        return [
            "40/member",
            '42/member,["getoldmsg",{"ns":"50"}]',
        ]

    def send_message(self, text):
        """
        You can easily send a message
        """
        return '42/member,["message",{"msg":"' + text + '","nickto":"","uidto":0,"colorsht":"","font":"","size":"","bold":"","type":"shout"}]'
