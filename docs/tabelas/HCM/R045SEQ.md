# R045SEQ

## Descrição

Sequência de Cheques

---

## Resumo

- Campos: 17
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Codigo da Empresa do Empregado |
| SeqChe | Number(005,0) | Não | Sequência |
| DatEmi | Date | Sim | Data Emissão Sequência |
| OriChe | String(001) | Sim | Tipo de Origem |
| CodBan | Number(004,0) | Sim | Código Banco da Sequência |
| CodAge | Number(005,0) | Sim | Código da Agência da Sequência |
| PriChe | Number(007,0) | Sim | Primeiro Cheque da Sequência |
| ModPag | String(001) | Sim | Modo de Pagamento do Sálario |
| IncPen | String(001) | Sim | Incluir Pensão |
| PerCen | Number(005,2) | Sim | Percentual |
| MaxChe | Number(002,0) | Sim | Número Máximo de Cheques |
| ValMin | Number(011,2) | Sim | Valor Mínimo do Cheque |
| DatIni | Date | Sim | Data Início Férias e Rescisão |
| DatFim | Date | Sim | Data Término Férias e Rescisão |
| CheMin | String(001) | Sim | Cheques no Valor Mínimo |
| JunCal | String(001) | Sim | Juntar Cálculos |
| OrdChe | String(001) | Sim | Ordem Cheques |

---

## Chave Primária

- NumEmp
- SeqChe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R045SEQ_005

**Tabela:** R012AGE

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |
| CodAge | CodAge |

