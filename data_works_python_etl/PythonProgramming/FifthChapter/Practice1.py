# 字符串格式化可以用来简化dateconvert2.py 程序（该程序在本章示例代码中，可下
# 载获得）。用字符串格式化方法重写该程序。

def main():
    # get the date
    dateStr = input("Enter a date (mm/dd/yyyy): ")
    # split into components
    monthStr, dayStr, yearStr = dateStr.split("/")
    # convert monthStr to the month name
    months = ["January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"]
    monthStr = months[int(monthStr)-1]
    # output result in month day, year format
    print("The converted date is:{0}{1},{2}".format(monthStr,dayStr,yearStr))
if __name__ == '__main__':
    main()