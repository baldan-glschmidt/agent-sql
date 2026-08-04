# E075IMP

## Descrição

Cadastros - Produtos - Impostos por Produto

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodImp | String(003) | Não | Código do imposto |
| PerAli | Number(006,3) | Sim | Percentual da Alíquota |
| UniMed | String(003) | Sim | Código da Unidade de Medida utilizada na base de cálculo |
| DatBas | Date | Não | Data base de vigência da alíquota do imposto |

---

## Chave Primária

- CodEmp
- CodPro
- CodImp
- DatBas

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E075IMP_001

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

### IR_E075IMP_002

**Tabela:** E051IMP

| Origem | Destino |
|--------|---------|
| CodImp | CodImp |

### IR_E075IMP_004

**Tabela:** E015MED

| Origem | Destino |
|--------|---------|
| UniMed | UniMed |

