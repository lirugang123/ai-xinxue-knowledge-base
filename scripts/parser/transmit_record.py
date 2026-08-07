#!/usr/bin/env python3
"""
传习录文本解析器
将文言文转换为结构化知识
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Optional

class ChuanchiParser:
    """传习录解析器"""
    
    def __init__(self, text_path: Path):
        self.text_path = text_path
        self.sections = []
        self.entities = []
        self.relations = []
    
    def parse(self) -> Dict:
        """解析传习录文本"""
        with open(self.text_path) as f:
            text = f.read()
        
        # 按章节分割
        chapters = re.split(r'卷[一二三]', text)
        
        result = {
            'title': '传习录',
            'chapters': len(chapters),
            'sections': self._extract_sections(text),
            'entities': self._extract_entities(text),
            'relations': self._extract_relations(text)
        }
        
        return result
    
    def _extract_sections(self, text: str) -> List[Dict]:
        """提取章节结构"""
        sections = []
        pattern = r'([一二三四五六七八九十]+)\.\s*(.+?)(?=\n\s*[一二三四五六七八九十]+\.|$)'
        matches = re.findall(pattern, text)
        
        for num, title in matches:
            sections.append({
                'number': num,
                'title': title.strip(),
                'content': self._clean_text(title)
            })
        
        return sections
    
    def _extract_entities(self, text: str) -> List[Dict]:
        """提取实体"""
        entities = []
        
        # 人物实体
        persons = ['王阳明', '徐爱', '陆澄', '钱德洪', '朱熹', '孔子', '孟子']
        for person in persons:
            if person in text:
                entities.append({
                    'name': person,
                    'type': 'person',
                    'mentions': text.count(person)
                })
        
        # 概念实体
        concepts = ['良知', '知行合一', '心即理', '致良知', '格物', '诚意']
        for concept in concepts:
            if concept in text:
                entities.append({
                    'name': concept,
                    'type': 'concept',
                    'mentions': text.count(concept)
                })
        
        return entities
    
    def _extract_relations(self, text: str) -> List[Dict]:
        """提取关系"""
        relations = []
        
        # 师徒关系
        relations.append({'subject': '王阳明', 'predicate': '传授', 'object': '徐爱'})
        relations.append({'subject': '王阳明', 'predicate': '传授', 'object': '陆澄'})
        relations.append({'subject': '王阳明', 'predicate': '传授', 'object': '钱德洪'})
        
        return relations
    
    def _clean_text(self, text: str) -> str:
        """清理文本"""
        return re.sub(r'[^\w\s\u4e00-\u9fff]', '', text)

def main():
    """主函数"""
    parser = ChuanchiParser(Path('knowledge/texts/chuanxi_record.txt'))
    result = parser.parse()
    
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
