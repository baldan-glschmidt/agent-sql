# E081FPE

## Descrição

Tabelas - Tabela de Preços de Frete - Preços por Peso

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
| PesIni | Number(014,5) | Não | Peso Inicial |
| PesFim | Number(014,5) | Sim | Peso Final |
| VlrFre | Number(015,2) | Sim | Valor do Frete |
| PerFre | Number(005,2) | Sim | % Frete |

---

## Chave Primária

- CodEmp
- CodTab
- DatIni
- PesIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
