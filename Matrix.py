from dataclasses import dataclass
from typing import List, Dict, Any

import time


@dataclass
class Matrix():
    # __init(self, ...)
    data: List[List]

    # 定義自訂Type
    Row = Dict[Any, Dict]

    def __post_init__(self):
        self.header: list = self.data[0]
        self.body: List[list] = self.data[1:]

    @property
    def dataframe(self) -> Dict[Any, Dict]:
        dataframe = {}
        for index, row in enumerate(self.__dict__()):
            dataframe[index] = row

        return dataframe

    def __dict__(self,) -> List[Dict[str, str]]:
        return [dict(zip(self.header, data)) for data in self.body]

    def reset_index(self, key, drop=False) -> Dict[Any, Row]:
        assert key in self.header, f"index: '{key}' not exists in header"

        reset_index_dataframe: Dict = {}
        if drop:
            for _, row in self.dataframe.items():
                new_key = row[key]
                del row[key]

                reset_index_dataframe[new_key] = row
        else:
            for _, row in self.dataframe.items():
                reset_index_dataframe[row[key]] = row

        return reset_index_dataframe


if __name__ == '__main__':
    def now(): return time.time()

    start = now()
    students = Matrix(
        [
            ["name", "age", "gender"],
            ["Ann", "18", "Female"],
            ["Eric", "20", "Male"],
        ],
    )

    # print(students.data)
    # print(students.header)
    # print(students.body)
    # print(students.dataframe)
    # print("############################")
    print(students.reset_index("name", drop=True))
    print((now() - start) * 1000)
