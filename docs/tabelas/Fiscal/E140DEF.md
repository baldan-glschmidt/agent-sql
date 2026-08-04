# E140DEF

## Descrição

Tabelas - Notas Fiscais de Saída - Defensivo Agrícula

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqDef | Number(003,0) | Não | Sequência do defensivo agrícula |
| NumRec | String(030) | Sim | Número do Receituário |
| CpfTec | String(011) | Sim | Número do CPF do responsável técnico pela emissão do receituário |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqDef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140DEF_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E140DEF_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

