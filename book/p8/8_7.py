def make_album(name,album_name,songs=''):
    if songs:
        album = {'name':name,'album_name':album_name,'songs':songs}
    else:
        album = {'name':name,'album_name':album_name}
    print(album)

make_album('zhoujielun','qinghuaci')
make_album('zhengzhihua','shuishou')
make_album('huajie','guanglang')
make_album('zhengzhihua','xingxingdiandeng','5')