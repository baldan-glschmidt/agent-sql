# E069CMC

## Descrição

Convênios - Movimentos de Conta Convênio

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodCli | Number(009,0) | Não | Código do Cliente |
| CodCnv | Number(004,0) | Não | Código do convênio |
| VlrMov | Number(015,2) | Sim | Valor do movimento da conta convênio |
| ObsCmc | String(099) | Sim | Observação do movimento de conta convênio |
| TipCmc | Number(002,0) | Sim | Tipo do movimento da conta convênio |
| OriCmc | Number(002,0) | Sim | Origem do movimento da conta convênio |
| DatMov | Date | Sim | Data do movimento da conta convênio |
| UsuMov | Number(010,0) | Sim | Usuário responsável pelo movimento da conta convênio |
| HorMov | Number(005,0) | Sim | Hora da geração do movimento da conta convênio |

---

## Chave Primária

- IdeUni

---

## Índices

### E069CMCIndice1

**Tipo:** Não unico

Campos:
- CodCli
- CodCnv

---

## Relacionamentos

Nenhum relacionamento cadastrado.
