# -*- coding: utf-8 -*-
import copy


def onServerInfo(server, info):
	if info.isPlayer == 1:
		if info.content.startswith('!!tp'):
			args = info.content.split(' ')
			if args[0] == '!!tp':
				if len(args) == 1:
					server.tell(info.player, '使用 !!tp 玩家名 传送到此玩家')
				elif len(args) == 2:
					server.execute('execute at ' + str(args[1]) + ' run tp ' + info.player + ' ' + str(args[1]))

		if info.content in ['!!overworld', '!!nether', '!!end'] and hasattr(server, 'MCDR'):
			api = server.get_plugin_instance('PlayerInfoAPI')
			pos = tuple(api.getPlayerInfo(server, info.player, 'Pos'))
			dim = api.getPlayerInfo(server, info.player, 'Dimension')
			if info.content == '!!overworld':
				if dim in [-1, 'minecraft:the_nether']:
					pos = pos[0] * 8, pos[1], pos[2] * 8
				server.reply(info, '正在传送至主世界 {}'.format(pos))
				server.execute('execute in minecraft:overworld run tp {} {} {} {}'.format(info.player, *pos))

			elif info.content == '!!nether':
				if dim in [0, 'minecraft:overworld']:
					pos = pos[0] / 8, pos[1], pos[2] / 8
				server.reply(info, '正在传送至地狱 {}'.format(pos))
				server.execute('execute in minecraft:the_nether run tp {} {} {} {}'.format(info.player, *pos))

			elif info.content == '!!end':
				server.reply(info, '正在传送至末地 (0, 80, 0)')
				server.execute('execute in minecraft:the_end run tp {} 0 80 0'.format(info.player))


def on_info(server, info):
	info2 = copy.deepcopy(info)
	info2.isPlayer = info2.is_player
	onServerInfo(server, info2)


def on_load(server, old):
	server.add_help_message('!!tp <玩家>', '传送至玩家，自动识别维度')
	server.add_help_message('!!overworld', '传送至主世界对应坐标')
	server.add_help_message('!!nether', '传送至地狱对应坐标')
	server.add_help_message('!!end', '传送至末地 (0, 80, 0)')
