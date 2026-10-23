# R013REP

## Descrição

Repositório de Integrações

---

## Resumo

- Campos: 8
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipInt | Number(002,0) | Sim | Tipo de integração com sistemas de terceiros |
| SeqInt | Number(008,0) | Sim | Sequência da Integração |
| DatHor | Number(014,6) | Sim | Data e hora da geração dos dados |
| UsuGer | Number(010,0) | Sim | código do usuário que executou a operação |
| NomTab | String(007) | Sim | Nome da tabela que foi alterada |
| ChaTab | String(250) | Sim | Chave da tabela alterada |
| TipAlt | String(001) | Sim | Tipo de operação executada na tabela |
| SitInt | Number(001,0) | Sim | Indica se os dados já foram exportados |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
