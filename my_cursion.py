import random
import string

def generate(kwargs):
    result = []
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
                    # Fixed the nested structure issue here
                    res['list'] = [random.randint(*v['items'][int]['datarange']) for _ in range(v.get('len', 1))]
                elif k == tuple:
                    # Fixed the tuple generation issue here
                    res['tuple'] = tuple(random.uniform(*v['items'][float]['datarange']) for _ in range(v.get('len', 1)))
                elif k == dict:
                    # Fixed the dict generation issue here
                    res['dict'] = {key: generate(val)[0] for key, val in v.get('items', {}).items()}
            else:
                res[k] = v
        result.append(res)
    return result


def main():
    struct = {
        'num': 2,  # Number of generated sets
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

    # Generate data based on the structure
    for sample in generate(struct):
        print(sample)


main()


