# R126SBS

## Descrição

Requisições - Substituídos

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRqu | Number(009,0) | Não | Código Requisição |
| NumEmp | Number(004,0) | Não | Empresa Requisitante |
| TipCol | Number(001,0) | Não | Tipo de Colaborador Substituído |
| NumCad | Number(009,0) | Não | Cadastro Colaborador Substituído |

---

## Chave Primária

- CodRqu
- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R126SBS_000

**Tabela:** R126RQU

| Origem | Destino |
|--------|---------|
| CodRqu | CodRqu |

### IR_R126SBS_003

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

