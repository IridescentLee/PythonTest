import asyncio
import time


async def run(x):
    """
    模拟异步任务
    :param x:
    :return:
    """
    print('开始', x)
    await asyncio.sleep(2)
    print('结束', x)
    return f'{x}的数据'


def call_back(future):
    print('call_back', future.result())


async def main():
    tasks = []
    url = ['阿力', '惊动', '摆渡', '哔哩哔哩']
    t1 = time.time()

    for i in url:
        coroutine = run(i)
        # task = asyncio.ensure_future(coroutine)
        task = asyncio.create_task(coroutine)
        task.add_done_callback(call_back)
        tasks.append(task)

    # return await asyncio.wait(tasks)
    return await asyncio.gather(*tasks)
    # print('耗时%.2f' % (time.time() - t1))


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # done = loop.run_until_complete(main())
    # done, pending = asyncio.run(main())
    done = asyncio.run(main())
    for d in done:
        # print('返回值', d.result())
        print('返回值', d)
