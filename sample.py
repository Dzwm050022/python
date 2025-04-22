import random
import string

def generate(kwargs):
    num = kwargs.get('num', 1)

    for _ in range(num):
        res = {}
        for k, v in kwargs.items():
            if k == 'num':
                continue

            if isinstance(k, type):
                if k == int:
                    res['int'] = random.randint(*v['datarange'])
                elif k == float:
                    res['float'] = random.uniform(*v['datarange'])
                elif k == str:
                    res['str'] = ''.join(random.choice(v['datarange']) for _ in range(v['len']))
                elif k == list:
                    res['list'] = [random.randint(*v['items'][int]['datarange']) for _ in range(v.get('len', 1))]
                elif k == tuple:
                    res['tuple'] = tuple(random.uniform(*v['items'][float]['datarange']) for _ in range(v.get('len', 1)))
                elif k == dict:
                    # 使用 next() 来从生成器中获取第一个结果
                    res['dict'] = {key: next(generate(val)) for key, val in v.get('items', {}).items()}
            else:
                res[k] = v
        yield res  # 使用 yield 而不是一次性返回所有数据


def main():
    struct = {
        'num': 10,  # 生成的样本数量
        int: {"datarange": (0, 100)},
        float: {"datarange": (0, 1.0)},
        str: {"datarange": string.ascii_uppercase, "len": 10},
        list: {
            "len": 3,
            "items": {
                int: {"datarange": (0, 10)}
            }
        },
        tuple: {
            "len": 2,
            "items": {
                float: {"datarange": (0, 1.0)}
            }
        },
        dict: {
            "items": {
                "nested_key": {
                    str: {"datarange": string.ascii_lowercase, "len": 5}
                }
            }
        }
    }

    # 根据结构生成数据
    count = 0
    for sample in generate(struct):
        print(sample)
        count += 1
        if count >= 10:  # 演示时限制输出10个样本
            break


if __name__ == "__main__":
    main()




