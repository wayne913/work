import os
import re
import sys

def get_screen_size(*args):
    """Get size of window and return the size for swipe function
       args 作为可变参数 表示是否传入设备的ID
    """
    if not args:
        # 如果没有传入指定设备ID，执行以下ADB command，获取设备屏幕分辨率
        size_file = os.popen("adb shell dumpsys window displays").read()
    else:
        # 如果传入指定设备ID，执行以下ADB command，获取设备屏幕分辨率
        uid = args[0]
        size_file = os.popen("adb -s %s shell dumpsys window displays" % uid).read()
    if not size_file:
        # 获取设备分辨率失败
        print("Cannot get the resolution of screen, please check the ADB.")
        sys.exit()
    else:
        # 正则表达式匹配设备分辨率
        size_match = re.search(r"(\d+)x(\d+)", size_file)
        if not size_match:
            # 设备分辨率匹配失败
            print("Failed to match the screen size.")
            sys.exit()
        else:
            # 设备分辨率信息从字符串分割转换为二元元组
            size_screen = re.split(r"x", size_match.group())
            print("屏幕分辨率：", size_screen)
            # 字符串元素元组转换为整型元素列表
            size = [int(size_screen[0]), int(size_screen[1])]
            return size


class Steps:

    def swipe_up(*args, t, n):
        """Swipe device screen up in t milliseconds and repeat the operation n times
           t=100 作为命名关键字参数 表示默认的滑动时间为100ms 可自寻设计滑动时间
           n=1 作为命名关键字参数 表示默认的滑动次数为1次 可自寻设计滑动次数
        """
        size = get_screen_size(*args)
        # print(size)
        # print("up_log")
        x1 = size[0] * 0.5
        y1 = size[1] * 0.6
        x2 = size[0] * 0.5
        y2 = size[1] * 0.25
        print("起点：%.f, %.f\n终点：%.f, %.f" % (x1, y1, x2, y2,))
        for i in range(n):
            print("滑动 " + str(i+1) + " 次")
            if not args:
                os.system("adb shell input swipe %f %f %f %f %d" % (x1, y1, x2, y2, t))
            else:
                uid = args[0]
                os.system("adb -s %s shell input swipe %f %f %f %f %d" % (uid, x1, y1, x2, y2, t))

    def swipe_down(*args, t, n):
        """Swipe device screen down in t milliseconds and repeat the operation n times"""
        size = get_screen_size(*args)
        print(size)
        x1 = size[0] * 0.5
        y1 = size[1] * 0.25
        x2 = size[0] * 0.5
        y2 = size[1] * 0.75
        print("起点：%.f, %.f\n终点：%.f, %.f" % (x1, y1, x2, y2,))
        for i in range(n):
            print("滑动 " + str(i + 1) + " 次")
            if not args:
                os.system("adb shell input swipe %f %f %f %f %d" % (x1, y1, x2, y2, t))
            else:
                uid = args[0]
                os.system("adb -s %s shell input swipe %f %f %f %f %d" % (uid, x1, y1, x2, y2, t))

    def swipe_left(*args, t, n):
        """Swipe device screen left in t milliseconds and repeat the operation n times"""
        size = get_screen_size(*args)
        x1 = size[0] * 0.95
        y1 = size[1] * 0.5
        x2 = size[0] * 0.05
        y2 = size[1] * 0.5
        print("起点：%.f, %.f\n终点：%.f, %.f" % (x1, y1, x2, y2,))
        for i in range(n):
            print("滑动 " + str(i + 1) + " 次")
            if not args:
                os.system("adb shell input swipe %f %f %f %f %d" % (x1, y1, x2, y2, t))
            else:
                uid = args[0]
                os.system("adb -s %s shell input swipe %f %f %f %f %d" % (uid, x1, y1, x2, y2, t))

    def swipe_right(*args, t, n):
        """Swipe device screen right in t milliseconds and repeat the operation n times"""
        size = get_screen_size(*args)
        x1 = size[0] * 0.05
        y1 = size[1] * 0.5
        x2 = size[0] * 0.95
        y2 = size[1] * 0.5
        print("起点：%.f, %.f\n终点：%.f, %.f" % (x1, y1, x2, y2,))
        for i in range(n):
            print("滑动 " + str(i + 1) + " 次")
            if not args:
                os.system("adb shell input swipe %f %f %f %f %d" % (x1, y1, x2, y2, t))
            else:
                uid = args[0]
                os.system("adb -s %s shell input swipe %f %f %f %f %d" % (uid, x1, y1, x2, y2, t))


    def swipe_oblique(*args, t, n):
        """Swipe device screen oblique in t milliseconds and repeat the operation n times"""
        size = get_screen_size(*args)
        x1 = size[0] * 0.05
        y1 = size[1] * 0.75
        x2 = size[0] * 0.95
        y2 = size[1] * 0.25
        print("起点：%.f, %.f\n终点：%.f, %.f" % (x1, y1, x2, y2,))
        for i in range(n):
            print("滑动 " + str(i + 1) + " 次")
            if not args:
                os.system("adb shell input swipe %f %f %f %f %d" % (x1, y1, x2, y2, t))
            else:
                uid = args[0]
                os.system("adb -s %s shell input swipe %f %f %f %f %d" % (uid, x1, y1, x2, y2, t))