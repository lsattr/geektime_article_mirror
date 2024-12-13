import subprocess
import os

"""
Batch Git Push For Subfolders
"""


def git_push_subfolders(root_path):
    """
    遍历root_path下的所有子文件夹，并对每个子文件夹执行git add、commit和push操作

    :param root_path: 包含多个子文件夹的根目录路径
    """
    # 确保当前在git仓库根目录
    subprocess.run(["git", "checkout", "master"], check=True)
    index = 0
    # 遍历所有子文件夹
    aritlce_root_path = os.path.join(os.path.join(root_path, "Article"), "专栏")
    for subfolder in os.listdir(aritlce_root_path):
        subfolder_path = os.path.join(aritlce_root_path, subfolder)

        # 确保是文件夹
        if os.path.isdir(subfolder_path):

            try:
                print(f"处理文件夹: {subfolder}")

                # 切换到子文件夹
                os.chdir(subfolder_path)

                # git add 所有文件
                subprocess.run(["git", "add", "."], check=True)

                # git commit，使用文件夹名作为commit消息
                commit_message = f"Add contents of {subfolder}"
                subprocess.run(["git", "commit", "-m", commit_message], check=True)

                # git push
                subprocess.run(["git", "push"], check=True)

                print(f"成功处理并推送 {subfolder}")

            except subprocess.CalledProcessError as e:
                print(f"处理 {subfolder} 时出错: {e}")
            except Exception as e:
                print(f"未知错误: {e}")

            # 返回到根目录
            os.chdir(root_path)


def main():
    # 获取脚本的绝对路径
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 执行批量推送
    git_push_subfolders(script_dir)


if __name__ == "__main__":
    main()
