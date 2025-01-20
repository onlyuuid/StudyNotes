"""
 OS文件/目录方法
 os模块提供了丰富的方法用来处理文件和目录. 常用的方法如下表所示:
 方法                                 描述
文件和目录操作：
os.mkdir(path)：创建一个目录。
os.makedirs(name)：递归地创建目录。
os.rmdir(path)：删除一个空目录。
os.removedirs(name)：递归地删除空目录。
os.listdir(path='.')：列出指定目录的内容。
os.remove(path)：删除一个文件。
os.rename(src, dst)：重命名文件或目录。
路径操作：
os.path.join()：智能地连接两个或更多的路径部分。
os.path.split(path)：将路径分割成一对 (head, tail)。
os.path.dirname(path)：返回路径中的目录名。
os.path.basename(path)：返回路径中的基础名（即文件名）。
os.path.exists(path)：如果路径存在则返回True。
os.path.isfile(path) 和 os.path.isdir(path)：检查路径是否为文件或目录。
环境变量：
os.environ：获取系统环境变量的映射对象。
os.getenv(key, default=None)：获取环境变量的值。
进程管理：
os.system(command)：执行shell命令。
os.popen(cmd, mode='r', buffering=-1)：打开一个管道到或从命令。
os.kill(pid, sig)：发送信号给进程。
os.startfile(path)：启动关联程序打开文件（仅限Windows）。
其他功能：
os.getpid()：获取当前进程ID。
os.urandom(n)：返回n个安全的随机字节。
"""

