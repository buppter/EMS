def num_to_gender(num: int) -> str:
    gender_dic = {0: "女", 1: "男", 2: "未知"}
    return gender_dic.get(num, "未知")


def gender_to_num(gender: str) -> int:
    gender_dic = {"男": 1, "女": 0}
    num = gender_dic.get(gender, 2)
    return num
