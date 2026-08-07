#!/usr/bin/env python3
"""
知识问答系统
"""

import json

class KnowledgeQA:
    """知识问答"""
    
    def __init__(self):
        self.qa_pairs = []
    
    def add_qa(self, question: str, answer: str):
        """添加问答对"""
        self.qa_pairs.append({"q": question, "a": answer})
    
    def query(self, question: str) -> str:
        """查询问题"""
        for qa in self.qa_pairs:
            if question in qa["q"]:
                return qa["a"]
        return "未找到相关答案"

def main():
    qa = KnowledgeQA()
    qa.add_qa("什么是知行合一？", "知行合一是王阳明心学的核心思想")
    result = qa.query("什么是知行合一？")
    print(f"答案: {result}")

if __name__ == "__main__":
    main()
