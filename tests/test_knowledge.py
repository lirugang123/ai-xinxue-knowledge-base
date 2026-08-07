import pytest

def test_knowledge_parser():
    """测试知识解析器"""
    from scripts.parser.knowledge_parser import KnowledgeParser
    parser = KnowledgeParser()
    result = parser.parse_text("知行合一")
    assert result["status"] == "parsed"

def test_knowledge_qa():
    """测试知识问答"""
    from scripts.analyzer.knowledge_qa import KnowledgeQA
    qa = KnowledgeQA()
    qa.add_qa("什么是知行合一？", "知行合一是王阳明心学的核心思想")
    result = qa.query("什么是知行合一？")
    assert "知行合一" in result

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
