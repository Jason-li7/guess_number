import random

def guess_number_game():
    print("=" * 50)
    print("        欢迎来到猜数字游戏!")
    print("=" * 50)
    print("系统会随机生成一个1-100之间的整数")
    print("你需要猜出这个数字是多少")
    print("-" * 50)
    
    total_games = 0
    total_guesses = 0
    best_score = float('inf')
    
    while True:
        secret_number = random.randint(1, 100)
        guess_count = 0
        total_games += 1
        
        print(f"\n【第 {total_games} 轮游戏开始】")
        print("我已经想好了一个数字，请开始猜测吧！")
        
        while True:
            try:
                guess = input("\n请输入你的猜测 (1-100): ")
                
                if guess.lower() == 'q':
                    print("\n感谢游玩！再见！")
                    return
                
                guess = int(guess)
                
                if guess < 1 or guess > 100:
                    print("请输入1-100之间的整数！")
                    continue
                
                guess_count += 1
                
                if guess < secret_number:
                    print(f"太小了！再试试看~ (已猜 {guess_count} 次)")
                elif guess > secret_number:
                    print(f"太大了！再试试看~ (已猜 {guess_count} 次)")
                else:
                    print(f"\n恭喜你！猜对了！答案就是 {secret_number}")
                    print(f"你一共用了 {guess_count} 次猜中！")
                    total_guesses += guess_count
                    
                    if guess_count < best_score:
                        best_score = guess_count
                        print("🎉 新纪录！这是你最好的成绩！")
                    break
                    
            except ValueError:
                print("输入无效，请输入一个整数！")
        
        print(f"\n当前统计：")
        print(f"  - 总游戏轮数: {total_games}")
        print(f"  - 平均猜测次数: {total_guesses / total_games:.1f}")
        print(f"  - 最佳成绩: {best_score} 次")
        
        play_again = input("\n是否再来一局？(y/n): ").lower()
        if play_again != 'y':
            print("\n" + "=" * 50)
            print("游戏结束！感谢你的游玩！")
            print(f"最终统计：共玩了 {total_games} 轮，最佳成绩 {best_score} 次")
            print("=" * 50)
            break

if __name__ == "__main__":
    guess_number_game()
