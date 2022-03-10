#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json
from random import choices, getrandbits, randint

import numpy as np
from faker import Faker
from tqdm import tqdm

leters = np.array([chr(c) for c in range(ord("a"), ord("z") + 1)])


def random_string(size: int) -> str:
    result = "".join(np.random.choice(leters, size=size // 2))
    if bool(getrandbits(1)):
        result += "#"
    result += "".join(np.random.choice(leters, size=size // 2))
    return result


def main() -> None:
    fake = Faker("en_US")
    items = []
    size = 1_000_000
    ages = np.random.randint(15, 81, size)
    for ind in tqdm(range(size)):
        items.append(
            {
                "age": int(ages[ind]),
                "full_name": fake.name(),
                "text": random_string(100),
            }
        )
    with open("random.json", "w") as f:
        json.dump(items, f)


if __name__ == "__main__":
    main()

