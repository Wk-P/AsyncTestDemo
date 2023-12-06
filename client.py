import concurrent.futures
import requests

def process_task(num:str):
    with requests.get(url='http://127.0.0.1:8081', json={"num": num}) as response:

        # 处理任务的逻辑
        result = f"Response JSON: {response.json()}"
    return result

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor(max_workers=50) as executor:
        all_tasks = list()
        for num in range(1000):
            all_tasks.append(str(num))

        # 提交所有任务，返回一个 future 对象的列表
        futures = [executor.submit(process_task, task) for task in all_tasks]

        # 使用 as_completed 获取任务完成的顺序
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            print(result)
