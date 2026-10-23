# R349IDV

## Descrição

S-5002 - eSocial - Informações do demonstrativo de valores devidos

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
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
| PerRef | Date | Sim | Período de referência das informações |
| IdeDev | String(030) | Sim | Identificador atribuído pela fonte pagadora para o demonstrativo de valores devidos ao trabalhador |
| TipPag | Number(001,0) | Sim | Informar o evento de origem do pagamento |
| DatPag | Date | Sim | Informar a data de pagamento |
| CodCat | Number(004,0) | Sim | Código da categoria do trabalhador |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqIdv

---

## Índices

### R349IDVIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
