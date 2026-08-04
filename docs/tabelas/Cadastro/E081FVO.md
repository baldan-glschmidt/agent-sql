# E081FVO

## Descrição

Tabelas - Tabela de Preços de Frete - Preços por Volume

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
| CodTab | String(004) | Não | Código da tabela de preço frete |
| DatIni | Date | Não | Data início de validade da tabela de preço |
| VolIni | Number(011,2) | Não | Volume Inicial |
| VolFim | Number(011,2) | Não | Volume Final |
| VlrFre | Number(015,2) | Não | Valor do Frete |
| PerFre | Number(005,2) | Sim | % Frete |

---

## Chave Primária

- CodEmp
- CodTab
- DatIni
- VolIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
