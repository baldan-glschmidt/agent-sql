# R030EBA

## Descrição

Transformação de EBAS para Sociedade com fins lucrativos

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| DatAlt | Date | Não | Data Alteração |
| PerTra | Number(001,0) | Sim | Informe o percentual de contribuição social devida |

---

## Chave Primária

- NumEmp
- CodFil
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030EBA_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

