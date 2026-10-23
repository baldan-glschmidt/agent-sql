# R038HIS

## Descrição

Histórico de Seguridade

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodOem | Number(008,0) | Não | Código da Outra Empresa |
| CodSeg | Number(004,0) | Não | Código de Seguridade |
| DatIni | Date | Não | Data de Início do Histórico de Administradora |
| PerSeg | Number(007,4) | Sim | % Seguridade |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodOem
- DatIni
- CodSeg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038HIS_003

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

### IR_R038HIS_004

**Tabela:** R026SEG

| Origem | Destino |
|--------|---------|
| CodSeg | CodSeg |

