import asyncio
import time

#สร้างฟังชั่น hello เพื่อปริ้นค่า แบบ asyncio
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")


# สร้าง ฟังชั่น main เพื่อกำหนด ตัวแปร task  กับ 2 และกำหนดให้ task ทำงานพร้อมกัน
# ใช้ gather เพื่อเก็บ task เป็นลิสไว้เพื่อที่จะได้่ประหยัดบรรทัด
async def main():
    task1 = asyncio.create_task(hello(1)) #returns immediately
#, the task is created await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')