def onServerInfo(server, info):
  if (info.isPlayer == 0):
    pass
  else:
    if info.content == '!!restart':
      server.say('restarting')
      server.stop()
      server.start()
    if info.content == '!!op':
      server.execute('op ' + info.player)


def on_info(server, info):
    if info.is_user:
      if info.content == '!!op':
        server.execute('op ' + info.player)
      if info.content == '!!restart':
        server.restart()
