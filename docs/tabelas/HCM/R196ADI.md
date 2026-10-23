# R196ADI

## Descrição

BS - Adicionais Tarefeiros

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Colaborador |
| DatAdi | Date | Não | Data Adicional |
| CodAdi | Number(004,0) | Não | Código do Adicional |
| QtdAdi | Number(011,2) | Sim | Quantidade do Adicional |
| VlrAdi | Number(011,2) | Sim | Valor do Adicional |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAdi
- CodAdi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R196ADI_004

**Tabela:** R194TAD

| Origem | Destino |
|--------|---------|
| CodAdi | CodAdi |

