def show_magicians(names):
    for name in names:
        print(name)

def make_great(names):
    while names:
        curr_names = "the Great " + names.pop()
        mod_names.append(curr_names)

magic_names = ['liuqian','zhuxun','dongqing']
mod_names = []
make_great(magic_names[:])
show_magicians(mod_names)
show_magicians(magic_names)