# R005AOC

## Descrição

Funcionários Envolvidos em Acidentes

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
| CodAci | Number(005,0) | Não | Código do Acidente |
| NumEmp | Number(004,0) | Não | Empresa do Colaborador |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| ColFer | String(001) | Sim | Colaborador Ferido |

---

## Chave Primária

- CodAci
- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R005AOC_000

**Tabela:** R005ACI

| Origem | Destino |
|--------|---------|
| CodAci | CodAci |

