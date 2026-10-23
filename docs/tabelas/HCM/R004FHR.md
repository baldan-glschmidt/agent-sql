# R004FHR

## Descrição

Faixas de Marcação do Horário

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodHor | Number(004,0) | Não | Código do Horário |
| SeqFai | Number(002,0) | Não | Sequência da Faixa de Marcação |
| IniAce | Number(005,0) | Sim | Início da Faixa p/ Marcação de Acesso |
| FimAce | Number(005,0) | Sim | Fim da Faixa p/ Marcação de Acesso |
| IniPto | Number(005,0) | Sim | Início da Faixa p/ Marcação de Ponto |
| FimPto | Number(005,0) | Sim | Fim da Faixa p/ Marcação de Ponto |

---

## Chave Primária

- CodHor
- SeqFai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R004FHR_000

**Tabela:** R004HOR

| Origem | Destino |
|--------|---------|
| CodHor | CodHor |

