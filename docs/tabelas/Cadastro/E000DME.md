# E000DME

## Descrição

Tabelas - Integrações - Definições de Metas

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodPme | Number(004,0) | Não | Códido período meta |
| CptPme | Date | Não | Mês e ano base da meta |
| ProSer | String(001) | Não | Solicitação de produto ou serviço |
| SeqDme | Number(004,0) | Não | Sequência da definição da meta |

---

## Chave Primária

- SeqInt

---

## Índices

### E000DMEIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- SeqDme
- ProSer
- CptPme
- CodPme

---

## Relacionamentos

Nenhum relacionamento cadastrado.
