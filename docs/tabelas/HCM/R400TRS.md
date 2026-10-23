# R400TRS

## Descrição

Registros a Serem Replicados

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatPen | Date | Não | Data da Pendência da Replicação |
| HorPen | Number(005,0) | Não | Hora da Pendência da Replicação |
| SeqPen | Number(005,0) | Não | Sequência da Pendência |
| CodTra | String(020) | Sim | Codigo da Transação |
| TabAlt | String(010) | Sim | Nome da Tabela do Registro a Ser Replicado |
| StrCha | String(100) | Sim | String Contendo a Chave do Registro a Ser Replicado |
| UsuBan | String(020) | Sim | Nome do Usuário do Banco Onde Foi Gerada a Transação |
| SerBan | String(020) | Sim | Serviço do Banco Onde Foi Gerada a Transação |
| OpeRep | String(001) | Sim | Operação de Replicação (I,U,D) |
| StaPro | String(001) | Sim | Status do Processamento |

---

## Chave Primária

- DatPen
- HorPen
- SeqPen

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
