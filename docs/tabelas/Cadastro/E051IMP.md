# E051IMP

## Descrição

Tabelas - Impostos - Tabela de Impostos

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
| CodImp | String(003) | Não | Código do imposto |
| DesImp | String(030) | Não | Descrição do imposto |
| TipImp | Number(002,0) | Não | Tipo de imposto |
| ImpIcs | String(003) | Sim | Código do imposto substituto / presumido secundário correspondente |
| ImpDie | String(003) | Sim | Código do imposto diferença interestadual / IR adicional correspondente |
| DevRet | String(001) | Sim | Indicativo se o imposto é devido ou retido |
| CodReg | Number(004,0) | Sim | Código da regra de cálculo do imposto |
| GruFis | String(001) | Não | Indicativo se o imposto é calculado por grupo fiscal |
| ImpRtr | String(003) | Sim | Código do imposto por responsabilidade tributária |
| TipAbt | String(001) | Sim | Tipo de abatimento |
| SitReg | String(001) | Sim | Situação do registro |
| AneSin | Number(002,0) | Sim | Número do anexo do simples nacional |
| MoeUpf | String(003) | Sim | Código da moeda da Unidade Padrão Fiscal |
| RefUpf | String(001) | Não | Tipo de período do cálculo do imposto |

---

## Chave Primária

- CodImp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
