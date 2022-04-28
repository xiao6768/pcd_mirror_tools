# coding=utf-8
from sys import argv  # 导入模块
import pypcd



# 如果执行的方式错误输出使用方法
USAGE = '''
用法错误，正确方式如下：
python pcd_mirror_tools.py x y input_pcd 
x,y center_coordinate
e.g.  python pcd_recenter_tools.py '98.7' '199.6' ../Town01.pcd 
'''

print(len(argv))

if len(argv) != 4:  # 判断argv的长度，如果脚本被直接执行(argv的值为当前脚本的路径)，如果执行命令是python demo.py 加两个参数(argv的长度就为3(以此类推))
    print(USAGE)  # 如果传入的参数不足，输出正确用法
    exit(1) # 异常退出(下面的代码将不会被执行)

script_name, x, y, input_file = argv  # 将传入的参数赋值进行使用



# also can read from file handles.
pc = pypcd.PointCloud.from_path(input_file)
# pc.pc_data has the data as a structured array
# pc.fields, pc.count, etc have the metadata

# center the x,y field
invert_x = 0 - float(x)
invert_y = 0 - float(y)


pc.pc_data['x'] = invert_x + pc.pc_data['x']
pc.pc_data['y'] = invert_y + pc.pc_data['y']


output_file = input_file + '_' + str(x) + '_' + str(y) + '.pcd'
# save as binary compressed
pc.save_pcd(output_file, compression='binary_compressed')