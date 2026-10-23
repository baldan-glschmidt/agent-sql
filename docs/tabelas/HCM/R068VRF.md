# R068VRF

## Descrição

Valores Refeição

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodRef | Number(003,0) | Não | Código da Refeição |
| DatAlt | Date | Não | Data de Alteração do Valor da Refeição |
| ValNor | Number(013,4) | Sim | Valor Normal da Refeição |
| ValSRe | Number(013,4) | Sim | Valor sem a Reserva da Refeição |
| ValSCo | Number(013,4) | Sim | Valor sem o Consumo da Refeição |
| ValSub | Number(013,4) | Sim | Valor da Refeiçao Subsidiado pela Empresa |
| ValREm | Number(013,4) | Sim | Valor da Refeição para a Empresa |

---

## Chave Primária

- NumEmp
- CodRef
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R068VRF_001

**Tabela:** R068TRF

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodRef | CodRef |

