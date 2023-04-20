"""
# 멀티프로세스 간 몇개 어트리뷰트를 공유하는 빠른 방법이 필요한 경우, 사용
"""
import multiprocessing as mp


def my_process(namespace):
    print(f"In Child Process : {namespace}")
    namespace.var = 2


def main():
    manager = mp.Manager()
    namespace = manager.Namespace()

    namespace.var = 1
    print(f"First Namespace Var : {namespace}")

    process = mp.Process(target=my_process, args=(namespace,))
    process.start()
    process.join()
    print(f"Final Namespace Var : {namespace}")


if __name__ == "__main__":
    main()
