import os
import sys
import base64
import requests
from urllib.parse import quote

REPO_OWNER = "ayaladavier125-bit"
REPO_NAME = "112304260151chewenbo"

files_to_upload = [
    "README.md",
    "UPLOAD_GUIDE.md",
    ".gitignore",
    "src/sentiment_analysis.py",
    "src/sentiment_analysis_basic.py",
    "submission/submission.csv",
    "push_to_github.bat",
    "upload_to_github.py",
    "upload_with_token.py",
    "upload_final.py"
]

def upload_file(file_path, token):
    if not os.path.exists(file_path):
        print(f"✗ 文件不存在: {file_path}")
        return False
    
    with open(file_path, 'rb') as f:
        content = f.read()
    
    encoded_content = base64.b64encode(content).decode('utf-8')
    
    encoded_path = quote(file_path)
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{encoded_path}"
    
    data = {"message": "Update files", "content": encoded_content}
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        response = requests.put(url, json=data, headers=headers)
        
        if response.status_code == 201:
            print(f"✓ 成功上传: {file_path}")
            return True
        elif response.status_code == 422:
            get_response = requests.get(url, headers=headers)
            if get_response.status_code == 200:
                data['sha'] = get_response.json()['sha']
                response = requests.put(url, json=data, headers=headers)
                if response.status_code == 200:
                    print(f"✓ 成功更新: {file_path}")
                    return True
        print(f"✗ 上传失败: {file_path}")
        print(f"  状态码: {response.status_code}")
        return False
    except Exception as e:
        print(f"✗ 上传异常: {file_path}")
        print(f"  错误: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python upload_final.py <GitHub Token>")
        print("示例: python upload_final.py ghp_xxx")
        sys.exit(1)
    
    token = sys.argv[1].strip()
    print(f"正在上传到仓库: {REPO_OWNER}/{REPO_NAME}")
    print("=" * 50)
    
    success_count = 0
    for file_path in files_to_upload:
        if upload_file(file_path, token):
            success_count += 1
    
    print("=" * 50)
    print(f"上传完成！成功: {success_count}/{len(files_to_upload)}")
    print(f"仓库地址: https://github.com/{REPO_OWNER}/{REPO_NAME}")