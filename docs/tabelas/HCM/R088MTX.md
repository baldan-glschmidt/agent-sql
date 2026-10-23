# R088MTX

## Descrição

Movimentação de Táxis

---

## Resumo

- Campos: 18
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| DatSol | Date | Não | Data da Movimentação do Veículo Táxi |
| HorSol | Number(005,0) | Não | Hora da Movimentação do Veículo |
| SeqSol | Number(002,0) | Não | Sequência da Movimentação |
| CodTax | Number(004,0) | Sim | Código Taxista |
| PlaVei | String(010) | Sim | Placa do Veículo |
| DatSai | Date | Sim | Data da Saída do Veículo |
| HorSai | Number(005,0) | Sim | Hora da Saída do Veículo |
| DatRet | Date | Sim | Data de Retorno do Veículo |
| HorRet | Number(005,0) | Sim | Hora do Retorno Veículo |
| QtdQui | Number(006,0) | Sim | Quantidade de Km Rodados |
| IndIme | String(001) | Sim | Saída Imediata do Táxi |
| ValDsp | Number(011,2) | Sim | Valor Total Despesa da Corrida de Táxi |
| CodSol | Number(006,0) | Sim | Número da Movimentação de Táxis |
| StaMtx | Number(001,0) | Sim | Status da Movimentação de Táxi |
| MovAge | String(001) | Sim | Movimentação por Agenda |
| MotUso | Number(003,0) | Sim | Motivo Uso do Veículo |

---

## Chave Primária

- NumEmp
- CodFil
- DatSol
- HorSol
- SeqSol

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088MTX_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

