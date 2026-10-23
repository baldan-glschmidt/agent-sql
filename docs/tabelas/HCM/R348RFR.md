# R348RFR

## Descrição

eSocial - Conferência INSS - Código de Receita por Filial - Liminares RPA

---

## Resumo

- Campos: 14
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| PerApu | Date | Não | Período Apuração |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRec | Number(006,0) | Não | Código de Receita |
| PerCen | Number(006,4) | Não | Percentual |
| CodSer | Number(003,0) | Não | Código do Serviço |
| BaInSu | Number(014,2) | Sim | Base do Código de Receita suspenso |
| BasCon | Number(014,2) | Sim | Base do INSS - Empresa concomitante |
| BasOne | Number(016,4) | Sim | Base do INSS - Onerada |
| BasDes | Number(016,4) | Sim | Base do INSS - Desonerada |
| ValSup | Number(014,2) | Sim | Valor do Código de Receita suspenso |
| VaSuCa | Number(014,2) | Sim | Valor do Código de Receita suspenso calculado |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CodFil
- CodRec
- PerCen
- CodSer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
