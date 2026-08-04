# E085OCO

## Descrição

Cadastros - Clientes - Observações do Cooperado

---

## Resumo

- Campos: 11
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do cliente |
| SeqCoo | Number(009,0) | Não | Sequência do Cadastro de Cooperado |
| SeqOco | Number(009,0) | Não | Sequência da observação |
| TipOco | String(001) | Não | Tipo de Observação |
| ObsOco | String(250) | Sim | Texto da observação do cooperado |
| ResUsu | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatOco | Date | Sim | Data da observação |
| SolOco | String(250) | Sim | Solução proposta para observação apresentada |
| SolUsu | Number(010,0) | Sim | Usuário responsável pela solução proposta |
| SolDat | Date | Sim | Data da Solução |
| SitObs | String(001) | Não | Situação da Observação |

---

## Chave Primária

- CodCli
- SeqCoo
- SeqOco

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
