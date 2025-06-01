import pickle
import requests
from io import BytesIO

def load_model_from_github():
    """
    从GitHub仓库加载LNTB-Radiomics.pkl模型文件
    
    返回:
        加载的模型对象
    """
    # GitHub仓库信息
    repo_owner = "xugechina"
    repo_name = "LNTB-Radiomics"
    file_path = "LNTB-Radiomics.pkl"  # 模型文件路径（根目录）
    branch = "main"  # 默认分支，如果你的分支不是main，请修改这里
    
    try:
        # 构建GitHub raw文件URL
        url = f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/{branch}/{file_path}"
        
        # 发送HTTP请求获取文件内容
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        
        # 从响应内容加载pickle模型
        model_file = BytesIO(response.content)
        model = pickle.load(model_file)
        
        print("模型加载成功！")
        return model
    
    except requests.exceptions.RequestException as e:
        print(f"无法从GitHub获取模型文件: {e}")
        return None
    except Exception as e:
        print(f"加载模型时出错: {e}")
        return None

if __name__ == "__main__":
    # 加载模型
    model = load_model_from_github()
    
    if model is not None:
        # 在这里你可以使用加载的模型
        print("模型已加载，可以用于预测等操作")
    else:
        print("模型加载失败")