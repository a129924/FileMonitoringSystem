import asyncio
from concurrent.futures import ThreadPoolExecutor
from asyncio import AbstractEventLoop

class AsyncPackage:
    def __init__(self, func, args):
        self._func = func
        self._args = args
        
    @property
    def args(self):
        return self._args
        
    async def do_async_job(self, loop:AbstractEventLoop, pool: ThreadPoolExecutor, arg):
        await loop.run_in_executor(pool, self._func, arg)

    async def do_many_variable_async_job(self, loop:AbstractEventLoop, pool:ThreadPoolExecutor, arg):
        await loop.run_in_executor(pool, self._func, *arg)

    async def main(self):
        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor() as pool:
            tasks = [asyncio.create_task(self.do_async_job(loop, pool, arg)) for arg in self._args]
            await asyncio.gather(*tasks)

    def run(self):
        asyncio.run(self.main())
