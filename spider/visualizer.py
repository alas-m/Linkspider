import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(graph, output_file="graph.png"):
    plt.figure(figsize=(16, 12))
    
    pos = nx.spring_layout(graph, k=1, iterations=50)
    
    nx.draw_networkx_nodes(graph, pos, node_size=100, node_color='lightblue', alpha=0.9)
    nx.draw_networkx_edges(graph, pos, edge_color='gray', alpha=0.6, arrows=True, arrowsize=10)
    
    degrees = dict(graph.degree())
    important_nodes = [node for node, degree in degrees.items() if degree > 2]
    labels = {node: node.split('//')[1].split('/')[0] if '//' in node else node for node in important_nodes}
    
    nx.draw_networkx_labels(graph, pos, labels, font_size=8, font_weight='bold')
    
    plt.title(f"Website Link Graph\n{len(graph.nodes)} nodes, {len(graph.edges)} edges")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"[+] Graph saved to {output_file}")