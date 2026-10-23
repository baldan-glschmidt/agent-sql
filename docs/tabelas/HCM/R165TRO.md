# R165TRO

## Descrição

BS - Troca de Trajetos

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatTro | Date | Não | Data Troca |
| CodTra | Number(006,0) | Sim | Código do Trajeto |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatTro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R165TRO_004

**Tabela:** R165TRA

| Origem | Destino |
|--------|---------|
| CodTra | CodTra |

