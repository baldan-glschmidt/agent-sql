# R030EFE

## Descrição

Filial - Órgão Público - ENTE Federativo

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| DatAlt | Date | Não | Data Alteração |
| TipPub | Number(001,0) | Não | Tipo Público |
| DesLei | String(050) | Sim | Lei Enquadramento |
| PerSeg | Number(005,2) | Sim | % Contrib. Segurado |
| PerNor | Number(005,2) | Sim | % Contrib. Normal |
| PerSup | Number(005,2) | Sim | % Contrib. Suplementar |

---

## Chave Primária

- NumEmp
- CodFil
- DatAlt
- TipPub

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030EFE_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

