import pytest
import sys
from pathlib import Path

# 添加scripts目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

def test_knowledge_parser():
    """测试知识解析器"""
    from parser.knowledge_parser import KnowledgeParser
    parser = KnowledgeParser()
    result = parser.parse_text("知行合一")
    assert result["status"] == "parsed"

def test_knowledge_qa():
    """测试知识问答"""
    from analyzer.knowledge_qa import KnowledgeQA
    qa = KnowledgeQA()
    qa.add_qa("什么是知行合一？", "知行合一是王阳明心学的核心思想")
    result = qa.query("什么是知行合一？")
    assert "知行合一" in result

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
