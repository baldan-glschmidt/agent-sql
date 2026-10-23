# R110HAA

## Descrição

Histórico de Aferição dos Audiômetros

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodAud | Number(003,0) | Não | Código do Audiômetro |
| DatAfe | Date | Não | Data da Aferição do Audiômetro |

---

## Chave Primária

- NumEmp
- CodAud
- DatAfe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110HAA_001

**Tabela:** R110AUD

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodAud | CodAud |

