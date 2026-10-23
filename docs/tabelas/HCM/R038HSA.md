# R038HSA

## Descrição

Histórico Salarial

---

## Resumo

- Campos: 21
- Chave Primária: 5 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| DatAlt | Date | Não | Data da Alteração |
| SeqAlt | Number(002,0) | Não | Sequência do reajuste |
| CodMot | Number(003,0) | Sim | Motivo da Alteração |
| CodEst | Number(004,0) | Sim | Código da Estrutura Salarial |
| ValSal | Number(013,4) | Sim | Salário Atual |
| CplSal | Number(013,4) | Sim | Valor Complementar ao Salário |
| TipSal | Number(001,0) | Sim | Tipo do Salário |
| TipEst | Number(001,0) | Sim | Tipo de Estrutura |
| ClaSal | String(005) | Sim | Classe Salarial |
| NivSal | String(005) | Sim | Nível Salarial |
| PerDes | Number(005,2) | Sim | Percentual Desempenho |
| PerRea | Number(008,5) | Sim | % de Reajuste Concedido |
| StaHis | Number(001,0) | Sim | Status do Histórico |
| CodIdm | Number(003,0) | Sim | Código da Tabela de Índices |
| SalEst | Number(013,4) | Sim | Salário atual em moeda estrangeira |
| CplEst | Number(013,4) | Sim | Valor Complementar ao Salário em moeda estrangeira |
| DatDis | Date | Sim | Data Fechamento Dissídio |
| USU_ForFai | String(001) | Sim | Salario Fora de Faixa? (Classe/Nivel) |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt
- SeqAlt

---

## Índices

### R038HSAIndice2

**Tipo:** Não unico

Campos:
- StaHis
- DatAlt

### R038HSAIndice3

**Tipo:** Não unico

Campos:
- CodMot

---

## Relacionamentos

### IR_R038HSA_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R038HSA_005

**Tabela:** R076MOT

| Origem | Destino |
|--------|---------|
| CodMot | CodMot |

