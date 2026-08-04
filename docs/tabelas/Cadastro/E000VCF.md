# E000VCF

## Descrição

Tabelas - Integrações - Verbas de compra das filiais

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
| VcfCpr | Date | Não | Mês e ano da competência para controle de verba de compra da filial |
| CodNtg | Number(004,0) | Não | Natureza de gasto para controle de verba de compra da filial |

---

## Chave Primária

- SeqInt

---

## Índices

### E000VCFIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodNtg
- VcfCpr

---

## Relacionamentos

Nenhum relacionamento cadastrado.
