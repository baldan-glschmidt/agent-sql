# R142ANA

## Descrição

Análise Diagnósticos Treinamento

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDia | Number(009,0) | Não | Código do Diagnóstico |
| DatAna | Date | Sim | Data da Análise |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo de Colaborador Responsável |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador Responsável |
| CodIdm | Number(003,0) | Sim | Código do Índice |
| CusPro | Number(011,2) | Sim | Custo Provável |
| DesAna | String(250) | Sim | Descrição da Análise |

---

## Chave Primária

- CodDia

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R142ANA_000

**Tabela:** R142DIA

| Origem | Destino |
|--------|---------|
| CodDia | CodDia |

