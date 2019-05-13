prom = {
    'shell': '一种linux脚本',
    'nginx': '一种web服务',
    'mysql': '一种数据库'
}
prom['redis'] = '一种缓存'
prom ['tomcat'] = 'java的web'
for k,v in prom.items():
    print(k + "意思是: " + v)
