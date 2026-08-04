# E043PPC

## Descrição

Controladoria - Percentual Plano de Contas Referencial

---

## Resumo

- Campos: 13
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| AbrFil | String(500) | Não | Lista de Abrangência de filiais |
| CodAfi | Number(004,0) | Não | Código do agrupamento de filiais |
| MesAno | Date | Não | Data de competência |
| CtaRed | Number(009,0) | Não | Número reduzido da conta da Empresa |
| PerGer | Number(011,8) | Sim | Percentual das contas gerais |
| PerRur | Number(011,8) | Sim | Percentual das contas rurais |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- AbrFil
- CodAfi
- MesAno
- CtaRed

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
