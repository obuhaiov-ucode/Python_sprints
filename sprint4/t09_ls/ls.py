import re
import sys
import os
import stat
import pwd
import grp
import datetime
from stat import *
from printy import printy

def walktree(dir, callback, flag=None):
    dirs = []
    items = {}
    all_items = sorted(list(os.listdir(dir)))
    for f in all_items:
        pathname = os.path.join(dir, f)
        mode = os.lstat(pathname).st_mode
        if S_ISDIR(mode) and not re.match(r"(\.|\.\.|^\.)", f):
            dirs.append(pathname)
            items.update({pathname: f})
        elif not re.match(r"(\.|\.\.|^\.)", f):
            items.update({pathname: f})
    callback(dir, items, flag)
    if flag and re.match(r"^-(lR|Rl|R)$", flag):
        for dir in dirs:
            printy('')
            walktree(dir, callback, flag)

def printer(dir, files, flag):
    if flag and re.match(r"^-(lR|Rl|R)$", flag):
        printy(dir, end=':\n')
    if not flag or re.match(r"^-R$", flag):
        line_len = 0
        for key, value in files.items():
            if line_len + len(value) > 79:
                line_len = 0
                printy('')
            if S_ISDIR(os.lstat(key).st_mode):
                printy(f'[b>B]{value}@', end='')
            else:
                printy(value, end='')
            line_len += len(value)
            if list(files.keys())[-1] != key:
                line_len += 1
                printy(' ', end='')
        printy('')
    elif re.match(r"^-(lR|Rl|l)$", flag):
        for key, value in files.items():
            printy(f'{stat.filemode(os.stat(key).st_mode)}', end=' ')
            printy(f'{pwd.getpwuid(os.stat(key).st_uid).pw_name}', end=' ')
            printy(f'{grp.getgrgid(os.stat(key).st_gid).gr_name}', end=' ')
            printy(f'{os.stat(key).st_size}', end=' ')
            t = datetime.datetime.fromtimestamp(os.stat(key).st_mtime)
            printy(f'{t.strftime("%b %d %H:%M")}')
            if S_ISDIR(os.lstat(key).st_mode):
                printy(f'[b>B]{value}@')
            else:
                printy(value)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        walktree('.', printer)
    elif len(sys.argv) == 2 and re.match(r"^-(lR|Rl|R|l)$", sys.argv[1]):
        walktree('.', printer, sys.argv[1])
    elif len(sys.argv) == 2:
        walktree(sys.argv[1], printer)
    elif len(sys.argv) == 3 and re.match(r"^-(lR|Rl|R|l)$", sys.argv[2]):
        walktree(sys.argv[1], printer, sys.argv[2])
