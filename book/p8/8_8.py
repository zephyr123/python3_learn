def make_album(name,album_name,songs=''):
    if songs:
        album = {'name':name,'album_name':album_name,'songs':songs}
    else:
        album = {'name':name,'album_name':album_name}
    print(album)

while True:
    print("please enter 'q' anytime,quit")
    name = input("please input singer'name:")
    if name == 'q':
        break
    album_name = input("please input album_name:")
    if album_name == 'q':
        break
    make_album(name,album_name)



