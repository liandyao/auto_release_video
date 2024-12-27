import os
import random

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


"""
自动发布抖音和快手2.0版本
author: liandyao
date: @date

"""
# 抖音需要标题

tags=["#跟我学英语",
    "#快乐学英语",
    "#寒假学英语",
    "#英语小达人",
    "#趣味学英语",
    "#每天一句英语",
    "#玩着学英语",
    "#英语启蒙小课堂",
    "#英语开口说",
    "#英语单词魔法书",
    "#亲子学英语",
    "#少儿英语我最棒",
    "#轻松早教学英语",
    "#宝宝爱英语",
    "#英语儿歌欢乐颂",
    "#玩中记单词",
    "#学英语从0开始",
    "#孩子的英语秘密",
    "#暑假学英语",
    "#英语奇妙冒险",
    "#掌握英语没烦恼",
    "#英语故事时间",
    "#小小英语天地",
    "#一起玩转英语",
    "#英语小剧场",
    "#英语启蒙魔法班",
    "#英语有趣学起来",
    "#幼儿英语早教启蒙",
    "#每天和宝宝学英语",
    "#少儿英语酷课堂",
    "#英语学习打卡中",
    "#家庭趣味学英语",
    "#英语新手村",
    "#少儿英语成长记",
    "#孩子的英语启蒙日记",
    "#英语词汇王",
    "#英语小冒险家",
    "#边玩边学英语",
    "#儿童英语趣味营",
    "#英语互动课堂",
    "#学英语从玩拼图开始",
    "#英语阅读童趣时光",
    "#一日一句英语启蒙",
    "#学会英语好轻松",
    "#让孩子爱上英语",
    "#英语快乐成长记",
    "#少儿双语小百科",
    "#英语语感培养屋",
    "#英语学习小能手"]

