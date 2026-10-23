# R050RIF

## Descrição

Receitas Base

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CmpRif | Date | Não | Competência Bases |
| PerRif | Number(002,0) | Não | Tipo Período Bases |
| CodBas | Number(002,0) | Não | Código da base |
| ValBas | Number(013,2) | Sim | Valor da Base de Cálculo |

---

## Chave Primária

- NumEmp
- CodFil
- CmpRif
- PerRif
- CodBas

---

## Índices

### R050RIFIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CodFil
- CodBas
- CmpRif
- PerRif

---

## Relacionamentos

### IR_R050RIF_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R050RIF_004

**Tabela:** R026BIF

| Origem | Destino |
|--------|---------|
| CodBas | CodBas |

