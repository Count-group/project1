import multiprocessing


def sum_chunk(chunk):
    return sum(chunk)


def parallel_sum(numbers, num_processes):
    pool = multiprocessing.Pool(processes=num_processes)
    chunk_size = len(numbers) // num_processes
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    results = pool.map(sum_chunk, chunks)
    pool.close()
    pool.join()
    return sum(results)


if __name__ == "__main__":
    numbers = list(range(1, 1001))
    num_processes = multiprocessing.cpu_count()
    result = parallel_sum(numbers, num_processes)
    print(f"Sum of numbers from 1 to 1000: {result}")
    