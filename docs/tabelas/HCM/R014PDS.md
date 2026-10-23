# R014PDS

## Descrição

Proventos/Descontos p/ Sindicato

---

## Resumo

- Campos: 11
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| TipPds | Number(002,0) | Não | Tipo provento/desconto p/ sindicato |
| MesPds | Number(002,0) | Não | Mês provento/desconto p/ sindicato |
| TclSoc | String(001) | Sim | Forma de calcular o desconto p/ sócios |
| ValSoc | Number(011,2) | Sim | Percentual / Valor / Dias desconto p/ sócios |
| MinSoc | Number(011,2) | Sim | Valor Mínimo do desconto p/ sócios |
| TetSoc | Number(011,2) | Sim | Valor máximo do desconto p/ sócios |
| TclNso | String(001) | Sim | Forma de calcular o desconto p/ não sócios |
| ValNso | Number(011,2) | Sim | Percentual / Valor / Dias desconto p/ não sócios |
| MinNso | Number(011,2) | Sim | Valor Mínimo de desconto p/ não sócios |
| TetNso | Number(011,2) | Sim | Valor máximo de desconto p/ não sócios |

---

## Chave Primária

- CodSin
- TipPds
- MesPds

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R014PDS_000

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

