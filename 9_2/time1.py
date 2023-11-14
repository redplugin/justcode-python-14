import time

start_time = time.time()

bomb_timer = 3
while bomb_timer > 0:
    print(f"Осталось секунд {bomb_timer}...")
    time.sleep(3)
    bomb_timer = bomb_timer - 1

print("BooM!")
end_time = time.time()

print(f"Заняло времени {end_time - start_time}")











