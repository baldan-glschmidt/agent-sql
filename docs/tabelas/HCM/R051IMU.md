# R051IMU

## Descrição

Informe/DIRF - Entidades Imunes/Isentas

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| AnoBas | Number(004,0) | Não | Ano |
| TipIns | Number(001,0) | Não | Código correspondente ao tipo de inscrição |
| NumIns | Number(015,0) | Não | Número de Inscrição |
| NomBen | String(060) | Sim | Nome do Beneficiário |

---

## Chave Primária

- NumEmp
- CodFil
- AnoBas
- TipIns
- NumIns

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R051IMU_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

