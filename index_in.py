# _*_coding : utf-8 _*_
# @Time     : 2020/8/28 10:12
# @FileName : 钉钉填报.py
# @Editor   : dml19
# @Software : PyCharm
import os
import time
import sys
import requests
from configparser import ConfigParser

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Server酱推送提醒，需要填写sckey，官网：https://s$
SCKEY = "SCU64015T063d0c6d922270500cd857c8c6d2cf525da073ba8e3e5"

# SERVER酱微信推送url
scurl = f"https://sc.ftqq.com/{SCKEY}.send"


class HealthReport:
    def __init__(self, headless=True, picture=False, size_x="720", size_y="1280"):

        self.desp = ""

        self.options = webdriver.ChromeOptions()
        self.headless = headless
        self.picture = picture
        self.size_x = size_x
        self.size_y = size_y

        self.journey = []
        self.student_id = ""
        self.secret_code = ""
        self.breakfast = ""
        self.lunch = ""
        self.dinner = ""

        options = self.set_options()
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)

        self.address_dic = {
            "行政楼": 0,
            "国交中心": 1,
            "资讯楼": 2,
            "一号实训楼": 3,
            "二号实训楼": 4,
            "一号教学楼": 5,
            "二号教学楼": 6,
            "三号教学楼": 7,
            "教学工厂": 8,
            "科技园C1楼": 9,
            "科技园C2楼": 10,
            "宿舍1-10栋": 11,
            "宿舍11-20栋": 12,
            "北苑公寓": 13,
            "一食堂": 14,
            "二食堂": 15,
            "体育馆": 16,
            "操场": 17,
            "图书馆": 18,
            "商业街": 19,
            "文澜宾馆": 20,
            "篮球场": 21,
        }

    def start(self):
        mark_of_success = False
        self.config_read()
        if mark_of_success := self.login():
            if mark_of_success := self.open_form():
                if mark_of_success := self.fill_in():
                    if mark_of_success := self.submit():
                        self.quit()

        if mark_of_success:
            print("Succeed\n")
            self.desp += "Succeed\n"

        else:
            print("Failed\n")
            self.desp += "Failed\n"
        self.pushWechat()

    def set_options(self):

        # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        # self.options.add_argument('--headlesss')
        self.options.headless = self.headless
        if self.options.headless:
            self.options.add_argument("--disable-gpu")

        # 不加载图片, 提升速度
        if not self.picture:
            self.options.add_argument("blink-settings=imagesEnabled=false")

        # 以最高权限运行
        self.options.add_argument("--no-sandbox")

        # 设置大小
        # self.options.add_argument(f"window-size={self.size_x},{self.size_y}")

        # 设置浏览器执行文件位置
        if len(sys.argv) > 1:
            self.options.binary_location = sys.argv[1]

        # self.options.binary_location('D:\\PycharmProjects\\health_report\\dist\\Chrome-bin\\chrome.exe')

        # 设置开发者模式启动，该模式下webdriver属性为正常值
        # self.options.add_experimental_option(
        #     "excludeSwitches", ["enable-automation"])

        mobile_emulation = {
            "deviceMetrics": {"width": 720, "height": 1280, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Linux; Android 10; MI 9 Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.21 SP-engine/2.17.0 baiduboxapp/11.21.0.10 (Baidu; P1 10) NABar/1.0",
        }
        self.options.add_experimental_option("mobileEmulation", mobile_emulation)
        return self.options

    def config_read(self, filename="./config.ini"):
        try:
            # 读取配置
            config = ConfigParser()
            config.read(filename, encoding="UTF-8")

            # 账户信息读取
            self.student_id = config["账户"]["用户名"]
            self.secret_code = config["账户"]["密码"]

            # 行程读取
            self.journey.append(
                {"地点": config["行程"]["上午地点"], "时间": config["行程"]["上午时间"]}
            )
            self.journey.append(
                {"地点": config["行程"]["中午地点"], "时间": config["行程"]["中午时间"]}
            )
            self.journey.append(
                {"地点": config["行程"]["下午地点"], "时间": config["行程"]["下午时间"]}
            )
            self.journey.append(
                {"地点": config["行程"]["晚上地点"], "时间": config["行程"]["晚上时间"]}
            )

            self.breakfast = config["就餐食堂"]["早"]
            self.lunch = config["就餐食堂"]["中"]
            self.dinner = config["就餐食堂"]["晚"]

            print("成功读取用户配置")
        except Exception as e:
            print("请补全配置文件！")
            config = ConfigParser()
            # 账户信息读取
            self.student_id = input("用户名:")
            config.set("账户", "用户名", self.student_id)
            self.secret_code = input("密码:")
            config.set("账户", "密码", self.secret_code)

            print("可选地点：")
            print()
            for i, v in enumerate(self.address_dic):
                print(v, end=", ")
                if (i + 1) % 5 == 0:
                    print()
            print()
            # 行程读取
            self.journey.append({"地点": input("上午地点:"), "时间": ""})
            self.journey.append({"地点": input("中午地点:"), "时间": ""})
            self.journey.append({"地点": input("下午地点:"), "时间": ""})
            self.journey.append({"地点": input("晚上地点:"), "时间": ""})

            config.add_section("行程")
            config.set("行程", "上午地点", self.journey[0]["地点"])
            config.set("行程", "上午时间", "")

            config.set("行程", "中午地点", self.journey[1]["地点"])
            config.set("行程", "中午时间", "")

            config.set("行程", "下午地点", self.journey[2]["地点"])
            config.set("行程", "下午时间", "")

            config.set("行程", "晚上地点", self.journey[3]["地点"])
            config.set("行程", "晚上时间", "")

            print("就餐食堂:")
            config.add_section("就餐食堂")
            self.breakfast = input("早餐食堂，没有填“无”: ")
            config.set("就餐食堂", "早", self.breakfast)
            self.lunch = input("午餐地点，没有填“无”: ")
            config.set("就餐食堂", "中", self.lunch)
            self.dinner = input("晚餐地点，没有填“无”: ")
            config.set("就餐食堂", "晚", self.dinner)
            with open(filename, "w", encoding="utf-8") as file:
                config.write(file)  # 数据写入配置文件
                print("成功写入配置文件")

    def login(self):
        try:
            # 打开网页
            self.driver.get("https://i.njcit.cn/EIP/user/index.htm")

            WebDriverWait(self.driver, 30).until(
                expected_conditions.presence_of_element_located((By.ID, "username"))
            )

            # 输入用户名
            self.driver.find_element(By.ID, "username").clear()
            self.driver.find_element(By.ID, "username").send_keys(self.student_id)

            # 输入密码
            self.driver.find_element(By.ID, "password").clear()
            self.driver.find_element(By.ID, "password").send_keys(self.secret_code)

            # 登录
            self.wait_for_click("CLASS_NAME", "btn-submit")

            WebDriverWait(self.driver, 10).until(
                expected_conditions.url_contains("EIP/user/index.htm"),
                message="登录失败,请检查账户信息和网络",
            )
            print("登录成功")
            return True
        except WebDriverException as e:
            print(e)
            self.desp += str(e) + "\n"
            return False

    def open_form(self):
        mark_of_success = False
        try:
            # 转到服务中心
            if mark_of_success := self.wait_for_click("LINK_TEXT", "服务中心"):
                # self.driver.find_element(By.LINK_TEXT, "服务中心").click()

                frame_1 = self.driver.find_element(
                    By.ID, "mini-17$body$4"
                ).find_element(By.TAG_NAME, "iframe")
                # 激活页面
                self.driver.switch_to.frame(frame_1)
                self.driver.find_element(By.XPATH, '//*[@id="keyword"]').clear()
                self.driver.find_element(By.XPATH, '//*[@id="keyword"]').send_keys(
                    "校内学生每日健康信息填报"
                )
                # 打开填报页面
                self.wait_for_click(
                    "CSS_SELECTOR",
                    "body > div.hall-detail-header > div.hall-detail-header-query > a.mini-button.hall-detail-btn-search.mini-button-plain",
                )

                if mark_of_success := self.wait_for_click(
                    "xpath", '//div[@id="form"]/div[2]/div[2]/div/a'
                ):
                    print("成功打开填报页面\n")
        except TimeoutException and WebDriverException as e:
            mark_of_success = False
            print(f"ERROR\n{e}\n")
            print("打开填报页面失败\n")
            self.desp += f"ERROR\n{e}\n"
            self.desp += "打开填报页面失败\n"
        finally:
            return mark_of_success

    def wait_for_click(self, by_="ID", value_=None):
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.element_to_be_clickable(
                    (by_.lower().replace("_", " "), value_)
                ),
                message=f"网页元素 {value_} 加载失败",
            )
            self.driver.find_element(
                by=by_.lower().replace("_", " "), value=value_
            ).click()
            return True
        except TimeoutException and WebDriverException as e:
            print(f"ERROR\n{e}\n")
            self.desp += f"ERROR\n{e}\n"
            return False

    def fill_in(self):
        mark_of_success = False

        st_id = 210
        checkall = "191checkall"
        try:

            # 页面激活1
            self.driver.switch_to.default_content()

            # 页面激活2
            self.driver.switch_to.frame(
                self.driver.find_element(By.ID, "mini-17$body$6").find_element(
                    By.TAG_NAME, "iframe"
                )
            )

            # 页面激活3
            self.driver.switch_to.frame(
                self.driver.find_element(By.XPATH, '//*[@id="mini-14$body$2"]/iframe')
            )
            if mark_of_success := self.select():

                if mark_of_success := self.radio():

                    # 上午行程添加
                    if mark_of_success := self.add_itinerary(
                        "toolbar_SWDD",
                        "1$cell$2",
                        f'mini-{st_id}${self.address_dic[self.journey[0]["地点"]]}',
                    ):
                        # 上午时间输入激活1
                        if mark_of_success := self.add_time(
                            "1$cell$3", f"mini-{st_id+1}", "mini-4"
                        ):
                            # 中午行程添加
                            if mark_of_success := self.add_itinerary(
                                "toolbar_ZWDD",
                                "2$cell$5",
                                f'mini-{st_id+5}${self.address_dic[self.journey[1]["地点"]]}',
                            ):
                                if mark_of_success := self.add_time(
                                    "2$cell$6", f"mini-{st_id+6}", "mini-4"
                                ):
                                    # 下午行程添加
                                    if mark_of_success := self.add_itinerary(
                                        "toolbar_XWDD",
                                        "3$cell$8",
                                        f'mini-{st_id+10}${self.address_dic[self.journey[2]["地点"]]}',
                                    ):
                                        if mark_of_success := self.add_time(
                                            "3$cell$9", f"mini-{st_id+11}", "mini-4"
                                        ):
                                            # 晚上行程添加
                                            if mark_of_success := self.add_itinerary(
                                                "toolbar_HTBD059F",
                                                "4$cell$11",
                                                f'mini-{st_id+15}${self.address_dic[self.journey[3]["地点"]]}',
                                            ):
                                                if mark_of_success := self.add_time(
                                                    "4$cell$12",
                                                    f"mini-{st_id+16}",
                                                    "mini-4",
                                                ):

                                                    # 接触人员
                                                    if mark_of_success := self.wait_for_click(
                                                        "XPATH",
                                                        '//*[@id="mini-'
                                                        + checkall
                                                        + '"]',
                                                    ):
                                                        # 早餐食堂及楼层，没有填“无”
                                                        self.driver.find_element(
                                                            By.ID,
                                                            "HT11E434$text",
                                                        ).send_keys(self.breakfast)

                                                        # 午餐食堂及楼层，没有填“无”
                                                        self.driver.find_element(
                                                            By.ID,
                                                            "HTDD18DB$text",
                                                        ).send_keys(self.lunch)

                                                        # 晚餐食堂及楼层，没有填“无”
                                                        self.driver.find_element(
                                                            By.ID,
                                                            "WCCZH$text",
                                                        ).send_keys(self.dinner)
                                                        print("成功填写表格")
        except WebDriverException as e:
            if not mark_of_success:
                print("表格填写失败")
                self.desp += "表格填写失败\n"
            print(e)
            self.desp += f"{e}\n"
        finally:
            return mark_of_success

    def select(self):
        # 当日身体状况
        if mark_of_success := self.wait_for_click(
            "XPATH", '//*[@id="DRSTZK"]/span/span/span[2]/span'
        ):
            if mark_of_success := self.wait_for_click(
                "XPATH", "//td[contains(.,'健康')]"
            ):
                # 现在何地 省
                if mark_of_success := self.wait_for_click(
                    "XPATH", '//*[@id="XZHS"]/span/span/span[2]/span'
                ):
                    if mark_of_success := self.wait_for_click(
                        "XPATH", "//td[contains(.,'江苏省')]"
                    ):
                        # 现在何地 市
                        if mark_of_success := self.wait_for_click(
                            "XPATH", '//*[@id="XZHSS"]/span/span/span[2]/span'
                        ):
                            if mark_of_success := self.wait_for_click(
                                "XPATH", "//td[contains(.,'南京市')]"
                            ):
                                # 现在何地 区
                                if mark_of_success := self.wait_for_click(
                                    "XPATH", '//*[@id="XZHQ"]/span/span/span[2]/span'
                                ):
                                    mark_of_success = self.wait_for_click(
                                        "XPATH", "//td[contains(.,'栖霞区')]"
                                    )
        return mark_of_success

    def radio(self):
        # 是否发热、咳嗽
        if mark_of_success := self.wait_for_click("ID", "mini-30$1"):
            # 是否接触发热、咳嗽症状人员
            if mark_of_success := self.wait_for_click("ID", "mini-31$1"):
                # 是否去过高中风险地区
                if mark_of_success := self.wait_for_click("ID", "mini-32$1"):
                    # 是否去过国外及港澳台地区
                    if mark_of_success := self.wait_for_click("ID", "mini-33$1"):
                        # 是否接触过国外及港澳台地区返回人员
                        if mark_of_success := self.wait_for_click("ID", "mini-34$1"):
                            if mark_of_success := self.wait_for_click(
                                "ID", "mini-35$1"
                            ):
                                if mark_of_success := self.wait_for_click(
                                    "ID", "mini-36$1"
                                ):
                                    # 是否首次填报
                                    mark_of_success = self.wait_for_click(
                                        "ID", "mini-37$1"
                                    )
        return mark_of_success

    def add_itinerary(self, *args):
        # 行程添加
        if mark_of_success := self.wait_for_click(
            "XPATH", f"//*[@id='{args[0]}']/a[1]"
        ):

            # 地点输入激活
            if mark_of_success := self.wait_for_click(
                "XPATH", f"//td[@id='{args[1]}']/div"
            ):

                # 选择地点
                mark_of_success = self.wait_for_click(
                    "XPATH",
                    f"//*[@id='{args[2]}']",
                )

        return mark_of_success

    def add_time(self, *args):
        # 时间输入激活1
        if mark_of_success := self.wait_for_click(
            "XPATH", f"//td[@id='{args[0]}']/div"
        ):

            # 时间输入激活2
            if mark_of_success := self.wait_for_click(
                "XPATH",
                f"//*[@id='{args[1]}']/span/span/span[2]/span",
            ):
                # 选择时间
                mark_of_success = self.wait_for_click(
                    "XPATH",
                    f"//*[@id='{args[2]}']/tbody/tr[2]/td/div/span[2]",
                )
        return mark_of_success

    def submit(self):
        mark_of_success = False
        try:
            # 激活页面
            self.driver.switch_to.parent_frame()

            # 提交表格
            if mark_of_success := self.wait_for_click(
                # "XPATH", '//a[contains(text(),"提交")]'
                "LINK_TEXT",
                "提交",
            ):

                # 确认提交
                if mark_of_success := self.wait_for_click(
                    # "XPATH", '//span[contains(.,"确定")]'
                    "LINK_TEXT",
                    "确定",
                ):
                    print("成功提交")
        except WebDriverException as e:
            print("提交失败")
            print(e)
            self.desp += f"提交失败\n{e}\n"
        finally:
            return mark_of_success

    def screen_capture(self):
        mark_of_success = False
        try:

            # # 激活初始页面
            # self.driver.switch_to.default_content()

            # if mark_of_success := self.open_form():
            #     # 页面激活1
            #     self.driver.switch_to.default_content()

            if mark_of_success := self.weui():
                self.driver.switch_to.default_content()
                # 截图保存
                # 生成年月日时分秒时间
                now_time = time.strftime(
                    "%Y-%m-%d-%H_%M_%S", time.localtime(time.time())
                )
                picture_path = (
                    f'{os.path.expanduser("~")}\\Desktop\\钉钉填报_{now_time}.png'
                )

                time.sleep(5)
                self.driver.save_screenshot(picture_path)

                # 关闭弹窗
                # self.wait_for_click("CSS_SELECTOR", "#mini-29 #\\33")
                print(f"成功截图并保存于\n {picture_path}")

        except WebDriverException as e:
            print("截图失败")
            print(e)
        finally:
            return mark_of_success

    def weui(self):
        self.driver.get("https://i.njcit.cn/EIP/weixin/weui/home.html")
        return self.wait_for_click(
            "XPATH", "//div[@id='div-desktop']/div[3]/div[2]/div[8]/div[2]/p"
        )

    def quit(self):
        self.driver.quit()

    # 微信推送
    def pushWechat(self):
        if "Failed" in self.desp:
            params = {"text": "签到失败", "desp": self.desp}
        else:
            params = {"text": "签到成功", "desp": self.desp}
        if self.desp != "":
            requests.post(scurl, params=params)


if __name__ == "__main__":
    HealthReport().start()
