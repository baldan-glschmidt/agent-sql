# R351PRE

## Descrição

S-2501 - eSocial - Informações de processos relacionados à não retenção de tributos ou a depósitos judiciais

---

## Resumo

- Campos: 13
- Chave Primária: 9 campo(s)
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
| SeqPre | Number(009,0) | Não | Sequência Processo relacionados a não retenção de tributos |
| TipPro | Number(001,0) | Não | Código Correspondente ao Tipo do Processo |
| NumPrb | String(021) | Não | Número do Processo/Benefício |
| CodSus | Number(014,0) | Não | Código Suspensão |
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

---

## Índices

### R351PREIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
