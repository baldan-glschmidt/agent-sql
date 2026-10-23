# R351DSU

## Descrição

S-2501 - eSocial - Detalhamento das deduções com exigibilidade suspensa

---

## Resumo

- Campos: 16
- Chave Primária: 11 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| NumPro | String(021) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| PerApu | Date | Não | Mês/ano em que é devida a obrigação de pagar a parcela prevista no acordo/sentença |
| SeqTpt | Number(009,0) | Não | Sequência |
| SeqPar | Number(005,0) | Não | Sequência parcial |
| SeqItp | Number(009,0) | Não | Sequência Trabalhador |
| SeqIrr | Number(009,0) | Não | Sequência Informações de Imposto de Renda Retido na Fonte |
| SeqPre | Number(009,0) | Não | Sequência Processos relacionados à não retenção de tributos |
| SeqIvl | Number(009,0) | Não | Sequência Valores não relacionados a não retenção de tributos ou depósitos judiciais |
| SeqDsu | Number(009,0) | Não | Sequência Dedução Exigibilidade Suspensa |
| IndTde | Number(001,0) | Não | Indicativo do tipo de dedução |
| VlrDsu | Number(015,2) | Sim | Valor da dedução da base de cálculo do imposto de renda com exigibilidade suspensa |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| VlrRem | Number(015,2) | Sim | Valor da dedução relativa a dependentes ou a pensão alimentícia com exigibilidade suspensa |
| PidExc | String(050) | Não | Identificador da pendência para execução |

---

## Chave Primária

- NumEmp
- FilEmp
- NumPro
- PerApu
- SeqTpt
- SeqPar
- SeqItp
- SeqIrr
- SeqPre
- SeqIvl
- SeqDsu

---

## Índices

### R351DSUIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
