level=6
#上面输入汉诺塔的层数
#a为最左边，b为中间，c为右边
#输出每一行为1个移动步骤
#使用 递归 进行运算
def hnt(first,middle,last,level):
    if level == 1:
        print(first+"-"+last)
    else:
        a = level-1
        hnt(first,last,middle,a)
        print(first+"-"+last)
        hnt(middle,first,last,a)
print("开始移动"+str(level)+"层汉诺塔")
hnt("a","b","c",level)
print(str(level)+"层汉诺塔移动完成")