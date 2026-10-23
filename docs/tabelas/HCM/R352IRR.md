# R352IRR

## Descrição

S-5501 - Informações de IRRF, consolidadas por Código de Receita

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Tipo de Período Apuração |
| NumPro | String(020) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqIrr | Number(009,0) | Não | Sequência |
| CodRec | Number(006,0) | Sim | Código de Receita |
| ValBas | Number(014,2) | Sim | Valor correspondente ao Código de Receita |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- NumPro
- SeqTab
- SeqIrr

---

## Índices

### R352IRRIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
