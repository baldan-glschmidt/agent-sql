# E000LOG

## Descrição

Cadastros - Log Genérico

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NomTab | String(032) | Não | Tabela monitorada |
| SeqLog | Number(009,0) | Não | Sequência do log |
| TipLog | String(001) | Não | Tipo de log |
| ChaTab | String(250) | Sim | Chave do registro monitorado |
| NomFrm | String(030) | Sim | Identificação do nome do formulário que foi monitorado |
| DesLog | String(9999) | Sim | Apresenta o conteúdo do registro alterado |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- NomTab
- SeqLog
- TipLog

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
