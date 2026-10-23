# R104REC

## Descrição

JR - Autor(Pessoa Física)

---

## Resumo

- Campos: 13
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodPrc | Number(007,0) | Não | Código da Ação |
| EmpAut | Number(004,0) | Não | Empresa do autor |
| TipCol | Number(001,0) | Não | Tipo do colaborador autor |
| NumCad | Number(009,0) | Não | Código do colaborador autor |
| CodFil | Number(006,0) | Sim | Código da filial |
| PerIni | Date | Sim | Período de início do direito |
| PerFim | Date | Sim | Período de fim de direito |
| QtdPar | Number(002,0) | Sim | Quantidade de parcelas para cumprimento da sentença |
| TipPer | Number(001,0) | Sim | Tipo de periodicidade(1-Dias, 2-Meses) |
| IntPer | Number(002,0) | Sim | Intervalo entre as parcelas(em meses ou dias) |
| IniPag | Date | Sim | Competência de início do pagamento |
| TipCon | Number(001,0) | Sim | Tipo de contrato a que se refere o processo judicial ou a demanda submetida à CCP ou ao NINTER |

---

## Chave Primária

- NumEmp
- CodPrc
- EmpAut
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104REC_001

**Tabela:** R104PRJ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |

### IR_R104REC_004

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| EmpAut | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

