import asyncio
import time
async def task(name, delay):
    await asyncio.sleep(delay)
    print(f'[Task {name}] is completed (delay: {delay} sec)')


async def run_tasks():
    delays = [1.5, 0.5, 1.0, 2.0, 0.1]
    parallel_start = time.time()
    
    tasks = [task(i, d) for i, d in enumerate(delays)]
    await asyncio.gather(*tasks)
    
    parallel_time = time.time() - parallel_start

    sequential_start = time.time()
    
    for i, d in enumerate(delays):
        await task(i, d)
        
    sequential_time = time.time() - sequential_start

    print("\n" + "="*40)
    print(f'Consistent: {sequential_time:.2f} sec')
    print(f'Parllel work:  {parallel_time:.2f} sec')
    print(f'Difference: X {sequential_time / parallel_time:.2f}')
    print("="*40)


def main():
    asyncio.run(run_tasks())


if __name__ == '__main__':
    main()