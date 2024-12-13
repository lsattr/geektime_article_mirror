import os
import time
from bs4 import BeautifulSoup
from typing import List
import requests
from urllib.parse import urljoin, urlparse, urldefrag

# 失败后修改主课程Index和子课程Index
# 从失败位置开始继续爬取数据
mainCourseIndex = 0
subCourseIndex = 0


class spider:
    def __init__(self):
        pass
        self.base_url = "https://learn.lianglianglee.com/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        self.output_dir = "./Article"

        os.makedirs(self.output_dir, exist_ok=True)

    def fetch_page_content(self, url: str) -> str:
        """
        获取网页内容

        :param url: 网页地址
        :return: 网页HTML内容
        """
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"获取网页内容时发生错误: {e}")
            return ""

    def parse_course_list(self) -> List:
        """
        解析课程列表

        :return: 课程信息列表
        """
        html_content = self.fetch_page_content(self.base_url)
        soup = BeautifulSoup(html_content, "html.parser")

        # Remove Static JS
        script_tags = soup.find_all("script", attrs={"data-cfasync": "false"})
        for tag in script_tags:
            tag.decompose()
        script_tags = soup.find_all("script", attrs={"data-website-id": True})
        for tag in script_tags:
            tag.decompose()
        script_tags = soup.find_all("script", attrs={"async": True})
        for tag in script_tags:
            tag.decompose()

        courses = []
        book_post_div = soup.find("div", class_="book-post")
        all_divs = book_post_div.find_all("div")
        course_div = all_divs[1]
        course_ul = course_div.find("ul")
        for li in course_ul.find_all("li"):
            a_tag = li.find("a")
            if a_tag:
                # 提取文本和href
                text = a_tag.get_text(strip=True)
                # href = a_tag.get("href")
                courses.append(text)

        for css in soup.find_all("link", rel="stylesheet"):
            href = css.get("href")
            if "static" not in href:
                continue
            if href:
                self.download_resource(
                    self.normalize_url(self.base_url, href), self.output_dir
                )

        # 处理JavaScript资源
        for script in soup.find_all("script", src=True):
            js_url = script.get("src")
            if js_url:
                self.download_resource(
                    self.normalize_url(self.base_url, js_url), self.output_dir
                )

        for img in soup.find_all("img", src=True):
            img_url = img.get("src")
            if img_url:
                self.download_resource(
                    self.normalize_url(self.base_url, img_url), self.output_dir
                )

        # Remove DRM
        node_to_remove = all_divs[0]
        node_to_remove.extract()

        # 保存网页HTML文件
        with open(
            os.path.join(self.output_dir, "index.html"), "w", encoding="utf-8"
        ) as f:
            f.write(str(soup))

        return courses

    def normalize_url(self, base_url, url):
        """
        标准化URL,处理特殊的相对路径情况
        """
        # 如果是以/开头的路径，需要特殊处理
        if url.startswith("/") and not url.startswith("//"):
            # 获取base_url的域名部分
            parsed_base = urlparse(base_url)
            return f"{parsed_base.scheme}://{parsed_base.netloc}{url}"
        return urljoin(base_url, url)

    def get_course_content(self, course_name: str, failed_download_course_name: str):
        rootDir = os.path.join(self.output_dir, "专栏")
        rootDir = os.path.join(rootDir, course_name)
        os.makedirs(rootDir, exist_ok=True)

        final_course_name = "专栏/" + course_name + "/"

        response = requests.get(self.base_url + final_course_name)
        html_content = response.text

        # 解析课程
        soup = BeautifulSoup(html_content, "html.parser")

        # Remove Static JS
        script_tags = soup.find_all("script", attrs={"data-cfasync": "false"})
        for tag in script_tags:
            tag.decompose()
        script_tags = soup.find_all("script", attrs={"data-website-id": True})
        for tag in script_tags:
            tag.decompose()
        script_tags = soup.find_all("script", attrs={"async": True})
        for tag in script_tags:
            tag.decompose()

        book_post_div = soup.find("div", class_="book-post")
        all_divs = book_post_div.find_all("div")
        course_div = all_divs[1]
        course_ul = course_div.find("ul")
        innerCourse = []
        for li in course_ul.find_all("li"):
            a_tag = li.find("a")
            if a_tag:
                # 提取文本和href
                text = a_tag.get_text(strip=True)
                innerCourse.append(text)
        # Remove DRM
        node_to_remove = all_divs[0]
        node_to_remove.extract()

        soup.prettify()
        # 保存网页HTML文件
        with open(os.path.join(rootDir, "index.html"), "w", encoding="utf-8") as f:
            f.write(str(soup))
        for i in range(len(innerCourse)):
            if course_name == failed_download_course_name and i < subCourseIndex:
                continue
            print("下载子课程:", innerCourse[i], "Index:", i)
            self.getInnerCourseContent(
                course_name=course_name,
                inner_course_name=innerCourse[i],
                outputDir=rootDir,
            )
            time.sleep(5)

    def getInnerCourseContent(
        self, course_name: str, inner_course_name: str, outputDir: str
    ):
        final_course_name = "专栏/" + course_name + "/" + inner_course_name
        rootPageURL = self.base_url + final_course_name
        response = requests.get(self.base_url + final_course_name)
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        # Remove Static JS
        script_tags = soup.find_all("script", attrs={"data-cfasync": "false"})
        for tag in script_tags:
            tag.decompose()
        script_tags = soup.find_all("script", attrs={"data-website-id": True})
        for tag in script_tags:
            tag.decompose()
        script_tags = soup.find_all("script", attrs={"async": True})
        for tag in script_tags:
            tag.decompose()

        book_post_div = soup.find("div", class_="book-post")
        if book_post_div:
            all_divs = book_post_div.find_all("div")

            # Remove DRM
            node_to_remove = all_divs[0]
            node_to_remove.extract()
            soup.prettify()
        else:
            print("子课程文档错误")

        imageOutputDir = os.path.join(outputDir, "assets")
        os.makedirs(imageOutputDir, exist_ok=True)
        for img in soup.find_all("img", src=True):
            img_url = img.get("src")
            if "favicon" in img_url:
                continue
            if img_url:

                downloadURL = self.base_url + "专栏/" + course_name
                downloadURL = downloadURL + "/" + img_url
                self.download_resource(downloadURL, "./Article")

        # 保存网页HTML文件
        with open(
            os.path.join(outputDir, inner_course_name), "w", encoding="utf-8"
        ) as f:
            f.write(str(soup))

    def download_resource(
        self,
        resource_url: str,
        output_directory: str,
    ):
        try:
            response = requests.get(resource_url)
            if response.status_code == 200:
                # 移除URL中的fragment部分
                parsed_url = urlparse(urldefrag(resource_url)[0])
                # 创建资源的相对路径
                # 去掉域名部分，保留路径
                relative_path = parsed_url.path.lstrip("/")
                resource_path = os.path.join(output_directory, relative_path)

                # 确保目录存在
                os.makedirs(os.path.dirname(resource_path), exist_ok=True)

                # 保存资源
                with open(resource_path, "wb") as f:
                    f.write(response.content)

                # 返回相对路径
                return relative_path
            return None
        except Exception as e:
            print(f"下载 {resource_url} 失败: {e}")
            exit()
            return resource_url

    def run(self):
        course = self.parse_course_list()
        time.sleep(2)
        print(
            "开始从课程:",
            course[mainCourseIndex],
            "子课程Index:",
            subCourseIndex,
            "开始下载",
        )
        for i in range(len(course)):
            if i < mainCourseIndex:
                continue
            print("下载课程:", course[i], "Index:", i)
            self.get_course_content(
                course[i], failed_download_course_name=course[mainCourseIndex]
            )
            time.sleep(1)


if __name__ == "__main__":
    spider = spider()
    spider.run()
