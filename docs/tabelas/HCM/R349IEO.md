# R349IEO

## Descrição

S-5013 - eSocial - Estabelecimento ou obra de construção civil

---

## Resumo

- Campos: 10
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
| TipFol | Number(001,0) | Não | Tipo Folha |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqIeo | Number(009,0) | Não | Sequência Identificação do Estabelecimento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição (CNPJ/CPF) - Obsoleto |
| CfjIns | String(014) | Sim | Número de inscrição (CNPJ/CPF) |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- TipFol
- SeqTab
- SeqIeo

---

## Índices

### R349IEOIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
