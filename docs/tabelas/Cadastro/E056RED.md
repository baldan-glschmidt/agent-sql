# E056RED

## Descrição

Cadastros - Tributos - Unidade Imobiliária - Redutores

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodImo | String(020) | Não | Código da unidade imobiliária |
| SeqRed | Number(003,0) | Não | Sequência do redutor |
| DatIni | Date | Não | Data início de vigência da redução |
| VlrRed | Number(015,2) | Sim | Valor do Redutor |
| VlrRfr | Number(015,2) | Sim | Valor por unidade |

---

## Chave Primária

- CodEmp
- CodImo
- SeqRed

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E056RED_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E056RED_001

**Tabela:** E056IMO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodImo | CodImo |

