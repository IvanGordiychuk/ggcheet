import requests
import asyncio
import aiohttp
import time

start_time = time.time()
async def get_page(session, category: str, page_id: int) -> str:
    if page_id:
        url = 'https://www.ozon.ru/brand/{0}/?page={1}'.format(category, page_id)
    else:
        url = 'https://www.ozon.ru/brand/{0}/'.format(category)

    async with session.get(url) as response:
        print('get url: {0}'.format(url))
        response_text = await response.text()
    return response_text


async def load_data():
    category_list = ['adidas-144082850', 'puma-87235756']
    async with aiohttp.ClientSession() as session:
        tasks = []
        for category in category_list:
            for page_id in range(50):
                task = asyncio.create_task(get_page(session,category,page_id))
                tasks.append(task)
            # обрабатываем полученный текст, сохраняем в файл/базу
        await asyncio.gather(*tasks)

asyncio.run(load_data())

end_time = time.time() - start_time
print(f'\nExecution time: {end_time} seconds')
