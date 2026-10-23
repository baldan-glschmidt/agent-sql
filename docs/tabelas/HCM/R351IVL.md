# R351IVL

## Descrição

S-2501 - eSocial - Informações de valores relacionados à não retenção de tributos ou a depósitos judiciais

---

## Resumo

- Campos: 17
- Chave Primária: 10 campo(s)
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
| SeqIvl | Number(009,0) | Não | Sequência Valores não relacionados a não retenção de tributos ou depósitos judiciais |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| VlrNre | Number(015,2) | Sim | Valor da retenção que deixou de ser efetuada em função de processo administrativo ou judicial |
| VlrDju | Number(015,2) | Sim | Valor do depósito judicial em função de processo administrativo ou judicial |
| VlrAnc | Number(015,2) | Sim | Valor da compensação relativa ao ano calendário em função de processo judicial |
| VlrAnt | Number(015,2) | Sim | Valor da compensação relativa a anos anteriores em função de processo judicial |
| VlrSus | Number(015,2) | Sim | Valor do rendimento com exigibilidade suspensa |
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

---

## Índices

### R351IVLIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
