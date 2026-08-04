# E089DOC

## Descrição

Tabelas - Tipos de Documento

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodDoc | String(003) | Não | Código do tipo de documento para tesouraria |
| DesDoc | String(100) | Não | Descrição do documento para tesouraria |
| AbrDoc | String(010) | Não | Abreviatura do tipo de documento para tesouraria |
| CriRat | Number(001,0) | Não | Critério utilizado para rateio |
| CtaRdv | Number(007,0) | Sim | Conta contábil reduzida - 1 |
| CtaRcr | Number(007,0) | Sim | Conta contábil reduzida - 2 |
| CtaFdv | Number(007,0) | Sim | Conta contábil reduzida - 3 |
| CtaFcr | Number(007,0) | Sim | Conta contábil reduzida - 4 |

---

## Chave Primária

- CodEmp
- CodDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
