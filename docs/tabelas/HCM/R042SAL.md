# R042SAL

## Descrição

HomologNet - Salários

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| MesAno | Date | Não | Mes/Ano do Salário |
| TipFor | Number(001,0) | Sim | Formação do Salário |
| TipSal | Number(001,0) | Sim | Tipo de Salário Fixo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- MesAno

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R042SAL_002

**Tabela:** R042COL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

