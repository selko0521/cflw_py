﻿import ipaddress
import cflw网络连接 as 连接
import cflw网络连接_串口 as 串口
import cflw网络地址 as 地址
import cflw网络设备 as 设备
import cflw网络设备_思科 as 思科
import cflw网络设备_华为 as 华为
import cflw网络设备_华三 as 华三
def main():
	print("开始")
	# v连接 = 连接.C空连接()
	# v连接 = 连接.C网络终端("gns3.localhost", 5000)
	# v设备 = 思科.f创建设备(v连接, 思科.E型号.c7200, 15.2)
	# v连接 = 连接.C网络终端("ensp.localhost", 2000)
	# v设备 = 华为.f创建设备(v连接, 华为.E型号.s3700, 5.11)
	v连接 = 串口.C串口("com1")
	v设备 = 华三.f创建设备(v连接, 华三.E型号.s3100, 5.20)
	#v设备.f自动适应延迟()
	v设备.fs回显(True)
	#for i in range(5):
	#	v设备.f输入(int(32).to_bytes(1, "big").decode())
	v用户模式 = v设备.f模式_用户()
	# try:	#测试异常
	# 	v用户模式.f执行当前模式命令("asdf")
	# except 设备.X命令 as e:
	# 	print("捕获异常")
	v用户模式.f显示_时间()
	v全局配置 = v用户模式.f模式_全局配置()
	# v接口配置 = v全局配置.f模式_接口配置("f0/0")
	v接口配置 = v全局配置.f模式_接口配置("v33")
	v接口配置.fs网络地址4("12.0.0.1/24")

	#用户
	# v用户配置 = v全局配置.f模式_用户配置("asdf")
	# v用户配置.fs密码("123456")

	#登陆
	# v登陆配置 = v全局配置.f模式_登陆配置(设备.E登陆方式.e虚拟终端)
	# v登陆配置.fs认证方式(设备.E登陆认证方式.e账号)

	#ospf
	# v路由配置 = v全局配置.f模式_开放最短路径优先(1)
	# v区域 = v路由配置.f模式_区域(0)
	# v区域.f通告网络("123.0.0.0/24")
	# v区域.f通告接口(v接口配置)

	#acl
	# v访问列表助手 = v设备.f助手_访问控制列表()
	# v访问列表 = v全局配置.f模式_访问控制列表(v访问列表助手.f计算序号_扩展4(0), 设备.E访问控制列表类型.ipv4扩展)
	# v访问列表.f添加规则(3, 设备.C访问控制列表规则(a允许 = False, a协议 = 设备.C访问控制列表规则.E协议.tcp, a源地址 = ipaddress.IPv4Network("1.2.3.4/24", False), a源端口 = 设备.S访问控制列表端口号.fc等于(123), a目的端口 = 设备.S访问控制列表端口号.fc大于等于(100)))
	# v时间范围 = v全局配置.f模式_时间范围("aaa")
	# v时间范围.f删除(设备.S时间范围.fc定期(设备.E日子.e每天, (0,1), (23,59)))
	# v时间范围.f删除(设备.S时间范围.fc绝对((2018,1,1,0,1), (2018,12,31,23,59)))

	#bgp1
	# v路由配置 = v全局配置.f模式_边界网关协议(65000)
	# v地址簇 = v路由配置.f模式_地址簇(设备.E边界网关协议地址地址簇.e单播4)
	# v对等体 = v地址簇.f模式_对等体("12.0.0.2")
	# v对等体.fs远端自治系统号(65000)

	#bgp2
	# v连接1 = 连接.C网络终端("gns3.localhost", 5001)
	# v设备1 = 思科.f创建设备(v连接, 思科.E型号.c7200, 15.2)
	# v设备1.fs回显(True)
	# v用户模式1 = v设备1.f模式_用户()
	# v全局配置1 = v用户模式1.f模式_全局配置()
	# v接口配置1 = v全局配置1.f模式_接口配置("f0/0")
	# v接口配置1.fs网络地址("12.0.0.2/24")

	#dhcp
	# v自动地址 = v全局配置.f模式_动态主机配置协议()
	# v自动地址.f开关(True)
	# v自动地址池 = v全局配置.f模式_动态主机配置协议地址池("a")
	# v自动地址池.fs网络范围("192.168.0.0/24")
	# v自动地址池.fs默认网关("192.168.0.1")

	#前缀列表
	# v前缀列表 = v全局配置.f模式_前缀列表("a", 设备.E前缀列表类型.e版本4)
	# v前缀列表规则 = 设备.C前缀列表规则(a网络号 = 地址.S网络地址4.fc自动("192.168.1.0/24"))
	# v前缀列表.f添加规则(10, v前缀列表规则)
	# v前缀列表.f删除规则(10)

	#钥匙链
	# v钥匙链 = v全局配置.f模式_钥匙链("keychain")
	# v钥匙 = v钥匙链.f模式_钥匙(1)
	# v钥匙.fs密码("12341234")

	#结束
	# v用户模式.f显示_时间()
	print("结束")
if __name__ == "__main__":
	main()