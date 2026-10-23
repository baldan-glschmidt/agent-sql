# R460TSO

## Descrição

Portal Web - SAC - Trâmite da Solicitação

---

## Resumo

- Campos: 10
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSol | Number(009,0) | Não | Código da Solicitação |
| SeqTra | Number(003,0) | Não | Trâmite da Solicitação |
| DatTra | Date | Sim | Data do Trâmite |
| HorTra | Number(005,0) | Sim | Hora do Trâmite |
| DesTra | String(1000) | Sim | Descrição do Trâmite |
| TraCon | String(001) | Sim | Concluído |
| GerTra | String(001) | Sim | Gerador do Trâmite |
| NumEmp | Number(004,0) | Sim | Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro |

---

## Chave Primária

- CodSol
- SeqTra

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
