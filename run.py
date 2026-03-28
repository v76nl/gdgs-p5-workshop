import subprocess
import sys

def main():
    if len(sys.argv) < 2:
        print("使用方法:")
        print("  python run.py serve  : ローカルサーバーを起動し、プレビューを表示する")
        print("  python run.py build  : ローカルにHTMLを生成する(確認用)")
        print("  python run.py deploy : GitHub Pagesへ自動でデプロイする")
        return

    command = sys.argv[1]

    if command == "serve":
        print("ローカルサーバーを起動します。ブラウザで http://127.0.0.1:8000 にアクセスしてください。")
        print("終了するには Ctrl+C を押してください。")
        # mkdocs serveコマンドを実行する
        subprocess.run(["mkdocs", "serve"])
        
    elif command == "build":
        print("HTMLファイルをビルドします...")
        # mkdocs buildコマンドを実行する
        subprocess.run(["mkdocs", "build"])
        print("ビルドが完了しました。site/ フォルダにHTMLが生成されました。")

    elif command == "deploy":
        print("GitHub Pagesへデプロイします...")
        # mkdocs gh-deployコマンドを実行する
        subprocess.run(["mkdocs", "gh-deploy"])
        print("デプロイが完了しました。")
        
    else:
        print(f"不明なコマンドです: {command}")

if __name__ == "__main__":
    main()