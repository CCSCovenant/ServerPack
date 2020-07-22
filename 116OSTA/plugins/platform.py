def on_info(server, info):
  if info.is_player and info.content == '!!platform':
    server.execute('execute at ' + info.player + ' run fill ~5 ~ ~5 ~-5 ~ ~-5 minecraft:iron_block')
