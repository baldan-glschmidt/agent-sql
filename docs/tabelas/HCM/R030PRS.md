# R030PRS

## Descrição

Processos Judiciais - Suspensão de Exigibilidade de Tributos e FGTS

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodPro | Number(009,0) | Não | Número do Processo/Benefício |
| DatIni | Date | Não | Data de Alteração |
| CodSus | Number(014,0) | Não | Código Suspensão |
| TipDec | Number(002,0) | Sim | Suspensão da Exigibilidade |
| DatDec | Date | Sim | Data da Decisão do Processo |
| DepInt | String(001) | Sim | Depósito do Montante Integral |
| CodPrc | Number(007,0) | Não | Código da Ação |
| ObsSus | String(100) | Sim | Observação da Suspensão de Exigibilidade |

---

## Chave Primária

- NumEmp
- CodPro
- DatIni
- CodSus

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
