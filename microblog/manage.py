# バーチャルエンブサーバを立ち上げる際に使用
#!/usr/bin/env python
"""Djangoの管理タスク用のコマンドラインユーティリティです。"""
import os
import sys


def main():
	"""管理タスクを実行します。"""
	# 環境変数 'DJANGO_SETTINGS_MODULE' を 'microblog.settings' に設定。
	# 'DJANGO_SETTINGS_MODULE' は Django の設定を指定するためのもの。
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'microblog.settings')

	try:
		# Djangoの管理コマンドを実行するためのモジュールをインポート。
		from django.core.management import execute_from_command_line
	except ImportError as exc:
		# Djangoのインポートが失敗した場合、エラーメッセージを表示します。
		raise ImportError(
			"Djangoをインポートできませんでした。インストールされていて、"
			"PYTHONPATH環境変数で利用可能であることを確認してください。"
			"仮想環境のアクティベーションを忘れていませんか？"
		) from exc

	# コマンドラインから渡された引数を使用して、Djangoの管理コマンドを実行します。
	execute_from_command_line(sys.argv)


# このスクリプトがコマンドラインから直接呼び出された場合、main関数を実行します。
if __name__ == '__main__':
	main()