class AutoRelease:
    def __init__(self, titles,  descris,tags=tags):
        # 初始化参数并将其存储为实例变量
        self.titles = titles  # 文字标题列表
        self.descris = descris  # 描述
        self.tags = tags  # 标签

    # 快手发布
    '''
    video_path 表示视频的路径
    title 表示需要写在封面的标题
    account_en 是账号的英文名称或者数字,不要使用中文
    '''
    def auto_release_kuaishou(self,video_path,title,account_en):
        # 创建 ChromeOptions，并指定 chrome.exe 的路径
        # 获取当前工作目录
        base_dir = os.getcwd()

        # 指定一个新的用户数据目录
        new_user_data_directory = os.path.join(base_dir, f"User_Data_ks_{account_en}")
        if not os.path.exists(new_user_data_directory):
            os.makedirs(new_user_data_directory)

        # 创建 ChromeOptions
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={new_user_data_directory}")  # 使用新的用户数据目录
        options.add_argument("profile-directory=Default")
        options.add_argument("--start-maximized")  # 最大化窗口

        # 启动 Chrome
        driver = webdriver.Chrome(options=options)

        try:
            driver.get("https://cp.kuaishou.com/article/publish/video")
        except Exception as e:
            print(f"Failed to load page: {e}")

        print('开始上传视频.')
        # 视频上传
        file_input = WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))

        file_input.send_keys(video_path)
        print('上传完成')

        time.sleep(3)

        # 等待第三个按钮出现  -- 第三个是合集
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "(//div[contains(@class, 'ant-select ant-select-single ant-select-allow-clear ant-select-show-arrow')])[4]")
            )
        )

        print("找到按钮，准备点击。")

        # 点击按钮
        button.click()
        print("合集按钮已被点击。")

        time.sleep(3)
        # 等待并找到第一个具有 ant-select-item-option 类的 div 元素
        first_item = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.ant-select-item-option"))
        )

        # 点击该元素
        first_item.click()
        print("已点击活跃选项。")

        random_title=''
        # 随机选择一个标题
        if len(self.titles) > 0:
            random_title = random.choice(self.titles)
        print(random_title)
        time.sleep(3)
        descri = random.choice(self.descris)
        # 填写描述
        title_input = WebDriverWait(driver, 150).until(
            EC.element_to_be_clickable((By.ID, "work-description-edit")))
        title_input.send_keys(f"{title} {random_title} {descri} ")
        # 每次加三个标签
        title_input.send_keys(f"{random.choice(self.tags).replace('抖音','快手')} ")
        time.sleep(2)
        title_input.send_keys(f"{random.choice(self.tags).replace('抖音','快手')} ")
        time.sleep(1)
        title_input.send_keys(f"{random.choice(self.tags).replace('抖音','快手')} ")

        # 等待直到特定类名的元素出现-当有预览按钮时,说明上传成功
        preview_header = WebDriverWait(driver, 240).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_preview-header_1ahzu_92"))
        )
        print("找到元素，继续执行下一步。")

        # 发布
        time.sleep(3)
        # 等待并找到具有特定类名并包含"发布"文本的 div 元素
        publish_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[contains(@class, '_button_si04s_1') and contains(@class, '_button-primary_si04s_60')]//div[text()='发布']"))
        )

        # 点击该元素
        publish_button.click()

        print("已点击发布按钮。")

        # 等待 10 秒
        time.sleep(10)


        driver.quit()  # 确保在完成后关闭浏览器


    def auto_release_douyin(self,video_path,title,account_en):

        # 创建 ChromeOptions，并指定 chrome.exe 的路径
        # 获取当前工作目录
        base_dir = os.getcwd()

        # 指定一个新的用户数据目录
        new_user_data_directory = os.path.join(base_dir, f"User_Data_dy_{account_en}")
        if not os.path.exists(new_user_data_directory):
            os.makedirs(new_user_data_directory)

        # 创建 ChromeOptions
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={new_user_data_directory}")  # 使用新的用户数据目录
        options.add_argument("profile-directory=Default")
        options.add_argument("--start-maximized")  # 最大化窗口

        # 启动 Chrome
        driver = webdriver.Chrome(options=options)

        '''
             作用：发布抖音视频
            '''

        # 进入创作者页面，并上传视频
        driver.get("https://creator.douyin.com/creator-micro/content/upload")
        time.sleep(3)
        # 视频上传
        file_input = WebDriverWait(driver, 600).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))

        file_input.send_keys(video_path)
        print('上传完成')

        time.sleep(10)

        # 等待输入框加载并获取元素
        input_element = WebDriverWait(driver, 600).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@class='semi-input semi-input-default' and @type='text']"))
        )


        # 随机选择一个标题
        random_title = random.choice(self.titles)
        print(random_title)

        input_element.send_keys(f"{title} ")  # 替换为你要设置的文本
        input_element.send_keys(f'{random_title}')
        time.sleep(2)
        # 等待加载 input 元素  标题
        input_element2 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'editor-kit-container'))
        )
        time.sleep(2)
        # 随机选择一个标题
        random_desc = random.choice(self.descris)
        print(random_desc)


        # 设置文本
        input_element2.send_keys(f"{random_desc} ")  # 替换为你要设置的文本
        input_element2.send_keys(f"{random.choice(self.tags)} ")
        input_element2.send_keys(f"{random.choice(self.tags)} ")
        input_element2.send_keys(f"{random.choice(self.tags)} ")

        time.sleep(2)

        # 加入活动标识
        try:
            # 等待目标类似结构的 div 元素及其包含“动画”文本的下级 div 加载
            target_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//div[contains(@class, 'container-BPqaWp activity-right-N1pBMo')]//div[descendant::text()[contains(., '动画')]]"
                    )
                )
            )

            # 点击该元素
            target_element.click()
            time.sleep(2)
        except Exception as e:
            print(f"没有相关活动：{e}")

        try:
            # 加入合集
            # 等待并点击第一个下拉框的 div
            select_div = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, "semi-select.select-collection-nkL6sA")
                )
            )
            select_div.click()  # 点击下拉选择框

            time.sleep(1)
            # 等待下拉选项出现，并找到第一个选项并点击
            first_option = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[contains(@class, 'semi-select-option collection-option')]")
                )
            )
            first_option.click()  # 点击第一个选项

            time.sleep(2)
        except Exception as e:
            print(f"没有相关活动：{e}")

        # 等待并检查是否存在包含"重新上传"文本的 div
        upload_div = WebDriverWait(driver, 180).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(), '重新上传')]")  # 使用 XPath 来查找包含文本的 div
            )
        )

        # 如果找到了 upload_div，则输出成功信息
        print("上传成功！可以点击发布按钮。")

        # 滚动到底部
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)  # 等待滚动完成


        publish_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "//button[contains(@class, 'primary-cECiOJ')]")
            )
        )



        # 点击发布按钮
        publish_button.click()

        print("已点击发布按钮。")

        # 等待 10 秒
        time.sleep(10)

        driver.quit()  # 确保在完成后关闭浏览器


