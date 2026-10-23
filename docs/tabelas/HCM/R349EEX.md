# R349EEX

## Descrição

S-5002 - eSocial - Endereço do beneficiário residente ou domiciliado no exterior

---

## Resumo

- Campos: 17
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqIdv | Number(009,0) | Não | Sequência |
| SeqExt | Number(009,0) | Não | Sequência |
| SeqEex | Number(009,0) | Não | Sequência |
| DesLog | String(080) | Sim | Descrição do logradouro |
| NroLog | String(010) | Sim | Número do logradouro |
| ComLog | String(030) | Sim | Complemento do logradouro |
| NomBai | String(060) | Sim | Nome do bairro/distrito |
| NomCid | String(040) | Sim | Nome da cidade |
| NomEst | String(040) | Sim | Nome da província/estado |
| CodPos | String(012) | Sim | Código de Endereçamento Postal |
| NumTel | String(015) | Sim | Número do telefone |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqIdv
- SeqExt
- SeqEex

---

## Índices

### R349EEXIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
