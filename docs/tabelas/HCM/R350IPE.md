# R350IPE

## Descrição

S-1210 - eSocial - Informações dos pagamentos efetuados

---

## Resumo

- Campos: 14
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
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| SeqPrt | Number(009,0) | Não | Sequência |
| SeqIpe | Number(009,0) | Não | Sequência |
| DatPag | Date | Sim | Data Pagamento |
| TipPag | Number(001,0) | Sim | Tipo Pagamento |
| PerRef | Date | Sim | Competência de Pagamento |
| IdeDem | String(030) | Sim | Identificador para demonstrativo de pagamento |
| ValLiq | Number(014,2) | Sim | Valor Líquido recebido pelo trabalhador |
| ResBra | String(001) | Sim | Beneficiário é residente no Brasil |
| CodPai | Number(003,0) | Sim | Código do país de residência para fins fiscais, quando no exterior, conforme Tabela 06 |
| PidExc | String(050) | Sim | Identificador da execução da pendência |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqPrt
- SeqIpe

---

## Índices

### R350IPEIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
