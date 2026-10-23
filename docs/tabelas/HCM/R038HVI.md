# R038HVI

## Descrição

Histórico Vínculo

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAlt | Date | Não | Data da Alteração do Vínculo |
| CodVin | Number(002,0) | Sim | Tipo de Vínculo |
| StaHis | Number(001,0) | Sim | Status do Histórico |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt

---

## Índices

### R038HVIIndice2

**Tipo:** Não unico

Campos:
- DatAlt
- NumEmp
- TipCol
- NumCad

### R038HVIIndice3

**Tipo:** Não unico

Campos:
- CodVin

---

## Relacionamentos

### IR_R038HVI_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R038HVI_004

**Tabela:** R022VIN

| Origem | Destino |
|--------|---------|
| CodVin | CodVin |

