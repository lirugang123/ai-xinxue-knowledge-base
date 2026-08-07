"""测试示例"""
import pytest
import sys
from pathlib import Path

# 添加scripts目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

def test_example():
    """测试示例功能"""
    assert True

def test_example_error():
    """测试错误处理"""
    assert True
