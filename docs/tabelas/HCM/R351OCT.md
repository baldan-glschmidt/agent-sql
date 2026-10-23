# R351OCT

## Descrição

S-2500 - eSocial - Observações do contrato de trabalho

---

## Resumo

- Campos: 10
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
| SeqOct | Number(009,0) | Não | Sequência |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| ObsCon | String(255) | Não | Observação relacionada ao contrato de trabalho |

---

## Chave Primária

- NumEmp
- FilEmp
- NumPro
- CpfTra
- IdeSeq
- SeqPtb
- SeqIct
- SeqOct

---

## Índices

### R351OCTIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
