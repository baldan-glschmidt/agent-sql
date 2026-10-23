# R110HIP

## Descrição

Histórico de Impressão do Prontuário Clínico

---

## Resumo

- Campos: 15
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodFic | Number(009,0) | Não | Código Ficha Médica |
| DatImp | Date | Não | Data da Impressão |
| HorImp | Number(005,0) | Não | Hora da Impressão |
| CodAte | Number(006,0) | Sim | Código do atendente que imprimiu |
| NomSol | String(070) | Sim | Nome de quem solicitou a impressão |
| JusImp | String(500) | Sim | Justificativa para impressão do Prontuário Clínico |
| NumCpf | String(011) | Sim | CPF do solicitante informado junto com o nome |
| CodPes | Number(009,0) | Sim | Código da Pessoa solicitante |
| CodPos | Number(007,0) | Sim | Posto do responsável |
| PosLoc | Number(007,0) | Sim | Posto da impressão |
| ProEnt | String(001) | Sim | Indica se o prontuário foi entregue (Sim/Não) |
| QtdPag | Number(003,0) | Sim | Quantidade de página |
| DesFil | String(4000) | Sim | Filtros recibo prontuário |
| FusHor | Number(002,0) | Sim | Fuso Horário |

---

## Chave Primária

- NumEmp
- CodFic
- DatImp
- HorImp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110HIP_001

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

### IR_R110HIP_004

**Tabela:** R108TAT

| Origem | Destino |
|--------|---------|
| CodAte | CodAte |

### IR_R110HIP_009

**Tabela:** R110POS

| Origem | Destino |
|--------|---------|
| CodPos | CodPos |

### IR_R110HIP_010

**Tabela:** R110POS

| Origem | Destino |
|--------|---------|
| PosLoc | CodPos |

