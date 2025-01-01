class UserService:
    def __init__(self, ctx):
        self.ctx = ctx

    async def hello_sender(self):
        sender_username = self.ctx.author.name
        await self.ctx.send(f'Hello, {sender_username}!')