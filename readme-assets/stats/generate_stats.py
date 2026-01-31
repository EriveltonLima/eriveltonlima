#!/usr/bin/env python3
"""
Script para gerar estatísticas SVG locais para o README
"""

import json
import subprocess
from datetime import datetime

def create_stats_svg():
    """Cria SVG com estatísticas do GitHub"""
    
    # Dados de exemplo (pode ser substituído por API real do GitHub)
    stats = {
        "repositories": 24,
        "followers": 42,
        "stars": 58,
        "commits_monthly": 45,
        "contributions": 1280,
        "since": 2020
    }
    
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="400" height="200" viewBox="0 0 400 200">
  <style>
    .title {{ font-family: Arial, sans-serif; font-size: 18px; font-weight: bold; fill: #0AE448; }}
    .stat {{ font-family: Arial, sans-serif; font-size: 24px; font-weight: bold; fill: #FFFFFF; }}
    .label {{ font-family: Arial, sans-serif; font-size: 12px; fill: #9F9F9F; }}
    .bg {{ fill: #151515; }}
  </style>
  
  <rect width="400" height="200" rx="10" class="bg"/>
  
  <text x="200" y="30" text-anchor="middle" class="title">GitHub Statistics</text>
  
  <!-- Linha 1 -->
  <g transform="translate(50, 70)">
    <text x="0" y="0" class="stat">{stats['repositories']}+</text>
    <text x="0" y="20" class="label">Repositories</text>
  </g>
  
  <g transform="translate(150, 70)">
    <text x="0" y="0" class="stat">{stats['followers']}</text>
    <text x="0" y="20" class="label">Followers</text>
  </g>
  
  <g transform="translate(250, 70)">
    <text x="0" y="0" class="stat">{stats['stars']}</text>
    <text x="0" y="20" class="label">Stars</text>
  </g>
  
  <!-- Linha 2 -->
  <g transform="translate(50, 140)">
    <text x="0" y="0" class="stat">{stats['commits_monthly']}</text>
    <text x="0" y="20" class="label">Commits/Month</text>
  </g>
  
  <g transform="translate(150, 140)">
    <text x="0" y="0" class="stat">{stats['contributions']}+</text>
    <text x="0" y="20" class="label">Contributions</text>
  </g>
  
  <g transform="translate(250, 140)">
    <text x="0" y="0" class="stat">{stats['since']}</text>
    <text x="0" y="20" class="label">Since</text>
  </g>
</svg>'''
    
    with open('readme-assets/stats/github_stats.svg', 'w') as f:
        f.write(svg_content)
    
    print("SVG de estatisticas gerado: readme-assets/stats/github_stats.svg")

def create_languages_svg():
    """Cria SVG com distribuição de linguagens"""
    
    languages = [
        {"name": "Python", "percentage": 35, "color": "#0AE448"},
        {"name": "JavaScript", "percentage": 25, "color": "#0AE448"},
        {"name": "TypeScript", "percentage": 20, "color": "#0AE448"},
        {"name": "Shell", "percentage": 15, "color": "#0AE448"},
        {"name": "Other", "percentage": 5, "color": "#0AE448"}
    ]
    
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" width="400" height="250" viewBox="0 0 400 250">
  <style>
    .title { font-family: Arial, sans-serif; font-size: 18px; font-weight: bold; fill: #0AE448; }
    .lang-name { font-family: Arial, sans-serif; font-size: 14px; fill: #FFFFFF; }
    .lang-percent { font-family: Arial, sans-serif; font-size: 12px; fill: #9F9F9F; }
    .bg { fill: #151515; }
  </style>
  
  <rect width="400" height="250" rx="10" class="bg"/>
  
  <text x="200" y="30" text-anchor="middle" class="title">Top Languages</text>
  
  <!-- Barras de progresso -->
'''
    
    y_position = 70
    for i, lang in enumerate(languages):
        bar_width = lang['percentage'] * 3  # 3px por porcentagem
        svg_content += f'''
  <!-- {lang['name']} -->
  <rect x="50" y="{y_position}" width="{bar_width}" height="15" fill="{lang['color']}" rx="3"/>
  <text x="45" y="{y_position + 11}" text-anchor="end" class="lang-name">{lang['name']}</text>
  <text x="{bar_width + 60}" y="{y_position + 11}" class="lang-percent">{lang['percentage']}%</text>
'''
        y_position += 30
    
    svg_content += '</svg>'
    
    with open('readme-assets/stats/languages.svg', 'w') as f:
        f.write(svg_content)
    
    print("SVG de linguagens gerado: readme-assets/stats/languages.svg")

def main():
    """Função principal"""
    print("Gerando estatisticas SVG locais...")
    create_stats_svg()
    create_languages_svg()
    print("OK Todos os SVGs foram gerados com sucesso!")
    print("\nEstrutura criada:")
    print("readme-assets/")
    print("├── badges/")
    print("│   ├── linkedin.svg")
    print("│   ├── gmail.svg")
    print("│   └── portfolio.svg")
    print("└── stats/")
    print("    ├── github_stats.svg")
    print("    └── languages.svg")
    print("\nPara usar no README:")
    print('<img src="./readme-assets/stats/github_stats.svg" alt="GitHub Stats" />')

if __name__ == "__main__":
    main()