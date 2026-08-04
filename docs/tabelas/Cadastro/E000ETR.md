# E000ETR

## Descrição

Tabelas - Integrações - Exclusão de Títulos a Receber

---

## Resumo

- Campos: 5
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
| NumTit | String(015) | Não | Número do título a receber |
| CodTpt | String(003) | Não | Código de Tipo de Título |

---

## Chave Primária

- SeqInt

---

## Índices

### E000ETRIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- NumTit
- CodTpt

---

## Relacionamentos

Nenhum relacionamento cadastrado.
