# E440DEF

## Descrição

Tabelas - Notas Fiscais de Entrada - Defensivo Agrícola

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| SeqDef | Number(003,0) | Não | Sequência do defensivo agrícula |
| NumRec | String(030) | Sim | Número do Receituário |
| CpfTec | String(011) | Sim | Número do CPF do responsável técnico pela emissão do receituário |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- CodSnf
- NumNfc
- SeqDef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440DEF_002

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

### IR_E440DEF_003

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

