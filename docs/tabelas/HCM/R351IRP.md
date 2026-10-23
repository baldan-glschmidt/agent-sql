# R351IRP

## Descrição

S-2500 - eSocial - Informações da remuneração e periodicidade de pagamento

---

## Resumo

- Campos: 13
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| NumPro | String(020) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| CpfTra | Number(011,0) | Não | Número do CPF do trabalhador |
| IdeSeq | Number(005,0) | Não | Sequência parcial |
| SeqPtb | Number(009,0) | Não | Sequência |
| SeqIct | Number(009,0) | Não | Sequência |
| SeqIrp | Number(009,0) | Não | Sequência |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| DatRem | Date | Sim | Data a partir da qual as informações de remuneração e periodicidade de pagamento estão vigentes |
| SalBas | Number(015,2) | Sim | Salário base do trabalhador, correspondente à parte fixa da remuneração |
| UniPag | Number(001,0) | Sim | Unidade de pagamento da parte fixa da remuneração |
| DscSal | String(999) | Sim | Descrição do salário por tarefa ou variável e como este é calculado |

---

## Chave Primária

- NumEmp
- FilEmp
- NumPro
- CpfTra
- IdeSeq
- SeqPtb
- SeqIct
- SeqIrp

---

## Índices

### R351IRPIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
