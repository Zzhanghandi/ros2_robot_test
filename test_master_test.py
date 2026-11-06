import pytest
# 这是一个列表，里面装了要测试的4个数据
test_cases = [10, 80, 50, 0]
#这行代码是要告诉pytest，把test_cases 里面的数字挨个塞进battery_level里面
@pytest.mark.parametrize("battery_level",test_cases)
def test_battery_safety(battery_level):
    print(f"\n当前正在测试电量：{battery_level}%")
    if battery_level < 20:
        print("警告电量过低")
        assert battery_level < 0
    else:
        print("电量充足")
        assert battery_level >= 20   