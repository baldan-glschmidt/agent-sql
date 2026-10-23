# R151REG

## Descrição

Auditoria Registro de alterações

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqReg | Number(015,0) | Não | Sequência do resgistro |
| VerSeq | Number(010,0) | Não | Versão da alteração |
| NomTab | String(099) | Sim | Tabela que gerou o log |
| DatAtu | Date | Sim | Data de Alteração do Registro |
| HorAtu | Number(005,0) | Sim | Hora da Alteração do Registro |
| SegAtu | Number(002,0) | Sim | Segundos da Alteração do Registro |
| TipDoc | Number(001,0) | Sim | Tipo do documento do usuário |
| NumDoc | String(020) | Sim | Número do documento do usuário |
| NomUsu | String(040) | Sim | Nome do usuário que alterou o registro |
| CodUsu | Number(009,0) | Sim | Código do usuário que alterou o registro |
| LogReg | String(1999) | Sim | Log da alteração do registro |

---

## Chave Primária

- SeqReg
- VerSeq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
