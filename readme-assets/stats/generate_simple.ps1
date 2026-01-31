# Script PowerShell para gerar SVGs simples

Write-Host "Gerando SVG de estatisticas..."

$statsSvg = @'
<svg xmlns="http://www.w3.org/2000/svg" width="400" height="200" viewBox="0 0 400 200">
  <style>
    .title { font-family: Arial, sans-serif; font-size: 18px; font-weight: bold; fill: #0AE448; }
    .stat { font-family: Arial, sans-serif; font-size: 24px; font-weight: bold; fill: #FFFFFF; }
    .label { font-family: Arial, sans-serif; font-size: 12px; fill: #9F9F9F; }
    .bg { fill: #151515; }
  </style>
  
  <rect width="400" height="200" rx="10" class="bg"/>
  
  <text x="200" y="30" text-anchor="middle" class="title">GitHub Statistics</text>
  
  <!-- Linha 1 -->
  <g transform="translate(50, 70)">
    <text x="0" y="0" class="stat">24+</text>
    <text x="0" y="20" class="label">Repositories</text>
  </g>
  
  <g transform="translate(150, 70)">
    <text x="0" y="0" class="stat">42</text>
    <text x="0" y="20" class="label">Followers</text>
  </g>
  
  <g transform="translate(250, 70)">
    <text x="0" y="0" class="stat">58</text>
    <text x="0" y="20" class="label">Stars</text>
  </g>
  
  <!-- Linha 2 -->
  <g transform="translate(50, 140)">
    <text x="0" y="0" class="stat">45</text>
    <text x="0" y="20" class="label">Commits/Month</text>
  </g>
  
  <g transform="translate(150, 140)">
    <text x="0" y="0" class="stat">1280+</text>
    <text x="0" y="20" class="label">Contributions</text>
  </g>
  
  <g transform="translate(250, 140)">
    <text x="0" y="0" class="stat">2020</text>
    <text x="0" y="20" class="label">Since</text>
  </g>
</svg>
'@

$statsSvg | Out-File -FilePath "github_stats.svg" -Encoding UTF8
Write-Host "SVG de estatisticas gerado: github_stats.svg"

Write-Host "Gerando SVG de linguagens..."

$langSvg = @'
<svg xmlns="http://www.w3.org/2000/svg" width="400" height="250" viewBox="0 0 400 250">
  <style>
    .title { font-family: Arial, sans-serif; font-size: 18px; font-weight: bold; fill: #0AE448; }
    .lang-name { font-family: Arial, sans-serif; font-size: 14px; fill: #FFFFFF; }
    .lang-percent { font-family: Arial, sans-serif; font-size: 12px; fill: #9F9F9F; }
    .bg { fill: #151515; }
  </style>
  
  <rect width="400" height="250" rx="10" class="bg"/>
  
  <text x="200" y="30" text-anchor="middle" class="title">Top Languages</text>
  
  <!-- Python -->
  <rect x="50" y="70" width="105" height="15" fill="#0AE448" rx="3"/>
  <text x="45" y="81" text-anchor="end" class="lang-name">Python</text>
  <text x="165" y="81" class="lang-percent">35%</text>
  
  <!-- JavaScript -->
  <rect x="50" y="100" width="75" height="15" fill="#0AE448" rx="3"/>
  <text x="45" y="111" text-anchor="end" class="lang-name">JavaScript</text>
  <text x="135" y="111" class="lang-percent">25%</text>
  
  <!-- TypeScript -->
  <rect x="50" y="130" width="60" height="15" fill="#0AE448" rx="3"/>
  <text x="45" y="141" text-anchor="end" class="lang-name">TypeScript</text>
  <text x="120" y="141" class="lang-percent">20%</text>
  
  <!-- Shell -->
  <rect x="50" y="160" width="45" height="15" fill="#0AE448" rx="3"/>
  <text x="45" y="171" text-anchor="end" class="lang-name">Shell</text>
  <text x="105" y="171" class="lang-percent">15%</text>
  
  <!-- Other -->
  <rect x="50" y="190" width="15" height="15" fill="#0AE448" rx="3"/>
  <text x="45" y="201" text-anchor="end" class="lang-name">Other</text>
  <text x="75" y="201" class="lang-percent">5%</text>
</svg>
'@

$langSvg | Out-File -FilePath "languages.svg" -Encoding UTF8
Write-Host "SVG de linguagens gerado: languages.svg"

Write-Host "Todos os SVGs foram gerados com sucesso!"
Write-Host ""
Write-Host "Estrutura:"
Write-Host "readme-assets/stats/"
Write-Host "├── github_stats.svg"
Write-Host "└── languages.svg"