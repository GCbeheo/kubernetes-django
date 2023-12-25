from django.http import HttpResponse
# from django_ratelimit.decorators import ratelimit
import time
import random
import asyncio
import multiprocessing

MILI_FACTOR = 1000

num_cores = multiprocessing.cpu_count()

async def consume_cpu(cpu_usage):
    time.sleep(cpu_usage / 1000)

async def consume_memory(memory_size):
    memory_block = bytearray(memory_size * 1024 * 1024)  # Convert to bytes
    # Simulate memory consumption by keeping a block of memory allocated
    await asyncio.sleep(0)  # Allow other tasks to run

async def hog():
    cpu_usage = random.randint(0, MILI_FACTOR)

    # Tiêu thụ tài nguyên CPU
    await consume_cpu(cpu_usage)

async def handle_request():
    tasks = []

    for i in range(random.randint(1, num_cores)):
        task = asyncio.create_task(hog())
        tasks.append(task)

    memory_size = random.randint(1, 10)  # Memory size in megabytes
    memory_task = asyncio.create_task(consume_memory(memory_size))
    tasks.append(memory_task)

    await asyncio.gather(*tasks)

# @ratelimit(key='user', rate='50/s', block=True)
async def index(request):
    # hold_time = random.randint(1, 5000)
    # time.sleep(hold_time / 1000)
    await handle_request()

    return HttpResponse("Request processed")
