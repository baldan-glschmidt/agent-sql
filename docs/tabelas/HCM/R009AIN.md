# R009AIN

## Descrição

Gestão de Incidentes - Agrupamento dos Incidentes

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodGIn | Number(003,0) | Não | Código da Definição de Gestão de Incidentes |
| DatAgr | Date | Não | Data Inicial do Agrupamento |
| SeqAgr | Number(002,0) | Não | Sequencia do Agrupamento |
| DesAgr | String(040) | Sim | Descrição do Agrupamento |
| DatFim | Date | Sim | Data Final do Agrupmaneto |
| AInDia | String(001) | Sim | Agrupa Incidentes por Dia |
| AInQtd | Number(003,0) | Sim | Agrupa Incidentes por Quantidade |

---

## Chave Primária

- CodGIn
- DatAgr
- SeqAgr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
