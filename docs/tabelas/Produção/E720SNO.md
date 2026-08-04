# E720SNO

## Descrição

Ficha - Roteiro - Seqüência de Narrativas p/ Operações (Instruções)

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodNof | String(006) | Não | Código da Narrativa técnica p/ operação (Instruções de trabalho) |
| SeqSno | Number(004,0) | Não | Número seqüencial da narrativa |
| ObsSno | String(240) | Não | Texto narrativo sobre a instrução de trabalho na operação |
| EndSno | String(255) | Sim | Endereço (caminho) da Narrativa (para busca automática) quando a Narrativa é complementada por algum arquivo |
| DatAlt | Date | Sim | Data da geração/alteração |
| CodUsu | Number(010,0) | Sim | Usuário geração/alteração |

---

## Chave Primária

- CodEmp
- CodNof
- SeqSno

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
