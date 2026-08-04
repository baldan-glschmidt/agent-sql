# E000PCM

## Descrição

Tabelas - Integrações - Contas ou Centro de Custos

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
| CodMpc | Number(004,0) | Não | Código do Modelo de Plano |
| CtaRed | Number(009,0) | Não | Número reduzido da conta do modelo de plano |

---

## Chave Primária

- SeqInt

---

## Índices

### E000PCMIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodMpc
- CtaRed

---

## Relacionamentos

Nenhum relacionamento cadastrado.
