# E044LOT

## Descrição

Cadastros - Lotes relacionados a distribuição de custo

---

## Resumo

- Campos: 12
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| NumLot | Number(009,0) | Não | Número do Lote |
| SitLot | Number(001,0) | Não | Situação do Lote |
| DatLot | Date | Não | Data do Lote |
| UsuLot | Number(010,0) | Sim | Identificador do usuário |
| NumTab | Number(009,0) | Não | Numero da Tabela de Competência Matriz de Distribuição de Custos |
| NumTrf | Number(009,0) | Não | Numero da Tabela da Matriz de Zeramento Contábil |
| NumMat | Number(009,0) | Não | Numero da Tabela de Competência Matriz de Distribuição de Gastos |
| CodFil | Number(005,0) | Não | Código da filial |
| SeqDis | Number(009,0) | Não | Sequência da Distribuição da Matriz |
| TipLot | String(001) | Não | Tipo de Lote Contábil |

---

## Chave Primária

- IdeUni

---

## Índices

### E044LOTIndice1

**Tipo:** Unico

Campos:
- CodEmp
- SeqDis
- NumLot
- TipLot

---

## Relacionamentos

Nenhum relacionamento cadastrado.
