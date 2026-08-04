# E210RES

## Descrição

Estoques - Produtos Reservados

---

## Resumo

- Campos: 12
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação |
| CodDep | String(010) | Não | Código do depósito movimentado |
| QtdRes | Number(014,5) | Sim | Quantidade reservada |
| IdeDre | Number(009,0) | Não | Identificação do registro da tabela de documentos de reserva |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| NumSep | String(050) | Não | Número de série do produto |
| CodLot | String(050) | Não | Código do lote de fabricação do produto |

---

## Chave Primária

- IdeUni

---

## Índices

### E210RESIndice1

**Tipo:** Não unico

Campos:
- IdeDre

### E210RESIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodPro
- CodDer
- CodDep

---

## Relacionamentos

### IR_E210RES_004

**Tabela:** E210EST

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |
| CodDep | CodDep |

### IR_E210RES_006

**Tabela:** E210DRE

| Origem | Destino |
|--------|---------|
| IdeDre | IdeUni |

