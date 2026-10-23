# R028EVL

## Descrição

Escalas Vale Transporte - linhas

---

## Resumo

- Campos: 14
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EscVtr | Number(005,0) | Não | Código da Escala |
| CodLin | Number(005,0) | Não | Código da Linha do VT |
| CalEvl | String(001) | Sim | Tipo de Cálculo da Linha |
| PasUte | Number(002,0) | Sim | Qtde de Passes em Dias Úteis |
| PasSab | Number(002,0) | Sim | Qtde de Passes aos Sábados |
| PasDom | Number(002,0) | Sim | Qtde de Passes aos Domingos |
| PasFer | Number(002,0) | Sim | Qtde de Passes em Feriados |
| PasFix | Number(003,0) | Sim | Qtde de Passes Fixos |
| PasSeg | Number(002,0) | Sim | Qtde de Passes às Segundas |
| PasTer | Number(002,0) | Sim | Qtde de Passes às Terças |
| PasQua | Number(002,0) | Sim | Qtde de Passes às Quartas |
| PasQui | Number(002,0) | Sim | Qtde de Passes às Quintas |
| PasSex | Number(002,0) | Sim | Qtde de Passes às Sextas |
| PasFol | Number(002,0) | Sim | Qtde de Passes em Folga |

---

## Chave Primária

- EscVtr
- CodLin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R028EVL_000

**Tabela:** R028EVT

| Origem | Destino |
|--------|---------|
| EscVtr | EscVtr |

### IR_R028EVL_001

**Tabela:** R028LVT

| Origem | Destino |
|--------|---------|
| CodLin | CodLin |

