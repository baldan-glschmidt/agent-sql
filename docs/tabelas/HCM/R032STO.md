# R032STO

## Descrição

Serviços Contidos na Nota Fiscal - Serviço Tomado

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CmpPoe | Date | Não | Competência do Pagto O.Empresa |
| CodOem | Number(008,0) | Não | Código da Outra Empresa |
| SeqPoe | Number(003,0) | Não | Sequência do pagamento |
| NumIte | Number(003,0) | Não | Número do item contido na nota fiscal |
| TipSer | Number(002,0) | Sim | Tipo de serviço tomado |
| ValBru | Number(014,2) | Sim | Valor bruto |
| BasRet | Number(014,2) | Sim | Base de cálculo da retenção |

---

## Chave Primária

- NumEmp
- CodFil
- CmpPoe
- CodOem
- SeqPoe
- NumIte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R032STO_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R032STO_003

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

