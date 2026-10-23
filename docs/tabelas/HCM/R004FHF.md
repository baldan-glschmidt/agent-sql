# R004FHF

## Descrição

Horários por empresa e filial

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodHor | Number(004,0) | Não | Código do Horário |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| SeqFai | Number(002,0) | Não | Sequência da Faixa de Marcação |
| IniAce | Number(005,0) | Sim | Início da Faixa p/ Marcação de Acesso |
| FimAce | Number(005,0) | Sim | Fim da Faixa p/ Marcação de Acesso |
| IniPto | Number(005,0) | Sim | Início da Faixa p/ Marcação de Ponto |
| FimPto | Number(005,0) | Sim | Fim da Faixa p/ Marcação de Ponto |

---

## Chave Primária

- CodHor
- NumEmp
- CodFil
- SeqFai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R004FHF_000

**Tabela:** R004HOR

| Origem | Destino |
|--------|---------|
| CodHor | CodHor |

