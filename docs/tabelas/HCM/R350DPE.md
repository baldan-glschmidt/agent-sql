# R350DPE

## Descrição

S-1210 - eSocial - Detalhamento dos pagamentos efetuados

---

## Resumo

- Campos: 13
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| SeqPrt | Number(009,0) | Não | Sequência |
| SeqIpe | Number(009,0) | Não | Sequência |
| SeqDpe | Number(009,0) | Não | Sequência |
| PerRef | Date | Sim | Competência de Pagamento |
| IdeDem | String(030) | Sim | Identificador para demonstrativo de pagamento |
| PagTot | String(001) | Sim | Pagamento Total ou Parcial |
| ValLiq | Number(014,2) | Sim | Valor Líquido recebido pelo trabalhador |
| NumRec | String(040) | Sim | Recibo de retorno do arquivo que contém as informações contratuais |
| PidExc | String(050) | Sim | Identificador da execução da pendência |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqPrt
- SeqIpe
- SeqDpe

---

## Índices

### R350DPEIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
