def get_mobile():
    """
    The Gateway's IDENTIFY packet contains a properties field, containing $os, $browser and $device fields.
    Discord uses that information to know when your phone client and only your phone client has connected to Discord,
    from there they send the extended presence object.
    The exact field that is checked is the $browser field. If it's set to Discord Android on desktop,
    the mobile indicator is is triggered by the desktop client. If it's set to Discord Client on mobile,
    the mobile indicator is not triggered by the mobile client.
    The specific values for the $os, $browser, and $device fields are can change from time to time.
    """
    import ast
    import inspect
    import re
    import discord

    def source(o):
        s = inspect.getsource(o).split("\n")
        indent = len(s[0]) - len(s[0].lstrip())

        return "\n".join(i[indent:] for i in s)

    source_ = source(discord.gateway.DiscordWebSocket.identify)
    patched = re.sub(
        r'([\'"]\$browser[\'"]:\s?[\'"]).+([\'"])',
        r"\1Discord Android\2",
        source_,
    )

    loc = {}
    exec(compile(ast.parse(patched), "<string>", "exec"), discord.gateway.__dict__, loc)
    return loc["identify"]