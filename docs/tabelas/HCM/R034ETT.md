# R034ETT

## Descrição

Informações do Estatutário

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| TipPro | Number(002,0) | Sim | Tipo Provimento |
| DatNom | Date | Sim | Data Nomeação |
| DatPos | Date | Sim | Data Posse |
| CodPro | Number(009,0) | Sim | Número do processo judicial |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034ETT_002

**Tabela:** R034CPL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

