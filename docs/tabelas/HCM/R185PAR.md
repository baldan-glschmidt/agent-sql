# R185PAR

## Descrição

Orçamento Individual - Definições Gerais

---

## Resumo

- Campos: 18
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| AnoBas | Number(004,0) | Não | Ano base de cálculo do orçamento |
| SitMan | String(001) | Sim | Manutenção da quadro oficial bloqueada |
| IteFer | Number(003,0) | Sim | Item de orçamento destinado ao cálculo de férias |
| IteAbo | Number(003,0) | Sim | Item de orçamento destinado ao cálculo do abono de férias |
| TerFer | Number(003,0) | Sim | Item de orçamento destinado ao cálculo de 1/3 das férias |
| TerAbo | Number(003,0) | Sim | Item de orçamento destinado ao cálculo de 1/3 do Abono de Férias |
| AdtDec | Number(003,0) | Sim | Item de orçamento destinado ao cálculo do Adto 13° Salário |
| DecTer | Number(003,0) | Sim | Item de orçamento destinado ao cálculo do 13° Salário |
| CodRe1 | Number(003,0) | Sim | Item de orçamento destinado ao cálculo da base |
| CodRe2 | Number(003,0) | Sim | Item de orçamento destinado ao cálculo das diferenças de Férias |
| CodRe3 | Number(003,0) | Sim | Item de orçamento destinado ao cálculo do salário mensal |
| LogDet | String(001) | Sim | Visualização de log detalhado |
| PrvFer | Number(003,0) | Sim | Item de orçamento destinado ao cálculo de provisão de férias |
| AjuFer | Number(003,0) | Sim | Item de orçamento destinado ao cálculo de ajuste de provisão de férias |
| Prv13s | Number(003,0) | Sim | Item de orçamento destinado ao cálculo de provisão de 13° salário |
| Aju13s | Number(003,0) | Sim | Item de orçamento destinado ao cálculo de ajuste de provisão de 13° salário |
| BasPrv | Number(001,0) | Sim | Definição da base de cálculo da provisão de férias |

---

## Chave Primária

- NumEmp
- AnoBas

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R185PAR_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

