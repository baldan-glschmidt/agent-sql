# E070VCF

## Descrição

Cadastros - Filiais - Verbas de Compra por Competência

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| VcfCpr | Date | Não | Mês e ano da competência para controle de verba de compra da filial |
| CodNtg | Number(004,0) | Não | Natureza de gasto para controle de verba de compra da filial |
| VlrVcf | Number(015,2) | Sim | Verba de compra estabelecida para a competência na filial |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| SitVer | String(001) | Não | Situação da verba de compra por competência |

---

## Chave Primária

- CodEmp
- CodFil
- VcfCpr
- CodNtg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
