#!/usr/bin/env python3
"""
知识图谱构建器
构建心学知识图谱
"""

import json
from pathlib import Path
from typing import Dict, List
import networkx as nx

class KnowledgeGraphBuilder:
    """知识图谱构建器"""
    
    def __init__(self):
        self.graph = nx.Graph()
        self.nodes = []
        self.edges = []
    
    def add_entity(self, name: str, entity_type: str, description: str = ''):
        """添加实体节点"""
        self.graph.add_node(name, type=entity_type, description=description)
        self.nodes.append({
            'name': name,
            'type': entity_type,
            'description': description
        })
    
    def add_relation(self, subject: str, predicate: str, obj: str):
        """添加关系边"""
        self.graph.add_edge(subject, obj, relation=predicate)
        self.edges.append({
            'subject': subject,
            'predicate': predicate,
            'object': obj
        })
    
    def build_from_data(self, data: Dict):
        """从数据构建图谱"""
        # 添加实体
        for entity in data.get('entities', []):
            self.add_entity(
                entity['name'],
                entity['type'],
                f"出现{entity['mentions']}次"
            )
        
        # 添加关系
        for relation in data.get('relations', []):
            self.add_relation(
                relation['subject'],
                relation['predicate'],
                relation['object']
            )
    
    def save_graph(self, output_path: Path):
        """保存图谱"""
        graph_data = {
            'nodes': self.nodes,
            'edges': self.edges,
            'statistics': {
                'node_count': len(self.nodes),
                'edge_count': len(self.edges)
            }
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(graph_data, f, ensure_ascii=False, indent=2)
    
    def find_connections(self, entity: str, depth: int = 2) -> List[Dict]:
        """查找实体连接"""
        connections = []
        try:
            connected = nx.single_source_shortest_path(self.graph, entity, cutoff=depth)
            for node, path in connected.items():
                if node != entity:
                    connections.append({
                        'entity': node,
                        'path': path,
                        'distance': len(path) - 1
                    })
        except:
            pass
        return connections

def main():
    """主函数"""
    builder = KnowledgeGraphBuilder()
    
    # 添加核心概念
    builder.add_entity('王阳明', 'person', '明代思想家，心学集大成者')
    builder.add_entity('良知', 'concept', '内在的道德直觉')
    builder.add_entity('知行合一', 'concept', '知识与行动的统一')
    builder.add_entity('致良知', 'concept', '扩充内在良知')
    
    # 添加关系
    builder.add_relation('王阳明', '创立', '心学')
    builder.add_relation('王阳明', '发展', '致良知')
    builder.add_relation('良知', '核心实践', '知行合一')
    
    builder.save_graph(Path('knowledge/graph/knowledge_graph.json'))

if __name__ == '__main__':
    main()
