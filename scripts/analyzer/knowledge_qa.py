#!/usr/bin/env python3
"""
知识问答系统
基于知识图谱的智能问答
"""

import json
from pathlib import Path
from typing import Dict, List, Optional

class KnowledgeQA:
    """知识问答系统"""
    
    def __init__(self, graph_path: Path):
        self.graph_path = graph_path
        self.knowledge = self._load_knowledge()
    
    def _load_knowledge(self) -> Dict:
        """加载知识库"""
        with open(self.graph_path) as f:
            return json.load(f)
    
    def query(self, question: str) -> Dict:
        """回答问题"""
        # 简单匹配
        question = question.replace('？', '?').replace('?', '').strip()
        
        # 实体识别
        entities = self._extract_entities(question)
        
        # 答案生成
        answers = self._generate_answers(entities, question)
        
        return {
            'question': question,
            'entities': entities,
            'answers': answers,
            'confidence': self._calculate_confidence(answers)
        }
    
    def _extract_entities(self, question: str) -> List[str]:
        """提取实体"""
        entities = []
        known_entities = [n['name'] for n in self.knowledge.get('nodes', [])]
        
        for entity in known_entities:
            if entity in question:
                entities.append(entity)
        
        return entities
    
    def _generate_answers(self, entities: List[str], question: str) -> List[Dict]:
        """生成答案"""
        answers = []
        
        if not entities:
            return [{'type': 'general', 'content': '请提供更多上下文'}]
        
        # 根据实体生成答案
        for entity in entities:
            entity_data = next((n for n in self.knowledge['nodes'] if n['name'] == entity), None)
            if entity_data:
                answers.append({
                    'type': 'entity',
                    'entity': entity,
                    'content': entity_data.get('description', '暂无描述'),
                    'source': entity_data['type']
                })
        
        return answers
    
    def _calculate_confidence(self, answers: List[Dict]) -> float:
        """计算置信度"""
        if not answers:
            return 0.0
        return min(0.9, len(answers) * 0.3)

def main():
    """主函数"""
    qa = KnowledgeQA(Path('knowledge/graph/knowledge_graph.json'))
    
    # 测试问答
    test_questions = [
        '什么是知行合一？',
        '王阳明是谁？',
        '什么是致良知？'
    ]
    
    for question in test_questions:
        result = qa.query(question)
        print(f"\n问题：{question}")
        print(f"答案：{result['answers'][0]['content'] if result['answers'] else '暂无答案'}")
        print(f"置信度：{result['confidence']:.2f}")

if __name__ == '__main__':
    main()
