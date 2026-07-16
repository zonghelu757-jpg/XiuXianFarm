def village_quest(player):

    while True:

        print()
        print("======村长======")
        print("1. 接受任务")
        print("2. 查看任务")
        print("3. 提交任务")
        print("0. 离开")

        choice = input("选择：")

        if choice == "1":

            print("村长:年轻人,帮我收集5个狼牙。")

        elif choice == "2":

            print(f"当前狼牙：{player.wolf_fang}/5")

        elif choice == "3":
            wolf_fang = player . items . get("狼牙", 0) 
            if player.items .get("狼牙", 0) >= 5:

                player. gold += 100
                player. items["狼牙"] -= 5

                print("任务完成！")
                print("获得100金币!")

            else:

                print(f"当前狼牙: {wolf_fang}/ 5")

        elif choice == "0":

            break

        else:

            print("输入错误！")