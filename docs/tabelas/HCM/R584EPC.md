# R584EPC

## Descrição

Manutenção do Inventário de Riscos - GHEs - Riscos - EPCs

---

## Resumo

- Campos: 9
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodInv | Number(007,0) | Não | Código do Inventário de Riscos |
| NumAmb | Number(007,0) | Não | Código do Ambiente de Trabalho |
| DatInv | Date | Não | Data do Inventário de Riscos |
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Não | Código do GHE - Grupo Homogêneo de Exposição |
| SeqRis | Number(006,0) | Não | Sequência do risco |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipEqp | Number(003,0) | Não | Código Tipo de Equipamento |
| CodEqp | Number(006,0) | Não | Código do Equipamento |

---

## Chave Primária

- CodInv
- NumAmb
- DatInv
- CodPRA
- CodGHE
- SeqRis
- NumEmp
- TipEqp
- CodEqp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R584EPC_005

**Tabela:** R584RIS

| Origem | Destino |
|--------|---------|
| CodInv | CodInv |
| NumAmb | NumAmb |
| DatInv | DatInv |
| CodPRA | CodPRA |
| CodGHE | CodGHE |
| SeqRis | SeqRis |

### IR_R584EPC_008

**Tabela:** R098EQP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipEqp | TipEqp |
| CodEqp | CodEqp |

