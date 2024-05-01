import socket

# socket.socket(): ソケットオブジェクトの作成
# AF_INET: IPv4 ベースのアドレス体系を使用することを示す
# SOCK_STREAM: TCP を使用することを示す
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# socket.bind(): IPアドレスとポート番号を作成したソケットオブジェクトに紐付ける
s.bind(('127.0.0.1', 60001))

# socket.listen(): クライアントからの入力待ち状態になる
# 1: 並列的に処理できるクライアント数を1つに指定する
s.listen(1)

try:
    while True:
        # socket.accept(): クライアントからの接続を待ち受ける
        # conn: 新しく作成したソケットオブジェクト
        # addr: クライアントのアドレス情報（クライアントのIPアドレス、クライアントのポート番号）
        conn, addr = s.accept()

        # クライアントのIPアドレスとポートを表示する
        print(f'Source IP address: {addr}')

        # クライアントのソケットにデータを送信する
        conn.send(b'Hello, client!')

        # クライアントのソケットオブジェクトを削除する
        conn.close()
except KeyboardInterrupt:
    print("Shutting down the server")
    s.close()

