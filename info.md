# 1.tạo môi trường trên myenv tránh global nếu không muốn cài

python -m venv myenv

# 2. kích hoạt

myenv\Scripts\activate

_(myenv) C:\your-project-path>_

# 3 kiểm tra những thư viện đã cài hay chưa

```py
pip list
```

=> nếu chưa

```py
pip install streamlit requests
```

# 4 tạo file requirement.txt (quan trọng)

```py
pip freeze > requirements.txt
```

# 5 chạy file app.py

```py
streamlit run app.py
```
