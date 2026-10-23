# R047DEF

## Descrição

Definições de Integração com o ERP

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CmpRef | Date | Não | Competência de Referência |
| RgrFor | Number(003,0) | Sim | Regra para cálculo do Código do Fornecedor |
| IntCcu | String(001) | Sim | Integrar Centro de Custos |
| FilSap | String(001) | Sim | Gerar Pendências pelas Filiais do ERP |
| FatCif | String(001) | Sim | Considera CIF na Fatura |
| RgrTit | Number(003,0) | Sim | Regra Integração Financeira - Integração Tasy |
| RgrCtb | Number(003,0) | Sim | Regra Integração Contábil - Integração Tasy |
| EmaLog | String(200) | Sim | E-mail para envio de log |
| FecInt | String(001) | Sim | Habilitar Fechamento Integração |
| IdeInt | String(010) | Sim | Identificador para Fechamento da Integração |

---

## Chave Primária

- CmpRef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
