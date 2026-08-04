# E049AIR

## Descrição

Tabelas - Tributos - Alíquotas de Tributos Retidos

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| TipImp | Number(002,0) | Não | Tipo de imposto |
| MesAno | Date | Não | Mês e ano de competência |
| PerImp | Number(007,4) | Não | Percentual do imposto |
| UsuGer | Number(010,0) | Sim | Código do usuário responsável pelo geração do registro |
| DatGer | Date | Sim | Data de geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- TipImp
- MesAno
- PerImp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
