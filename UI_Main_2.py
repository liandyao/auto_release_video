# -*- coding:utf-8 -*-
"""

@author: liandyao
@date: 2024/12/26 11:58
"""
import json
import os
import re
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui.ar_ui2 import Ui_Form  # 导入自动生成的 UI 类
import add_video_cover
from web_auto_relase2_0 import AutoRelease

ks_account = './account.json'
JSON_FILE = './content.json'


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 创建 UI 对象
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # 设置 UI
        self.setWindowTitle('自动发布短视频V1.0')
        # 打开文件夹
        self.ui.toolButton_file_select.clicked.connect(self.open_dir_video)

        # 连接按钮点击事件
        self.ui.pushButton_release.clicked.connect(self.release_video)
        self.ui.comboBox_account.setEditable(True)  # 设置为可编辑
        self.comboBox = self.ui.comboBox_account

        # 加载账号数据
        self.load_data()

        # 连接文本变化事件
        self.ui.pushButton_add_ks.clicked.connect(self.add_to_combobox_ks)

        self.titles=[] # 快手不需要标题
        self.tags =[]
        self.descris =[]


        self.initText()

        # 最后一次打开的文件夹
        self.last_folder = self.load_last_folder()

        # 加载自动发布工具
        self.auto = AutoRelease(titles=self.titles,descris=self.descris,tags=self.tags)

    def add_to_combobox_ks(self):
        text = self.ui.comboBox_account.currentText()
        print('输入的文本是',text)
        # 获取输入文本
        if text and text not in [self.comboBox.itemText(i) for i in range(self.comboBox.count())]:
            # 添加到下拉框中
            self.comboBox.addItem(text)
            # 保存到文件
            self.save_data()

    def save_data(self):
        # 获取下拉框中的所有项
        items = [self.comboBox.itemText(i) for i in range(self.comboBox.count())]

        self.save_last_folder('account_ks', items)

    def load_data(self):
        # 如果文件存在，加载数据
        if os.path.exists(ks_account):
            with open(ks_account, 'r',encoding='utf-8') as f:
                accounts_data = json.load(f)
                items = accounts_data.get('account_ks', [])  # 获取账户列表
                for item in items:
                    self.comboBox.addItem(item)  # 添加到下拉框中

                    # 初始化文本等内容
    def initText(self):

        '''
        self.ui.plainTextEdit_tags 和 self.ui.plainTextEdit_descris 是两个文本框，每次需要从content.json中获取标签和文案

        content.json的格式为:
        {
            "tags:["a","b","c","d","e","f"],
            "descris":["a","b","c"]
        }
        当界面有修改时,需要从界面保存到json文件中,下次再读取出来,请为实现代码

        '''
        self.load_content_from_json()
        # 为两个文本框的内容变化连接信号函数
        self.ui.plainTextEdit_tags.textChanged.connect(self.update_json)
        self.ui.plainTextEdit_descris.textChanged.connect(self.update_json)

        # 从self.ui.plainTextEdit_tags中获取所有的标签,注意标签是换行符分割的,放入到self.tags中
        # 从 plainTextEdit 获取文本
        text = self.ui.plainTextEdit_tags.toPlainText()  # 获取文本区域的内容
        # 用换行符分割并去掉空白标签
        self.tags = [tag.strip() for tag in text.splitlines() if tag.strip()]
        # 从self.ui.plainTextEdit_descris中获取所有的文案,注意每一条文案都是使用$$开始和$$结尾的,解析之后放入到self.descris中
        # 输出获取的标签列表
        print("获取的标签:", self.tags)


        # 从 plainTextEdit 获取文本
        text = self.ui.plainTextEdit_descris.toPlainText()  # 获取文本区域的内容

        # 使用正则表达式查找所有 $$ 开头和 $$ 结尾的文案
        self.descris = re.findall(r'\$\$(.*?)\$\$', text)  # 非贪婪模式匹配

        # 去除文案前后的空白字符
        self.descris = [descr.strip() for descr in self.descris]

        # 输出获取的文案列表
        print("获取的文案:", self.descris)

    def load_content_from_json(self):
        """从content.json加载内容，并填入到两个文本框"""
        try:
            with open(JSON_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)

                # 加载 `tags`，换行分隔
                tags = "\n".join(data.get("tags", []))
                self.ui.plainTextEdit_tags.setPlainText(tags)

                # 加载 `descris`，合并为 $$...$$ 格式的字符串
                descris_list = data.get("descris", [])
                descris = "\n".join([f"$$ {item} $$" for item in descris_list])  # 格式化为 $$...$$
                self.ui.plainTextEdit_descris.setPlainText(descris)
        except FileNotFoundError:
            # 如果 JSON 文件不存在，初始化两个文本框为空
            self.ui.plainTextEdit_tags.setPlainText("")
            self.ui.plainTextEdit_descris.setPlainText("")
        except json.JSONDecodeError as e:
            print(f"JSON文件读取错误: {e}")
            self.ui.plainTextEdit_tags.setPlainText("")
            self.ui.plainTextEdit_descris.setPlainText("")

    def update_json(self):
        """从两个文本框获取内容并更新到JSON文件"""

        # 获取 `tags`，按行分割为列表
        tags = self.ui.plainTextEdit_tags.toPlainText().strip().splitlines()
        print("更新获取的标签:", tags)
        # 获取 `descris`，从文本框内容依次提取 `$$...$$` 的中间部分
        descris_text = self.ui.plainTextEdit_descris.toPlainText().strip()
        descris = [item.strip() for item in descris_text.split("$$") if item.strip()]  # 提取非空内容

        # 准备保存内容
        data = {
            "tags": tags,
            "descris": descris
        }

        # 将内容写入 JSON 文件
        try:
            with open(JSON_FILE, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"写入 JSON 文件失败: {e}")

            # 打开文件夹
    def load_last_folder(self):
        """加载上次打开的文件夹路径"""
        try:
            with open(ks_account, 'r',encoding='utf-8') as f:
                data = json.load(f)
                return data.get('last_folder', '')  # 返回上次文件夹路径
        except (FileNotFoundError, json.JSONDecodeError):
            return ''  # 如果文件不存在或不可解析，返回空字符串

    def open_dir_video(self):
        # 显示文件夹选择对话框
        folder = QFileDialog.getExistingDirectory(self, "选择视频文件夹", self.last_folder)

        if folder:  # 检查是否选择了文件夹
            print("打开文件夹:", folder)
            # 清空当前下拉框中的内容
            self.ui.comboBox_file.clear()

            # 保存当前选择的文件夹路径
            self.save_last_folder('last_folder',folder)

            # 遍历文件夹中的所有文件
            for filename in os.listdir(folder):
                if filename.endswith('.mp4'):  # 只选取 .mp4 文件
                    file_path = os.path.join(folder, filename)  # 获取完整路径
                    self.ui.comboBox_file.addItem(file_path)  # 将文件路径添加到下拉框中

    def save_last_folder(self, key, datas):
        """保存上次打开的文件夹路径"""
        try:
            # 读取现有数据
            with open(ks_account, 'r',encoding='utf-8') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # 如果文件不存在或为空，则初始化为空字典
            data = {}

        # 更新 last_folder
        data[key] = datas

        # 写回文件
        with open(ks_account, 'w',encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


    # 发布视频事件
    def release_video(self):
        self.title = self.ui.lineEdit_title.text()
        print('开始发布')
        # 获取被选择的路径
        selected_path = self.ui.comboBox_file.currentText()  # 获取当前选中的文件路径
        if selected_path:
            print("选中的文件路径:", selected_path)  # 输出选中的路径

            # 加入封面
            new_path = add_video_cover.start(selected_path,self.title)

            self.auto.auto_release_kuaishou(new_path,self.title,self.ui.comboBox_account.currentText())
        else:
            print("没有选择任何文件")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())