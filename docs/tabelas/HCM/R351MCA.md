# R351MCA

## Descrição

S-2500 - eSocial - Informação do novo código de categoria e/ou da nova natureza da atividade

---

## Resumo

- Campos: 12
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
| SeqMca | Number(009,0) | Não | Sequência |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| CodCat | Number(004,0) | Sim | Código da categoria do trabalhador |
| NatAti | Number(001,0) | Sim | Código da natureza da atividade |
| DatMud | Date | Sim | Data a partir da qual foi reconhecida a nova categoria e/ou natureza da atividade |

---

## Chave Primária

- NumEmp
- FilEmp
- NumPro
- CpfTra
- IdeSeq
- SeqPtb
- SeqIct
- SeqMca

---

## Índices

### R351MCAIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
