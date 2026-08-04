# E000REZ

## Descrição

Tabelas - Integrações - Reduções Z

---

## Resumo

- Campos: 16
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodEqu | Number(003,0) | Não | Código do equipamento fiscal da redução Z |
| CroEcf | Number(006,0) | Não | Cont. de Reinício de Operação do ECF |
| DatRef | Date | Não | Data de referência da redução Z |
| NumMar | Number(006,0) | Sim | Número do mapa resumo |
| NumRez | Number(006,0) | Não | Número da redução Z |
| VlrGtf | Number(015,2) | Sim | Gran total do final do dia da redução Z |
| VlrBru | Number(015,2) | Sim | Valor bruto da redução Z |
| VlrDsc | Number(015,2) | Sim | Valor dos descontos da redução Z |
| VlrCan | Number(015,2) | Sim | Valor dos cancelamentos da redução Z |
| VlrSer | Number(015,2) | Sim | Valor dos serviços da redução Z |
| VlrGti | Number(015,2) | Sim | Gran total do início do dia da redução Z |
| VlrAcr | Number(015,2) | Sim | Valor dos acréscimos da redução Z |
| ConRei | Number(003,0) | Sim | Valor acumulado no contador de reinício de operação |
| CooRed | Number(006,0) | Sim | Número do cont. de ordem de ope. último documento emitido (COO da Redução Z) |

---

## Chave Primária

- CodEmp
- CodFil
- CodEqu
- CroEcf
- DatRef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
