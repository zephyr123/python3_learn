favorite_places = {
    'huyongsheng': ['lushan', 'taishan', 'qinghua'],
    'liyue': ['home', 'shenyang', 'dalian'],
    'zhangshengchao': ['beijing', 'jiangxi', 'xingtai']
}
for k,vs in favorite_places.items():
    print(k + "最喜欢的地方是:")
    for v in vs:
        print(v)