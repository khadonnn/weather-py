# utils.py
import json
from difflib import get_close_matches

def load_provinces(filename='provinces.json'):
    """Đọc file JSON và trả về danh sách tên tỉnh"""
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [item['name'] for item in data.values()]

def find_province(query, province_list):
    """Tìm tỉnh gần nhất từ input người dùng"""
    query = query.strip().lower()
    matches = get_close_matches(query, province_list, n=3, cutoff=0.3)
    return matches