# E000TCR

## Descrição

Tabelas - Integrações - Títulos a Receber

---

## Resumo

- Campos: 6
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
| NumTit | String(015) | Não | Número do título a receber |
| CodTpt | String(003) | Não | Código do tipo de título a receber |
| IdeUni | String(050) | Sim | Identificador único alfanumérico |

---

## Chave Primária

- SeqInt

---

## Índices

### E000TCRIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- NumTit
- CodTpt

### E000TCRIndice2

**Tipo:** Não unico

Campos:
- IdeUni

---

## Relacionamentos

Nenhum relacionamento cadastrado.
