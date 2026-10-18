import random
tasks = ["张三","李四","王五","赵六","孙七"]

def show_menu():
    print("1.抽奖")
    print("2.查看剩余名单")
    print("3.退出")

def view_tasks(tasks):
    for i in range(0, len(tasks)):
        print(f"{tasks[i]}")

def draw_lottery(tasks):
        if not tasks:
            return
        result = tasks[random.randrange(0, len(tasks))]
        return result

while True:
    show_menu()
    choice = int(input("请按数字键选择"))
    if choice == 1:
        result = draw_lottery(tasks)
        if not result:
            print("已经抽完了")
            continue
        print("恭喜",result,"中奖")
        tasks.remove(result)
    elif choice == 2:
        view_tasks(tasks)
    elif choice == 3:
        print("抽奖结束")
        break
    else:
        print("请输入有效数字")



