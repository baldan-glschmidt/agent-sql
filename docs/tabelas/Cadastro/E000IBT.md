# E000IBT

## Descrição

Tabelas - Integrações - Intenção de baixas de títulos C.Receber

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumTit | String(015) | Não | Número do título a receber |
| CodTpt | String(003) | Não | Código do tipo de título a receber |
| SeqIbt | Number(004,0) | Não | Seq. de intenção de baixa de título |
| VlrIbt | Number(011,2) | Sim | Valor de baixa do título |
| IdtIbt | String(020) | Sim | Identificação Baixa |
| IndIbt | String(001) | Sim | Indicativo se a baixa foi realizada |
| CodInt | Number(002,0) | Não | Código do sistema integrado |

---

## Chave Primária

- CodEmp
- CodFil
- NumTit
- CodTpt
- SeqIbt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
