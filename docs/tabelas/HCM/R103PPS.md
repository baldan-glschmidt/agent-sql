# R103PPS

## Descrição

PSS - Participantes do grupo

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodPss | Number(003,0) | Não | Código do grupo de PSS |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador Participante |
| DatEnt | Date | Não | Data de entrada do participante no grupo |
| DatSai | Date | Sim | Data de saída do participante do grupo |
| IndLid | String(001) | Sim | Define se o participante é líder do grupo |

---

## Chave Primária

- NumEmp
- CodPss
- TipCol
- NumCad
- DatEnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R103PPS_001

**Tabela:** R103GPS

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPss | CodPss |

