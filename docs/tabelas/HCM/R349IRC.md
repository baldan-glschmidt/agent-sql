# R349IRC

## Descrição

S-5002 - eSocial - Informações por categoria do trabalhador (versão 2.5)

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
| PerApu | Date | Não | Período Apuração |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqIrc | Number(009,0) | Não | Sequência |
| CodCat | Number(004,0) | Sim | Código da categoria |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| IndRes | String(001) | Sim | Indicativo se o beneficiário do pagamento é residente fiscal no Brasil |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqIrc

---

## Índices

### R349IRCIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
