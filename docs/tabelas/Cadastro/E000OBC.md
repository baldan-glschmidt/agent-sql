# E000OBC

## Descrição

Tabelas - Integrações - Observações do Cliente

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodCli | Number(009,0) | Não | Código do cliente |
| SeqObs | Number(004,0) | Não | Sequência da observação |

---

## Chave Primária

- SeqInt

---

## Índices

### E000OBCIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodCli
- SeqObs

### E000OBCEmpresaFilial

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil

---

## Relacionamentos

Nenhum relacionamento cadastrado.
