# R351IRR

## Descrição

S-2501 - eSocial - Informações de Imposto de Renda Retido na Fonte

---

## Resumo

- Campos: 16
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| NumPro | String(020) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| PerApu | Date | Não | Mês/ano em que é devida a obrigação de pagar a parcela prevista no acordo/sentença |
| SeqTpt | Number(009,0) | Não | Sequência |
| SeqPar | Number(005,0) | Não | Sequência parcial |
| SeqItp | Number(009,0) | Não | Sequência Trabalhador |
| SeqIrr | Number(009,0) | Não | Sequência Informações de Imposto de Renda Retido na Fonte |
| CodRec | Number(006,0) | Sim | CR relativo a Imposto de Renda Retido na Fonte |
| ValRec | Number(014,2) | Sim | Valor relativo ao Imposto sobre a renda retido na fonte para o código de receita - rendimento mensal |
| DesRra | String(050) | Sim | Descrição dos Rendimentos Recebidos Acumuladamente (RRA) |
| QtdMes | Number(004,1) | Sim | Número de meses relativo aos Rendimentos Recebidos Acumuladamente (RRA) |
| VlrCus | Number(015,2) | Sim | Valor das despesas com custas judiciais |
| VlrAdv | Number(015,2) | Sim | Valor das despesas com advogados |
| VlrC13 | Number(015,2) | Sim | Valor relativo ao Imposto sobre a renda retido na fonte para o código de receita - 13º Salário |
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

---

## Índices

### R351IRRIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
