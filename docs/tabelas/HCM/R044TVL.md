# R044TVL

## Descrição

Tipos de Vales

---

## Resumo

- Campos: 21
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodVal | Number(004,0) | Não | Código do Vale |
| DesVal | String(025) | Sim | Descrição do Vale |
| CodEve | Number(004,0) | Sim | Código do Evento |
| TipTvl | String(001) | Sim | Indicador Tipo do Vale |
| BasTvl | String(001) | Sim | Tipo de Base |
| VlrVal | Number(011,2) | Sim | Valor do Vale |
| ValMin | Number(011,2) | Sim | Valor Mínimo do Vale |
| ValMax | Number(011,2) | Sim | Valor Máximo do Vale |
| CalDia | String(001) | Sim | Cálculo dos Dias |
| NroMax | Number(002,0) | Sim | Número Máximo de Vales |
| DesRcs | String(001) | Sim | Desconto do Vale na Rescisão |
| RgrEve | Number(003,0) | Sim | Regra para Cálculo do Evento de Vale |
| CodEvs | Number(004,0) | Sim | Evento para o Subsídio |
| RgrEvs | Number(003,0) | Sim | Regra do Evento de Subsídio |
| ForVal | Number(002,0) | Sim | Empresa Fornecedora de Vales |
| CodPrd | String(029) | Sim | Produto |
| ApuAfa | Number(001,0) | Sim | Afastamento Período Apuração |
| ConEso | String(001) | Sim | Considerar tipo de vale para o eSocial |
| TipWip | Number(002,0) | Sim | Tipo de Vale Wiipo |
| BolWip | Number(003,0) | Sim | Bolso Wiipo |

---

## Chave Primária

- TabEve
- CodVal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R044TVL_000

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |

