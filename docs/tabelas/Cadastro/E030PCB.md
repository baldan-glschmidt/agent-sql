# E030PCB

## Descrição

Cadastros - Bancos - Produtos Corresp.Bancário

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBan | String(003) | Não | Código do banco na Febraban |
| CodPcb | Number(003,0) | Não | Código do produto de Correspondente Bancário |
| DesPcb | String(050) | Sim | Descrição do produto de correspondente bancário |
| VlrCom | Number(008,2) | Sim | Valor de comissão para o produto |
| PerCom | Number(004,2) | Sim | Percentual de comissão do produto |
| PdtTef | Number(002,0) | Sim | Tipo de produto no sistema TEF |
| IdeTef | String(005) | Sim | Identificador deste produto no retorno do Tef |

---

## Chave Primária

- CodBan
- CodPcb

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
