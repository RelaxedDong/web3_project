# IPFS
IPFS(InterPlanetary File System，星际文件系统），它是一种全新的超媒体文本传输协议，可以把它理解为一种支持分布式存储的网站

参考资料: [ipfs PPT.pdf](ipfsPPT.pdf) 
来源：[B站视频分享](https://www.bilibili.com/video/BV1fL4y187mS?from=search&seid=16590021780953099369&spm_id_from=333.337.0.0)

# IPNS 如何处理目录CID变动？
```bash

# 1. 生成ipns ID
[root@iZt4na58hlqlij2bd6il00Z ~]# ipfs key gen --type=rsa --size=2048 bca_test_3
k2k4r8jvi71mdlgcz5z22i991zodwxen2xg5ogs8uxqwue9hx641fhrk

# 2. 上传一个文件夹，然后使用
[root@iZt4na58hlqlij2bd6il00Z ~]# ipfs add -r test | tail -n 1
added QmZPRAujYM4FjwLoxEkMWNTxR6L5VfkWGuvMJwSKHEgm3Q test

[root@iZt4na58hlqlij2bd6il00Z ~]# ipfs name publish --key=bca_test_3  QmZPRAujYM4FjwLoxEkMWNTxR6L5VfkWGuvMJwSKHEgm3Q
Published to k2k4r8jvi71mdlgcz5z22i991zodwxen2xg5ogs8uxqwue9hx641fhrk: /ipfs/QmZPRAujYM4FjwLoxEkMWNTxR6L5VfkWGuvMJwSKHEgm3Q

# 3. 修改文件夹，再次使用上传一个文件到文件后，再次上传
[root@iZt4na58hlqlij2bd6il00Z test]# echo "donghao" >> hello2.text
[root@iZt4na58hlqlij2bd6il00Z ~]# ipfs add -r test | tail -n 1
 32 B / 32 B [===============================================================================================================] 100.00%
 added QmRucJWpykcn85HkvPMNXU6qxroLVzTqRWjvemBfqcfXTc test
# 4.增加绑定
[root@iZt4na58hlqlij2bd6il00Z ~]# ipfs name publish --key=bca_test_3 QmRucJWpykcn85HkvPMNXU6qxroLVzTqRWjvemBfqcfXTc
Published to k2k4r8jvi71mdlgcz5z22i991zodwxen2xg5ogs8uxqwue9hx641fhrk: /ipfs/QmRucJWpykcn85HkvPMNXU6qxroLVzTqRWjvemBfqcfXTc
```
# Pinning Service
```bash
# 添加pinata pinning-service:
	ipfs pin remote service add pinata https://api.pinata.cloud/psa xxx(your tk)
	[root@iZt4na58hlqlij2bd6il00Z ~]# ipfs pin remote service ls
	Pinata https://api.pinata.cloud/psa
	[root@iZt4na58hlqlij2bd6il00Z ~]# echo "hello world" > hello.text
	[root@iZt4na58hlqlij2bd6il00Z ~]# ls
	hello.text
	[root@iZt4na58hlqlij2bd6il00Z ~]# ipfs add hello.text
	added QmT78zSuBmuS4z925WZfrqQ1qHaJ56DQaTfyMUF7F8ff5o hello.text
	 12 B / 12 B [===============================================================================================================] 100.00%

[root@iZt4na58hlqlij2bd6il00Z ~]# ipfs cat QmT78zSuBmuS4z925WZfrqQ1qHaJ56DQaTfyMUF7F8ff5o
	hello world
	[root@iZt4na58hlqlij2bd6il00Z ~]# ipfs pin remote service ls
	Pinata https://api.pinata.cloud/psa

	[root@iZt4na58hlqlij2bd6il00Z ~]# ipfs pin remote add --service=Pinata  --name=hello.text QmT78zSuBmuS4z925WZfrqQ1qHaJ56DQaTfyMUF7F8ff5o
	CID:    QmT78zSuBmuS4z925WZfrqQ1qHaJ56DQaTfyMUF7F8ff5o
	Name:   hello.text
	Status: pinned
```