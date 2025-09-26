# -*- coding: utf-8 -*-
import random

def judge_winner(player, computer):
    """勝敗を判定する関数"""
    if player == computer:
        return "引き分け"
    elif (player == "グー" and computer == "チョキ") or \
          (player == "チョキ" and computer == "パー") or \
          (player == "パー" and computer == "グー"):
        return "あなたの勝ち"
    else:
        return "コンピュータの勝ち"

def main():
    """メインゲームループ"""
    print("=" * 40)
    print("じゃんけんゲームへようこそ！")
    print("=" * 40)

    choices = ["グー", "チョキ", "パー"]

    wins = 0
    losses = 0
    draws = 0

    while True:
        print("\nじゃんけん...")
        print("1: グー, 2: チョキ, 3: パー, 0: 終了")

        player_input = input("あなたの選択を入力してください (1-3) または 0 で終了: ")

        if player_input == '0':
            print("ゲームを終了します。")
            print(f"最終結果 - 勝ち: {wins}, 負け: {losses}, 引き分け: {draws}")
            break

        if player_input not in ['1', '2', '3']:
            print("無効な入力です。もう一度試してください。")
            continue

        player_choice = choices[int(player_input) - 1]
        computer_choice = random.choice(choices)

        print(f"あなたの選択: {player_choice}")
        print(f"コンピュータの選択: {computer_choice}")

        result = judge_winner(player_choice, computer_choice)

        if result == "あなたの勝ち":
            wins += 1
        elif result == "コンピュータの勝ち":
            losses += 1
        else:
            draws += 1

        print(result)
        print(f"現在のスコア - 勝ち: {wins}, 負け: {losses}, 引き分け: {draws}")

if __name__ == "__main__":
    main()
