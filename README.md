# 自动发布短视频小工具

## 目前已经开发有快手版，需要其他网站的原理一样。
## 注意第一次运行需要扫码登录,之后cookie会一直保存.

### 发布前需要准备的.

  1. 一台安装好chrome浏览器的电脑.
  2. 准备一个视频文件夹,视频可以按照序号排序.
  3. 准备pycharm开发工具或者其他亦可.注意python3.10版本
  4. 下载必须包,运行即可.
  5. 可以提前登录账号去新建一个合集,这样每次发布就会自动选择这个合集.
  6. 需要提前安装好ffmpeg (安装方法在文末)

### 需要用到的包
``` python
  Pillow==11.0.0
  PySide6
  selenium==4.27.1
```  
* 如果指定的包下载不了,也下载最新版即可. *

### 注意运行完成之后会在当前文件夹新增一张封面图片,在原视频文件夹多一个加了封面的视频,不需要可以自行删除.
### 本程序作为python学习之用途,请不要用于非法用途. 

---

  ### 界面
![image](https://github.com/user-attachments/assets/e2da1f7c-6048-44f8-9917-61714809cf65)

 ### 封面图片示例
![20241226_175158_1](https://github.com/user-attachments/assets/ac8b3cce-19f3-4e23-8a0e-3306446450c1)


ffmpeg官方：https://www.ffmpeg.org/download.html
安装步骤网上很多教程，大家可以自行选择；
推荐步骤：
1. 下载FFmpeg:
  - 访问FFmpeg的官方网站（https://ffmpeg.org/download.html）或使用提供的第三方链接，如gyan.dev或BtbN GitHub Releases，选择适合Windows的预编译版本。推荐选择最新版本，例如6.0或6.1。
  - 根据你的系统架构（32位或64位），下载对应的ZIP文件。
2. 解压文件:
  - 下载完成后，找到ZIP文件并解压到你希望存放FFmpeg的目录，比如C:\Program Files\ffmpeg。
3. 设置环境变量:
  - 进入解压后的目录，找到bin子文件夹，这个文件夹包含了所有可执行文件（如ffmpeg.exe）。
  - 打开Windows设置，搜索“编辑环境变量”或通过控制面板进入“系统”->“高级系统设置”->“环境变量”。
  - 在“用户变量”或“系统变量”中找到“Path”，点击“编辑”。
  - 点击“新建”，然后输入或粘贴解压后bin文件夹的完整路径（例如C:\Program Files\ffmpeg\bin），确保没有引号，并以bin结尾。
  - 点击“确定”保存所有更改。
4. 验证安装:
  - 打开命令提示符（CMD）或Windows Terminal，输入ffmpeg -version。
  - 如果安装成功，系统将显示FFmpeg的版本信息，表明FFmpeg已经正确安装并添加到系统路径中。
