# R070TAC

## Descrição

Tipos de Acesso

---

## Resumo

- Campos: 14
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipAcc | Number(003,0) | Não | Código do Tipo de Acesso |
| DesTAc | String(080) | Sim | Descrição do Tipo de Acesso |
| DesRed | String(020) | Sim | Título Reduzida do Tipo de Acesso |
| AcaTAc | Number(001,0) | Sim | Ação para o Tipo de Acesso |
| ConApu | String(001) | Sim | Considerar Tipo de Acesso p/ Apuração |
| CodFnc | Number(002,0) | Sim | Codigo da Função a Ser Gerada no Acesso |
| ExiAcc | String(001) | Sim | Exibir Tipo de Acesso no Monitoramento On-Line |
| CorAcc | Number(009,0) | Sim | Cor do Tipo de Acesso no Monitoramento On-Line |
| BeeAcc | String(001) | Sim | Beep para o Tipo de Acesso no Monitoramento On-Line |
| VisCam | String(001) | Sim | Visualiza Câmera CFTV no Monitoramento do Acesso |
| IntMap | Number(005,0) | Sim | Intervalo em Minutos para Sinalização no A-Map |
| TipOcP | Number(003,0) | Sim | Tipo de incidente para a geração do incidente |
| ObsOcP | String(1500) | Sim | Descrição do incidente na portaria |
| GerOcp | String(001) | Sim | Gerar incidente na coleta de marcação de acesso |

---

## Chave Primária

- TipAcc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
