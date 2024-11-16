import schedule
import time


def my_task():
    print("定期タスク実行中")

def my_task_2():
    print("定期タスク実行中!!!")


# 毎分実行
# schedule.every(1).minutes.do(my_task)

# 10秒ごとにタスクをスケジュール
schedule.every(10).seconds.do(my_task)

# 毎日10時に実行
schedule.every().day.at("01:27").do(my_task_2)

while True:
    schedule.run_pending()
    time.sleep(1)  # 無駄なCPU使用率を抑えるための待機