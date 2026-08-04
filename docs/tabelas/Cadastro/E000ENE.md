# E000ENE

## Descrição

Tabelas - Integrações - Cancelamento notas fiscais de entrada

---

## Resumo

- Campos: 8
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
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| DatCan | Date | Sim | Data de cancelamento da nota de entrada |
| AcaNfc | Number(001,0) | Não | Ação da pendência de nota fiscal de entrada. |

---

## Chave Primária

- SeqInt

---

## Índices

### E000ENEIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- AcaNfc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
