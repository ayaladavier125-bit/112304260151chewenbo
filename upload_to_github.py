import os
import base64
import requests

# GitHub 仓库信息
GITHUB_TOKEN = input("请输入你的 GitHub Personal Access Token: ")
REPO_OWNER = "ayaladavier125-bit"
REPO_NAME = "112304260151chewenbo"

# 要上传的文件列表
files_to_upload = [
    "README.md",
    "UPLOAD_GUIDE.md",
    ".gitignore",
    "src/sentiment_analysis.py",
    "src/sentiment_analysis_basic.py",
    "submission/submission.csv",
    "push_to_github.bat",
    "images/112304260151_车文博_kaggle_score.png"
]

def upload_file(file_path):
    """上传单个文件到 GitHub"""
    with open(file_path, 'rb') as f:
        content = f.read()
    
    encoded_content = base64.b64encode(content).decode('utf-8')
    
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{file_path}"
    
    data = {
        "message": f"Add {file_path}",
        "content": encoded_content
    }
    
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.put(url, json=data, headers=headers)
    
    if response.status_code == 201:
        print(f"✓ 成功上传: {file_path}")
        return True
    elif response.status_code == 422:
        # 文件已存在，更新它
        # 需要先获取 sha
        get_url = url
        get_response = requests.get(get_url, headers=headers)
        if get_response.status_code == 200:
            sha = get_response.json()['sha']
            data['sha'] = sha
            response = requests.put(url, json=data, headers=headers)
            if response.status_code == 200:
                print(f"✓ 成功更新: {file_path}")
                return True
    print(f"✗ 上传失败: {file_path}")
    print(f"  错误: {response.text}")
    return False

if __name__ == "__main__":
    print("=" * 60)
    print("GitHub 文件上传工具")
    print(f"仓库: {REPO_OWNER}/{REPO_NAME}")
    print("=" * 60)
    
    success_count = 0
    for file_path in files_to_upload:
        if os.path.exists(file_path):
            if upload_file(file_path):
                success_count += 1
        else:
            print(f"✗ 文件不存在: {file_path}")
    
    print("=" * 60)
    print(f"上传完成！成功: {success_count}/{len(files_to_upload)}")
    print(f"查看仓库: https://github.com/{REPO_OWNER}/{REPO_NAME}")